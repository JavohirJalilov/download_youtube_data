#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Error: YouTube URL is required."
  echo "Usage: ./run.sh <youtube_channel_or_playlist_url>"
  exit 1
fi

URL="$1"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
  source venv/bin/activate
else
  echo "Error: Virtual environment 'venv' not found. Please run setup first."
  exit 1
fi

# Run the python script in the background using nohup
nohup python main.py "$URL" > download.log 2>&1 &

# Store the Process ID
PID=$!

INFO="=====================================================
✅ Download started successfully in the background!
=====================================================
Process ID (PID): $PID
Log file: download.log

To watch the progress live, run:
  tail -f download.log

To stop the download, run:
  kill $PID
====================================================="

# Print to console
echo "$INFO"

# Also append to the log file so the user doesn't lose the PID
echo "$INFO" >> download.log

