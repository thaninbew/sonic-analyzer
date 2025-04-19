# Sonic Analyzer

A Python script for analyzing and comparing audio recordings from different microphones. The script generates multiple visualizations to help understand the differences in how microphones capture sound.

## Features

1. **Waveform Zoom (Transient Response)**
   - Shows detailed waveform comparison starting slightly before a consonant/transient
   - Default: Starts 50ms before the specified consonant time and extends forward for the specified duration
   - Both microphones shown with identical amplitude scaling for direct comparison
   - Consonant time marked with a red vertical line

2. **Full Spectrograms**
   - Complete frequency-over-time visualization for both recordings
   - Shows full frequency range up to Nyquist frequency
   - Uses Hann window with 2048-point FFT and 50% overlap

3. **Focused Spectrograms with Average Response**
   - Detailed spectrogram view of the transient region
   - Shows frequency content from 50ms before consonant through specified duration
   - Includes average frequency response comparison between mics for the focused region
   - Consonant time marked with red vertical line

4. **Static Spectrum Snapshot**
   - Frequency response comparison at a specific vowel sound
   - Both microphones overlaid for direct comparison
   - Data exported to CSV for further analysis

## Usage

1. Place your audio files in the same directory as the script
2. Update the following parameters in the script:
   ```python
   file1 = 'sm7b.wav'        # First microphone recording
   file2 = 'samson.wav'      # Second microphone recording
   
   # Transient analysis settings
   consonant_time = 0.490    # Time of the consonant/transient
   zoom_width = 0.5          # Duration to analyze after consonant
   
   # Vowel analysis settings
   vowel_center = 1.141      # Time of the vowel sound
   vowel_duration = 0.1      # Duration of vowel analysis window
   ```

3. Run the script:
   ```bash
   python sonic-analyzer-fixed.py
   ```

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SciPy
- Pandas

## Output

The script generates:
- Interactive plots for all visualizations
- A CSV file (`spectrum_comparison.csv`) with the frequency response data

## Notes

- Audio files should be WAV format
- Stereo files will be converted to mono (using first channel)
- The script includes error handling for missing files and invalid parameters
- All time values are in seconds
- Frequency analysis extends to the Nyquist frequency (half the sample rate)

## Setup

1. **Install Python:**
   - Download and install Python 3.7+ from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Install Dependencies:**
   - Open a command prompt or terminal in this directory
   - Run: `pip install -r requirements.txt`

3. **Prepare Audio Files:**
   - Place two WAV files in this directory:
     - `sm7b.wav`: Recording from an SM7B microphone
     - `samson.wav`: Recording from a Samson microphone
   - Files should contain the same spoken content for proper comparison

## Running the Script

### Testing the Setup

Before running the main script, verify your setup:

1. Test matplotlib:
   ```
   python test_matplotlib.py
   ```
   This should open a window with a simple sine wave graph.

2. Test audio file loading:
   ```
   python test_audio.py
   ```
   This will verify if your audio files exist and can be read.

### Running the Main Analysis

```
python sonic-analyzer.py
```

This will generate and display:
- Waveform zooms showing transient response
- Spectrograms showing frequency content over time
- Static spectrum snapshots showing frequency response
- A CSV file with the spectrum data for further analysis

## Troubleshooting

If you see a red error or no output:

1. **Missing Audio Files:**
   - Ensure both `sm7b.wav` and `samson.wav` exist in the same folder as the script
   - Try using different audio files and update the filenames in the script

2. **Matplotlib Display Issues:**
   - Try running with a different backend:
     ```
     set MPLBACKEND=TkAgg
     python sonic-analyzer.py
     ```
   - For Windows, you might need to install additional libraries:
     ```
     pip install pywin32
     ```

3. **Dependencies Issues:**
   - Try updating your dependencies:
     ```
     pip install --upgrade -r requirements.txt
     ```
   - Reboot your computer after installation

4. **Python Version Conflict:**
   - Check which Python version is running:
     ```
     python --version
     ```
   - Make sure pip is installing packages for the correct Python version
   
## Customization

Edit the parameters at the top of `sonic-analyzer.py` to:
- Adjust the zoom window location and width
- Change the vowel center and duration
- Modify spectrogram settings 