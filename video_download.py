# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:21:03 2024

@author: UgoGard

This script reads a list of YouTube video URLs from a file, downloads each video to a specified directory,
and logs the downloads. The downloads are managed concurrently using threads and a semaphore to limit the number
of concurrent downloads. Logging is synchronized using a lock to prevent race conditions.

Modules:
    - pytube: Used for downloading YouTube videos.
    - threading: Used for concurrent downloading of videos.
    - os: Used for directory creation.
    - logging: Used for logging download information.

Functions:
    - read_video_urls(file_path): Reads video URLs from a file and returns them as a list.
    - download_video(url, output_path, semaphore, log_lock): Downloads a video from YouTube and logs the download.
    - main(): Main function to read video URLs from a file and download them concurrently.

Usage:
    Ensure 'video_urls.txt' contains the list of YouTube video URLs to be downloaded, one URL per line.
    Run the script, and it will download the videos to a 'downloads' directory and log the details in 'download_log.txt'.

Example:
    To run the script, simply execute it in a Python environment:
        python video_download.py
"""

# Import necessary modules
from pytube import YouTube
from threading import Thread, Semaphore, Lock
import os
import logging


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define a function to read URLs from a file
def read_video_urls(file_path):
    """
    Read video URLs from a file and return them as a list.
    
    Parameters:
    file_path (str): The path to the file containing video URLs.
    
    Returns:
    list: A list of video URLs.
    """

    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    return urls


# Function to download a video and log the download
def download_video(url, output_path, semaphore, log_lock):
    """
    Download a video from YouTube and save it in a folder named after the video title.
    Log the download using a shared log lock to prevent race conditions.
    
    Parameters:
    url (str): The URL of the YouTube video to download.
    output_path (str): The directory where the video will be saved.
    semaphore (Semaphore): A semaphore to limit the number of concurrent downloads.
    log_lock (Lock): A lock to synchronize access to the log file.
    """
   
    with semaphore:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)

        with log_lock:
            logging.info(f"Downloaded: {yt.title}")
        

def main():
    # Set up logging
    logging.basicConfig(filename='download_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Specify the path to the file
    file_path = 'video_urls.txt'

    # Read the URLs
    video_urls = read_video_urls(file_path)

    # Directory to save the videos
    output_path = 'downloads'
    os.makedirs(output_path, exist_ok=True)

    # Semaphore to limit the number of concurrent downloads
    semaphore = Semaphore(5)
    log_lock = Lock()
    threads = []

    # Download videos in parallel with logging
    for url in video_urls:
        thread = Thread(target=download_video, args=(url, output_path, semaphore, log_lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
