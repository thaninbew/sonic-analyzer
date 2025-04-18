import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram, get_window
import pandas as pd
import os
import sys
import traceback

# Print Python and package versions for debugging
print(f"Python version: {sys.version}")
print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {matplotlib.__version__}")
print(f"SciPy version: {__import__('scipy').__version__}")
print(f"Pandas version: {pd.__version__}")

# Set the backend explicitly for Windows compatibility
matplotlib.use('TkAgg')
print(f"Using matplotlib backend: {matplotlib.get_backend()}")

# ---------------------
# USER PARAMETERS
# ---------------------
file1 = 'sm7b.wav'        # SM7B recording filename
file2 = 'samson.wav'      # Samson recording filename

# Check if files exist and print status
print(f"Checking for audio files:")
print(f"  {file1} exists: {os.path.exists(file1)}")
print(f"  {file2} exists: {os.path.exists(file2)}")

# Zoom window around a sharp consonant (e.g., a "p" or "t")
consonant_time = 0.490     # seconds where the transient occurs
zoom_width = 0.1         # seconds of window width (e.g., 20 ms)

# Static spectrum snapshot around a vowel sound
vowel_center = 2.00       # seconds at center of vowel (e.g., "ah" or "ee")
vowel_duration = 0.05     # seconds of vowel window (e.g., 50 ms)

# Spectrogram settings
n_fft = 2048
hop_length = n_fft // 2
window = 'hann'

try:
    # ---------------------
    # LOAD AUDIO
    # ---------------------
    print("Attempting to load audio files...")
    
    # Check if files exist before trying to load them
    if not os.path.exists(file1):
        print(f"ERROR: File {file1} not found. Please place it in the same directory as this script.")
        sys.exit(1)
    
    sr1, data1 = wavfile.read(file1)
    print(f"Successfully loaded {file1} with sample rate {sr1}Hz and {len(data1)} samples")
    
    if not os.path.exists(file2):
        print(f"WARNING: File {file2} not found. Will analyze only {file1}.")
        # Create dummy data for the second file (silence)
        sr2, data2 = sr1, np.zeros_like(data1)
    else:
        sr2, data2 = wavfile.read(file2)
        print(f"Successfully loaded {file2} with sample rate {sr2}Hz and {len(data2)} samples")

    # Ensure mono
    if data1.ndim > 1: 
        data1 = data1[:,0]
        print(f"Converted {file1} to mono")
    if data2.ndim > 1: 
        data2 = data2[:,0]
        print(f"Converted {file2} to mono")

    # ---------------------
    # 1) WAVEFORM ZOOM (Transient Response)
    # ---------------------
    print("Generating waveform plots...")
    for idx, (data, sr, label) in enumerate([(data1, sr1, 'SM7B'), (data2, sr2, 'Samson')], start=1):
        start = int((consonant_time - zoom_width/2) * sr)
        end   = int((consonant_time + zoom_width/2) * sr)
        
        # Safety check to avoid index errors
        if start < 0:
            start = 0
        if end >= len(data):
            end = len(data) - 1
            
        if end <= start:
            print(f"WARNING: Invalid time window for {label}. Skipping waveform plot.")
            continue
            
        t_zoom = np.linspace(consonant_time - zoom_width/2,
                             consonant_time + zoom_width/2,
                             end - start)
        amp_zoom = data[start:end]
        
        plt.figure()
        plt.plot(t_zoom, amp_zoom)
        plt.title(f'{label} Transient Zoom ({zoom_width*1000:.0f} ms around {consonant_time:.2f}s)')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.tight_layout()
        print(f"  Created waveform plot for {label}")

    # ---------------------
    # 2) SPECTROGRAMS (Frequency over Time)
    # ---------------------
    print("Generating spectrograms...")
    for idx, (data, sr, label) in enumerate([(data1, sr1, 'SM7B'), (data2, sr2, 'Samson')], start=1):
        plt.figure()
        plt.specgram(data, NFFT=n_fft, Fs=sr, noverlap=hop_length, window=get_window(window, n_fft))
        plt.title(f'{label} Spectrogram (n_fft={n_fft}, hop={hop_length})')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.ylim(0, sr//2)
        plt.colorbar(label='Intensity [dB]')
        plt.tight_layout()
        print(f"  Created spectrogram for {label}")

    # ---------------------
    # 3) STATIC SPECTRUM SNAPSHOT (Frequency Distribution)
    # ---------------------
    print("Generating static spectrum snapshot...")
    # Extract vowel slices
    vstart1 = int((vowel_center - vowel_duration/2) * sr1)
    vend1   = int((vowel_center + vowel_duration/2) * sr1)
    
    # Safety check
    if vstart1 < 0:
        vstart1 = 0
    if vend1 >= len(data1):
        vend1 = len(data1) - 1
        
    slice1 = data1[vstart1:vend1] * get_window(window, vend1-vstart1)

    vstart2 = int((vowel_center - vowel_duration/2) * sr2)
    vend2   = int((vowel_center + vowel_duration/2) * sr2)
    
    # Safety check
    if vstart2 < 0:
        vstart2 = 0
    if vend2 >= len(data2):
        vend2 = len(data2) - 1
        
    slice2 = data2[vstart2:vend2] * get_window(window, vend2-vstart2)

    # FFT
    N = 4096
    freqs = np.fft.rfftfreq(N, 1/sr1)
    fft1 = np.abs(np.fft.rfft(slice1, n=N))
    fft2 = np.abs(np.fft.rfft(slice2, n=N))
    
    # Avoid divide by zero
    max_fft1 = np.max(fft1)
    max_fft2 = np.max(fft2)
    
    if max_fft1 > 0:
        db1 = 20 * np.log10(fft1 / max_fft1)
    else:
        db1 = np.zeros_like(fft1)
        
    if max_fft2 > 0:
        db2 = 20 * np.log10(fft2 / max_fft2)
    else:
        db2 = np.zeros_like(fft2)

    # Plot overlay
    plt.figure()
    plt.plot(freqs, db1, label='SM7B')
    plt.plot(freqs, db2, label='Samson')
    plt.title(f'Static Spectrum ({vowel_duration*1000:.0f} ms around {vowel_center:.2f}s)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB, normalized)')
    plt.xlim(0, sr1//2)
    plt.legend()
    plt.tight_layout()
    print("  Created static spectrum plot")

    # Save CSV for annotation (optional)
    df = pd.DataFrame({'frequency': freqs, 'SM7B_dB': db1, 'Samson_dB': db2})
    df.to_csv('spectrum_comparison.csv', index=False)
    print("Saved spectrum data to 'spectrum_comparison.csv'")

    print("Displaying plots...")
    plt.show()
    print("Script completed successfully!")

except FileNotFoundError as e:
    print(f"ERROR: File not found: {e}")
    print(f"Please make sure the audio files ({file1} and {file2}) are in the same directory as this script.")
    
except Exception as e:
    print(f"ERROR: An unexpected error occurred: {e}")
    print("Detailed error information:")
    traceback.print_exc()
    
    # Try to save the current plots even if there was an error
    try:
        print("Attempting to display any plots that were generated before the error...")
        plt.show()
    except:
        print("Could not display plots.")

print("End of script execution.") 