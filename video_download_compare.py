# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:50:05 2024

@author: UgoGard
"""

# Import necessary modules
import os
from pytube import YouTube
from threading import Thread, Semaphore, Lock
import logging
import time


# Define a function to read URLs from a file
def read_video_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls


# Specify the path to the file
file_path = 'video_urls.txt'
# Read the URLs
video_urls = read_video_urls(file_path)
# Print the URLs to verify
for url in video_urls:
    print(url)


# Function to download a video - Serial execution
def download_video_serial(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
    print(f"Downloaded: {yt.title}")


# Function to download a video - Parallel execution
def download_video_parallel(url, output_path, semaphore):
    with semaphore:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        print(f"Downloaded: {yt.title}")


def main():
    # Directory to save the videos
    output_path = 'downloads'
    os.makedirs(output_path, exist_ok=True)

    # Measure time for serial execution
    start_time_serial = time.time()

    # Download videos serially
    for url in video_urls:
        download_video_serial(url, output_path)

    end_time_serial = time.time()

    # Semaphore to limit the number of concurrent downloads
    semaphore = Semaphore(5)
    threads = []


    # Measure time for parallel execution
    start_time_parallel = time.time()

    # Download videos in parallel
    for url in video_urls:
        thread = Thread(target=download_video_parallel, args=(url, output_path, semaphore))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time_parallel = time.time()
    
    # Compare serial and parallel executions for your video download script 
    print(f"Serial execution time: {end_time_serial - start_time_serial} seconds")
    print(f"Parallel execution time: {end_time_parallel - start_time_parallel} seconds")


if __name__ == "__main__":
    main()


