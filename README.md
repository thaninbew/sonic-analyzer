# Sonic Analyzer

A Python script for analyzing and comparing audio recordings from different microphones.

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