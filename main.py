import os
import sys
from dotenv import load_dotenv
import yt_dlp

import subprocess

def ensure_nodejs():
    """
    Ensure Node.js is available. YouTube's recent anti-bot protections require
    a JavaScript runtime (like Node.js) to extract videos successfully.
    """
    try:
        subprocess.run(['node', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Node.js is missing but required by yt-dlp to bypass YouTube's protections.")
        print("Installing a local version of Node.js via nodeenv...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'nodeenv'], check=True)
        subprocess.run([sys.executable, '-m', 'nodeenv', '-p'], check=True)
        print("Node.js installed successfully in the virtual environment.\n")

def download_videos(url):
    """
    Downloads videos from a given YouTube channel or playlist URL.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Ensure Node.js is installed for yt-dlp
    ensure_nodejs()
    
    # Get the download directory from .env, default to './downloads'
    download_dir = os.getenv('DOWNLOAD_DIR', './downloads')

    # Ensure the download directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # yt-dlp configuration options
    ydl_opts = {
        # Organize downloads in folders by Uploader -> Playlist -> Video Title
        'outtmpl': os.path.join(download_dir, '%(uploader)s', '%(playlist_title|No Playlist)s', '%(title)s.%(ext)s'),
        
        # Download best mp4 format available or fallback to best
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        
        # Skip unavailable videos and continue
        'ignoreerrors': True,
        
        # Disable the progress bar to prevent spamming the log file with thousands of lines per video
        'noprogress': True,
        
        # Extract metadata
        'extract_flat': False,
        
        # JS runtime configuration to bypass YouTube's signature protection
        'js_runtimes': {'node': {}},
        'extractor_args': {'youtube': ['player-client=web,default']},
    }

    print(f"Starting download for: {url}")
    print(f"Saving videos to: {os.path.abspath(download_dir)}\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownload completed successfully.")
    except Exception as e:
        print(f"\nAn error occurred during the download process: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If URL is passed as a command line argument
        target_url = sys.argv[1]
    else:
        # Otherwise, ask the user for input
        target_url = input("Enter YouTube channel or playlist URL: ").strip()
    
    if target_url:
        download_videos(target_url)
    else:
        print("Error: No URL provided.")
