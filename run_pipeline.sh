#!/bin/bash

# Step 1: Install required Python packages
echo "Installing required packages..."
pip install -r requirements.txt

# Step 2: Download videos
echo "Downloading videos..."
python video_download.py -i video_urls.txt -o downloads -c 5 -l download_log.txt

# Step 3: Extract audio from videos
echo "Extracting audio..."
python extract_audio.py

# Step 4: Transcribe the audio
echo "Transcribing audio..."
python transcribe_audio.py

# Step 5: Perform sentiment analysis on the transcribed text
echo "Performing sentiment analysis..."
python sentiment_analysis.py

# Step 6: Translate the text
echo "Translating text..."
python translate_text.py

# Step 7: Extract emotions from transcribed text
echo "Extracting emotions..."
python extract_emotions.py

echo "Pipeline executed successfully."
