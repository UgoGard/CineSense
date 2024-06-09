# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:17:56 2024

@author: UgoGard

Description:
This script extracts audio from video files located in the 'downloads' directory 
and saves the extracted audio as .wav files in dedicated folders under the 'outputs' directory.
It leverages the MoviePy library for video and audio processing and uses multiprocessing
to handle multiple video files concurrently for efficiency.

Usage:
1. Place your .mp4 video files in the 'downloads' directory.
2. Run this script.
3. The extracted audio files will be saved in individual folders within the 'outputs' directory,
   named after the respective video files.

Functions:
- extract_audio(video):
    Extracts audio from a given video file and saves it as a .wav file in a dedicated folder.
    
- main():
    Retrieves video filenames from the 'downloads' directory, creates a list of filenames 
    (without extensions), and utilizes multiprocessing to extract audio from each video file concurrently.

Dependencies:
- glob
- os
- moviepy.editor (install via `pip install moviepy`)
- pathlib
- multiprocessing

Ensure you have the necessary permissions to read from the 'downloads' directory and write to the 'outputs' directory.
"""

# Import necessary modules
import glob
import os
import logging
from moviepy.editor import VideoFileClip
from pathlib import Path
from multiprocessing import Pool


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_audio(video):
    """
    Extracts audio from a given video file and saves it as a .wav file.

    Parameters:
    video (str): The name of the video file (without extension).

    The function creates a dedicated folder 'outputs/{video}' for each video and 
    saves the extracted audio as 'outputs/{video}/{video}.wav'.
    """
    
    video_path = f"downloads/{video}.mp4"
    output_path = f"outputs/{video}/{video}.wav"
    # Create a dedicated folder "outputs/{filename}"
    Path(f"outputs/{video}").mkdir(parents=True, exist_ok=True)
    logging.info(f"Folder outputs/{video} created")
    # Extract audio from video file
    video_clip = VideoFileClip(video_path)
    video_clip.audio.write_audiofile(output_path)
    logging.info(f"Extracted audio: {output_path}")


def main():
    # Retrieve video filenames and create filenames list
    downloads = glob.glob("downloads/*.mp4")
    videos = [os.path.basename(download)[0:-4] for download in downloads]
    
    # Create a pool of workers and map the extract_audio function to each video
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(extract_audio, videos)


if __name__ == "__main__":
    main()
