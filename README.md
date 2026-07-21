# YouTube Video Downloader

A simple Python application to download all videos from a YouTube channel or playlist using `yt-dlp`.

## Features
- Downloads all videos from a given YouTube channel or playlist URL.
- Automatically creates an organized folder structure: `downloads/Uploader/Playlist/Video Title.mp4`.
- Uses `.env` configuration to easily change the output directory.
- Downloads the best available quality in MP4 format.

## Setup Instructions

1. **Create a virtual environment (already created if you ran the initial setup):**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration (`.env`):**
   You can modify the download destination by editing the `.env` file:
   ```env
   DOWNLOAD_DIR=./downloads
   ```

## Usage

You can run the script in three ways:

**1. Running in the background (Recommended for large channels/playlists):**
For very large playlists or channels, it's highly recommended to run the download in the background so it doesn't stop if you close your terminal.
```bash
./run.sh "https://www.youtube.com/@ToshkentshaharARGOS"
```
*This will start the download in the background using `nohup`, save logs to `download.log`, and provide you with a command to monitor the progress live.*

**2. Passing the URL as an argument:**
```bash
python main.py "https://www.youtube.com/@ToshkentshaharARGOS"
```

**3. Running interactively:**
```bash
python main.py
```
*The script will then prompt you to enter the channel or playlist URL.*

## Note
Depending on the size of the channel or playlist, the download process might take a significant amount of time and disk space.
