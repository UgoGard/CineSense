# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:24:31 2024

@author: UgoGard
"""

# Import necessary modules
import glob
import os
import logging
import time
from moviepy.editor import VideoFileClip
from pathlib import Path
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor, as_completed


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_audio(video):
    video_path = f"downloads/{video}.mp4"
    output_path = f"outputs/{video}/{video}.wav"
    # Create a dedicated folder "outputs/{filename}"
    Path(f"outputs/{video}").mkdir(parents=True, exist_ok=True)
    logging.info(f"Folder outputs/{video} created")
    # Extract audio from video file
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)
    logging.info(f"Extracted audio: {output_path}")
    # Ensure resources are released
    video_clip.reader.close()


def main():
    # Retrieve video filenames and create filenames list
    downloads = glob.glob("downloads/*.mp4")
    videos = [os.path.basename(download)[0:-4] for download in downloads]
    
    logging.info("Serial audio extraction starting...")
    # Measure time for serial execution
    start_time_serial = time.time()
    # Process each video file serially
    for video in videos:
        logging.info(f"Processing {video}...")
        extract_audio(video)
    end_time_serial = time.time()
    
    logging.info("Multiprocessing audio extraction starting...")
    # Measure time for parallel execution - multiprocessing
    start_time_parallel_multiprocessing = time.time()    
    # Create a pool of workers and map the extract_audio function to each video
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(extract_audio, videos)
    end_time_parallel_multiprocessing = time.time()
    
    logging.info("Multithreading audio extraction starting...")
    # Measure time for parallel execution - multithreading
    start_time_parallel_multithreading = time.time()    
    # Create a pool of workers and map the extract_audio function to each video
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [executor.submit(extract_audio, video) for video in videos]
        for future in as_completed(futures):
            future.result()  # Retrieve the result to raise any exceptions
    end_time_parallel_multithreading = time.time()     
    
    # Compare serial and parallel executions for extract audio script
    print(f"Serial execution time: {end_time_serial - start_time_serial} seconds")
    print(f"Parallel - multiprocessing execution time: {end_time_parallel_multiprocessing - start_time_parallel_multiprocessing} seconds")
    print(f"Parallel - multithreading execution time: {end_time_parallel_multithreading - start_time_parallel_multithreading} seconds")


if __name__ == "__main__":
    main()
