# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:28:17 2024

@author: UgoGard

This script translates transcription files from English to a target language (default is Spanish) using Google Translate API.
The translated files are saved in the same directory as the original transcription files.

Functions:
    translate_file(file_path, target_language='es'):
        Translates the content of a transcription file into the target language and saves it as a new file.

    main():
        Identifies transcription files in the 'outputs/' directory and translates them in parallel using multiprocessing.

Usage:
    Run the script directly to process all transcription files in the 'outputs/' directory and save their translations.
"""

# Import necessary modules
import os
import logging
from deep_translator import GoogleTranslator
from multiprocessing import Pool


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def translate_file(file_path, target_language='es'):
    """
    Translates the content of a transcription file into the target language and saves it as a new file.

    Args:
        file_path (str): The path to the transcription file to be translated.
        target_language (str): The language code to translate the text into (default is 'es' for Spanish).

    Returns:
        None
    """

    with open(file_path, "r", encoding='utf-8') as file:
        text = file.read()
    
    translation = GoogleTranslator(source='auto', target=target_language).translate(text)
    translation_path = file_path.replace("transcription.txt", "translation.txt")
    logging.info(f"Translation for {translation_path}: {translation}")
    
    with open(translation_path, "w", encoding='utf-8') as file:
        file.write(translation)


def main():
    output_dir = "outputs/"
    # Get list of transcription files
    # Create a list of transcription files to process
    files_to_process = [f"{output_dir}{filename}/transcription.txt" for filename in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, filename))]

    # Create a pool of worker processes and translate files in parallel
    with Pool() as pool:
        pool.map(translate_file, files_to_process)


if __name__ == "__main__":
    main()
