# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:56:30 2024

@author: UgoGard

This script reads transcription files, performs sentiment analysis to extract emotions,
and writes the results to new files in the same directories as the original transcriptions.

Dependencies:
- spacy
- nltk
- multiprocessing
- nrclex

Functions:
- extract_emotions: Extracts emotions from a given text using NRCLex.
- process_file: Reads a transcription file, performs sentiment analysis, and writes the results to a new file.
- main: Main function that sets up the processing pipeline using multiprocessing to handle multiple files in parallel.

Usage:
1. Ensure the necessary packages are installed.
2. Place transcription files in the 'outputs/' directory, where each transcription is in its own subdirectory.
3. Run the script.

The script will create new files named 'emotions.txt' in each subdirectory, containing the detected emotions and their frequencies.
"""

# Import necessary modules
import spacy,nltk
import os
import logging
from multiprocessing import Pool
from nrclex import NRCLex


# Download necessary NLTK resources
nltk.download('punkt', quiet=True)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to load the SpaCy model with automatic download if not available
def load_spacy_model(model_name):
    try:
        nlp = spacy.load(model_name)
    except OSError:
        logging.info(f"Model '{model_name}' not found. Downloading...")
        from spacy.cli import download
        download(model_name)
        nlp = spacy.load(model_name)
    return nlp


# Load SpaCy model
nlp = load_spacy_model('en_core_web_sm')


def extract_emotions(text):
    """
    Extracts emotions from a given text using NRCLex.

    Parameters:
    text (str): The text from which to extract emotions.

    Returns:
    NRCLex: An NRCLex object containing the detected emotions and their frequencies.
    """

    emotions = NRCLex(text)
    
    return emotions


def process_file(file_path):
    """
    Reads a transcription file, performs sentiment analysis, and writes the results to a new file.

    Parameters:
    file_path (str): The path to the transcription file.

    Returns:
    None
    """

    with open(file_path, "r") as file:
        text = file.read()
    
    emotions = extract_emotions(text)
    emotions_file_path = file_path.replace("transcription.txt", "emotions.txt")
    logging.info(f"Emotions for {emotions_file_path}: {emotions.affect_frequencies}")
    
    with open(emotions_file_path, "w") as file:
        file.write(str(emotions.affect_frequencies))


def main():
    output_dir = "outputs/"
    # Get list of transcription files
    # Create a list of transcription files to process
    files_to_process = [f"{output_dir}{filename}/transcription.txt" for filename in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, filename))]

    # Create a pool of worker processes
    with Pool() as pool:
        pool.map(process_file, files_to_process)


if __name__ == "__main__":
    main()
