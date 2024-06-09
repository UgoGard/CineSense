# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:01:57 2024

@author: UgoGard

This script performs sentiment analysis on text transcriptions stored in multiple subdirectories 
within a specified output directory. The sentiment analysis is conducted using the TextBlob library.

The script defines three main functions:
1. sentiment_analysis(text): This function takes a text string as input, performs sentiment analysis 
   using TextBlob, and returns the sentiment polarity and subjectivity.
2. process_file(file_path): This function reads the transcription file from the provided file path, 
   performs sentiment analysis on the text, and writes the resulting sentiment to a new file in the 
   same subdirectory.
3. main(): This function orchestrates the process by defining the output directory, creating a list 
   of transcription files to process, and utilizing multiprocessing to process the files in parallel.

Usage:
- Ensure that the TextBlob library is installed: `pip install textblob`
- Place the script in the same directory level as the `outputs` folder containing the subdirectories 
  with transcription files.
- Run the script: `python script_name.py`

The script will read each `transcription.txt` file in the subdirectories, perform sentiment analysis, 
and save the sentiment results in a `sentiment.txt` file in the same subdirectory.

Directory Structure:
outputs/
    ├── subdir1/
    │   └── transcription.txt
    ├── subdir2/
    │   └── transcription.txt
    └── subdir3/
        └── transcription.txt

Example of Sentiment Output:
Sentiment(polarity=0.0, subjectivity=0.0)
"""

# Import necessary modules
import os
import logging
from textblob import TextBlob
from multiprocessing import Pool

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to perform sentiment analysis on a given text
def sentiment_analysis(text):
    """
    Perform sentiment analysis on the given text using TextBlob.

    Parameters:
    text (str): The text to analyze.

    Returns:
    TextBlob.sentiment: The sentiment of the text, represented as a named tuple 
    containing polarity and subjectivity.
    """

    blob = TextBlob(text)
    sentiment = blob.sentiment

    return sentiment


# Function to read transcription, perform sentiment analysis, and write the result to a file
def process_file(file_path):
    """
    Read the transcription file, perform sentiment analysis, and write the result 
    to a new file.

    Parameters:
    file_path (str): The path to the transcription file.

    Actions:
    Reads the content of the transcription file, performs sentiment analysis, 
    and writes the sentiment result to a new file named 'sentiment.txt' in the 
    same directory as the transcription file.
    """    
    
    with open(file_path, "r") as file:
        text = file.read()
    
    sentiment = sentiment_analysis(text)
    sentiment_file_path = file_path.replace("transcription.txt", "sentiment.txt")
    logging.info(f"Sentiment for {sentiment_file_path}: {str(sentiment)}")
    
    with open(sentiment_file_path, "w") as file:
        file.write(str(sentiment))


def main():
    # Define the folder path
    output_dir = "outputs/"
    # Create a list of transcription files to process
    files_to_process = [f"{output_dir}{filename}/transcription.txt" for filename in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, filename))]
    
    # Use multiprocessing to process files in parallel
    with Pool() as pool:
        pool.map(process_file, files_to_process)


if __name__ == "__main__":
    main()
