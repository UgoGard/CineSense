# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:12:09 2024

@author: UgoGard

Description:
This script processes audio files located in the 'outputs' directory. It transcribes
each audio file to text using Google's Speech Recognition API and saves the transcription
in a text file within the respective output directory.

Functions:
- transcribe_audio(audio_path): Transcribes audio from a given file path to text.
- process_file(audio_file): Processes a single audio file by creating a directory for its output,
  transcribing the audio, and saving the transcription to a text file.
- main(): Retrieves audio file names from the 'outputs' directory, appends the '.wav' extension,
  and processes them using multiprocessing.

Usage:
Run the script directly to start processing the audio files.
"""

# Import necessary modules
import os
import logging
import speech_recognition as sr
from multiprocessing import Pool


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def transcribe_audio(audio_path):
    """
    Transcribes audio from the given file path to text using Google's Speech Recognition API.

    Parameters:
    audio_path (str): The path to the audio file to be transcribed.

    Returns:
    str: The transcribed text if successful, None otherwise.
    """
    
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language='en-GB')
        logging.info(f"Transcription for {audio_path}: {text}")
        
        return text
    
    except sr.UnknownValueError:
        logging.error(f"Google Speech Recognition could not understand audio {audio_path}")
        
        return None
    
    except sr.RequestError as e:
        logging.error(f"Could not request results from Google Speech Recognition service for {audio_path}; {e}")
        
        return None


def process_file(audio_file):
    """
    Processes a single audio file by creating a directory for its output, 
    transcribing the audio, and saving the transcription to a text file.

    Parameters:
    audio_file (str): The name of the audio file to be processed.
    """

    folder = f"outputs/{audio_file[0:-4]}"
    
    # Ensure the output directory exists
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    audio_path = f"{folder}/{audio_file}"
    transcription = transcribe_audio(audio_path)
    
    if transcription:
        with open(os.path.join(folder, "transcription.txt"), "w") as file:
            file.write(transcription)


def main():
    # Get the list of filenames in the outputs directory and append ".wav"
    output_dir = "outputs"
    audio_files = [f"{filename}.wav" for filename in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, filename))]
    
    # Use multiprocessing Pool to process files concurrently
    with Pool() as pool:
        pool.map(process_file, audio_files)


if __name__ == "__main__":
    main()
