# **SplitTracks-ForLive**

This Python script was developed specifically to address the **2GB file size limitation in Ableton Live**, which prevents loading large FLAC or WAV files. The script splits audio files into smaller chunks, ensuring compatibility with Ableton’s requirements. You can easily select either a single file or an entire folder for automatic processing, making this tool ideal for preparing audio files for seamless integration into Ableton Live projects.

---

## **Features**

- **Supports FLAC and WAV**: Splits audio files into smaller chunks based on a configurable maximum file size.
- **Process Folders or Files**: Choose individual files or complete folders for processing.
- **User-Friendly Interface**: Select files or folders directly via Finder (macOS) or Explorer (Windows).
- **Automatic Progress Tracking**: Visual progress is displayed during file processing.

---

## **Requirements**

### **1. Python**
Ensure Python 3.7 or newer is installed.

- Check Python version:
  ```bash
  python3 --version
  ```
- If Python is not installed:
  - **macOS**: Install Python via Homebrew:
    ```bash
    brew install python
    ```
  - **Ubuntu/Debian**: Install Python via APT:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

### **2. Required Python Packages**
Install the required packages using:
```bash
python3 -m pip install pydub tqdm
```

### **3. FFmpeg**
FFmpeg is required for audio processing.

- **macOS** (via Homebrew):
  ```bash
  brew install ffmpeg
  ```
- **Ubuntu/Debian**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```
- **Windows**:
  - Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
  - Extract the files and add the `bin` folder to your system's `PATH`.

Verify the installation:
```bash
ffmpeg -version
```

---

## **Installation**

1. Download the `flac_splitter.py` script.
2. Save it in a folder of your choice, e.g., `~/Documents/SplitTracks/`.

---

## **How to Use**

### **1. Run the Script**
Run the script using Python:
```bash
python3 flac_splitter.py
```

### **2. Select Mode**
When prompted:
- **Type `f`** to choose a single FLAC or WAV file.
- **Type `d`** to choose a folder containing multiple FLAC or WAV files.

### **3. Process the Files**
- The script automatically creates a `Cut` subfolder in the same directory as the selected file or folder.
- All split files are saved in this `Cut` folder.

### **4. Track Progress**
The script displays progress for each file, ensuring transparency during processing.

---

## **How to Avoid Gaps When Importing into Ableton Live**

When you import the split files into Ableton Live, they might appear on a single track with unwanted gaps between clips. To fix this:

1. **Import into the Session View First**:
   - Drag all split files into the **Session View** (vertical clip view) instead of directly into the Arrangement View.
   - This ensures the clips are neatly organized without gaps.

2. **Select All Clips**:
   - Highlight all clips imported into the Session View.

3. **Drag to Arrangement View**:
   - Drag the selected clips to the **Arrangement View** (horizontal timeline view).
   - The clips will align seamlessly without gaps.

This method ensures smooth playback without interruptions in your Ableton Live project.

---

## **Example Output**

### **File Selected**
```plaintext
Welcome to the FLAC/WAV Splitter!
Select a file or folder...
Type 'f' to select a file or 'd' to select a directory: f
Selected path: /Users/username/Music/track1.flac
Output folder: /Users/username/Music/Cut
Processing file: /Users/username/Music/track1.flac
Splitting track1: 100%|████████████████████████████████████████| 4/4 [00:10<00:00,  2.50s/it]
Exported: /Users/username/Music/Cut/track1 Cut 1.flac
Exported: /Users/username/Music/Cut/track1 Cut 2.flac
All tasks completed successfully!
```

### **Folder Selected**
```plaintext
Welcome to the FLAC/WAV Splitter!
Select a file or folder...
Type 'f' to select a file or 'd' to select a directory: d
Selected path: /Users/username/Music
Output folder: /Users/username/Music/Cut
Processing all files in directory: /Users/username/Music
Processing file: /Users/username/Music/track1.flac
Processing file: /Users/username/Music/track2.wav
...
All tasks completed successfully!
```

---

## **Common Issues**

1. **`ModuleNotFoundError: No module named 'pydub'`**
   - Ensure `pydub` is installed:
     ```bash
     python3 -m pip install pydub
     ```

2. **`FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`**
   - FFmpeg is not installed or not in your system's `PATH`.
   - Verify installation:
     ```bash
     ffmpeg -version
     ```

3. **Finder/Explorer Opens in Background**
   - Ensure the Finder/Explorer dialog is brought to the foreground. The script handles this automatically.

---

## **Customization**

To change the maximum file size for splitting, update the `max_file_size_mb` value in the script:
```python
max_file_size_mb=2000
```

---

## **License**

This project is licensed under the MIT License. You are free to use, modify, and distribute it as needed.

---