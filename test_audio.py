import numpy as np
import os
import sys
from scipy.io import wavfile

print(f"Python version: {sys.version}")
print(f"NumPy version: {np.__version__}")
print(f"SciPy version: {__import__('scipy').__version__}")

# Paths to audio files
file1 = 'sm7b.wav'
file2 = 'samson.wav'

# Check if files exist
print(f"Checking for audio files:")
print(f"  {file1} exists: {os.path.exists(file1)}")
print(f"  {file2} exists: {os.path.exists(file2)}")

# Try to read files that exist
if os.path.exists(file1):
    try:
        sr, data = wavfile.read(file1)
        print(f"Successfully read {file1}:")
        print(f"  Sample rate: {sr} Hz")
        print(f"  Samples: {len(data)}")
        print(f"  Duration: {len(data)/sr:.2f} seconds")
        print(f"  Channels: {2 if data.ndim > 1 else 1}")
        print(f"  Data type: {data.dtype}")
    except Exception as e:
        print(f"Error reading {file1}: {e}")

if os.path.exists(file2):
    try:
        sr, data = wavfile.read(file2)
        print(f"Successfully read {file2}:")
        print(f"  Sample rate: {sr} Hz")
        print(f"  Samples: {len(data)}")
        print(f"  Duration: {len(data)/sr:.2f} seconds")
        print(f"  Channels: {2 if data.ndim > 1 else 1}")
        print(f"  Data type: {data.dtype}")
    except Exception as e:
        print(f"Error reading {file2}: {e}")

print("Audio test completed") 