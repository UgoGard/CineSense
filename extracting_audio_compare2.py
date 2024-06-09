# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:52:25 2024

@author: UgoGard
"""

# Import necessary modules
import glob
import os
import logging
import time
from moviepy.editor import VideoFileClip
from pathlib import Path
import asyncio
import aiofiles
from aiomultiprocess import Pool

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def extract_audio(video):
    """
    Extracts audio from a given video file and saves it as a .wav file asynchronously.

    Parameters:
    video (str): The name of the video file (without extension).

    The function creates a dedicated folder 'outputs/{video}' for each video and 
    saves the extracted audio as 'outputs/{video}/{video}.wav'.
    """
    try:
        video_path = f"downloads/{video}.mp4"
        output_path = f"outputs/{video}/{video}.wav"
        
        # Create a dedicated folder "outputs/{video}"
        Path(f"outputs/{video}").mkdir(parents=True, exist_ok=True)
        logging.info(f"Folder outputs/{video} created")
        
        # Extract audio from video file
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        
        # Save the extracted audio asynchronously using aiofiles
        async with aiofiles.open(output_path, 'wb') as f:
            audio_clip.write_audiofile(output_path)
        
        logging.info(f"Extracted audio: {output_path}")
        
        # Ensure resources are released
        video_clip.reader.close()
        
    except Exception as e:
        logging.error(f"Failed to extract audio from {video}: {e}")


async def main():
    try:
        # Retrieve video filenames and create filenames list
        downloads = glob.glob("downloads/*.mp4")
        if not downloads:
            logging.warning("No video files found in the 'downloads' directory.")
            return
        
        videos = [os.path.basename(download)[0:-4] for download in downloads]
        
        # Measure time for parallel execution - multithreading
        start_time_concurrency = time.time()  
        # Process each video file using asynchronous execution with aiomultiprocess Pool
        async with Pool() as pool:
            await pool.map(extract_audio, videos)
        end_time_concurrency = time.time()
        print(f"Concurrency execution time: {end_time_concurrency - start_time_concurrency} seconds")
        
    except Exception as e:
        logging.error(f"Error in main function: {e}")


if __name__ == "__main__":
    # Run the main function using asyncio
    asyncio.run(main())
