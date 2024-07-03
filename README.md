CineSense
Technical Report
Author: Ugo Gard
Student ID: 131865582

Context

CineSense is an innovative video-processing startup that extracts valuable insights from social media video content. It uses advanced natural language processing (NLP) and computer vision techniques to analyse videos' sentiments and emotions. This analysis is crucial for businesses seeking to understand their audience, improve customer experiences, and make data-driven decisions.
On your first day at CineSense as a data engineer, you were assigned a critical project: find the best strategy to download and analyse videos. CineSense uses YouTube videos posted by its target audience. Each video must be analysed, and results should be extracted and shared with customers. Usual tasks include extracting video, audio, transcripts, sentiments, and emotions. Since you are paired with a customer from Madrid, you will also need to transcribe videos in Spanish.
Thanks to Python, you can showcase your skills and automate the tasks. Your project leader is particularly looking for a strategy to complete tasks faster! Parallel processing concepts can help you speed up your analysis tasks, contributing to your company's success.

Technical Writing

run_pipeline.sh
The script outlines a multi-step pipeline to handle a series of tasks from downloading videos to analyzing their audio content. Let's break down each step in more detail and consider the potential implementation of each Python script.
This pipeline efficiently manages the entire process of downloading, extracting, transcribing, analyzing, and translating video content. Each script performs a specific task, contributing to the overall workflow.
Requirements:
-	requirements.txt: Contain the dependencies to install.
-	video_urls.txt: Contain video urls to read.
Step-by-Step Breakdown:
1.	Install Required Python Packages
-	Command: pip install -r requirements.txt
-	Purpose: Install all necessary Python packages as listed in the requirements.txt file. This file typically contains package names and their versions.
2.	Download Videos
-	Command: python video_download.py -i video_urls.txt -o downloads -c 5 -l download_log.txt
-	Purpose: Download videos from URLs listed in video_urls.txt. Save them to the downloads directory, use 5 concurrent download threads, and log the download process in download_log.txt.
3.	Extract Audio from Videos
-	Command: python extract_audio.py
-	Purpose: Extract audio tracks from the downloaded videos.
4.	Transcribe the Audio
-	Command: python transcribe_audio.py
-	Purpose: Convert the audio files into text using a speech-to-text system.
5.	Perform Sentiment Analysis on the Transcribed Text
-	Command: python sentiment_analysis.py
-	Purpose: Analyze the sentiment (positive, negative, neutral) of the transcribed text.
6.	Translate the Text
-	Command: python translate_text.py
-	Purpose: Translate the transcribed text into another language (e.g., English to Spanish).
7.	Extract Emotions from the Transcribed Text
-	Command: python translate_text.py
-	Purpose: Translate the transcribed text into another language (e.g., English to Spanish).

video_download.py
This script reads a list of YouTube video URLs from a file, downloads each video to a specified directory,
and logs the downloads. The downloads are managed concurrently using threads and a semaphore to limit the number
of concurrent downloads. Logging is synchronized using a lock to prevent race conditions.
Dependencies:
-	pytube: Used for downloading YouTube videos.
-	threading: Used for concurrent downloading of videos.
-	os: Used for directory creation.
-	logging: Used for logging download information.
Functions:
-	read_video_urls(file_path): Reads video URLs from a file and returns them as a list.
-	download_video(url, output_path, semaphore, log_lock): Downloads a video from YouTube and logs the download.
-	main(): Main function to read video URLs from a file and download them concurrently.
Usage:
-	Ensure 'video_urls.txt' contains the list of YouTube video URLs to be downloaded, one URL per line.
-	Run the script, and it will download the videos to a 'downloads' directory and log the details in 'download_log.txt'.

read_video_urls(file_path)
Read video URLs from a file and return them as a list.
Parameters:
-	file_path (str): The path to the file containing video URLs.
Returns:
-	list: A list of video URLs.

download_video(url, output_path, semaphore, log_lock)
Download a video from YouTube and save it in a folder named after the video title. Log the download using a shared log lock to prevent race conditions.
Parameters:
-	url (str): The URL of the YouTube video to download.
-	output_path (str): The directory where the video will be saved.
-	semaphore (Semaphore): A semaphore to limit the number of concurrent downloads.
-	log_lock (Lock): A lock to synchronize access to the log file.
Returns:
-	None

extract_audio.py
Description:
This script extracts audio from video files located in the 'downloads' directory and saves the extracted audio as .wav files in dedicated folders under the 'outputs' directory. It leverages the MoviePy library for video and audio processing and uses multiprocessing to handle multiple video files concurrently for efficiency.
Dependencies:
-	glob
-	os
-	moviepy.editor
-	pathlib
-	multiprocessing
Functions:
-	extract_audio(video): Extracts audio from a given video file and saves it as a .wav file in a dedicated folder.
-	main(): Retrieves video filenames from the 'downloads' directory, creates a list of filenames  (without extensions), and utilizes multiprocessing to extract audio from each video file concurrently.
Ensure you have the necessary permissions to read from the 'downloads' directory and write to the 'outputs' directory.
Usage:
-	Place your .mp4 video files in the 'downloads' directory.
-	Run this script.
-	The extracted audio files will be saved in individual folders within the 'outputs' directory, named after the respective video files.

extract_audio(video)
Extracts audio from a given video file and saves it as a .wav file.
Parameters:
-	video (str): The name of the video file (without extension).
The function creates a dedicated folder 'outputs/{video}' for each video and 
saves the extracted audio as 'outputs/{video}/{video}.wav'.
Returns:
-	None

transcribe_audio.py
Description:
This script processes audio files located in the 'outputs' directory. It transcribes each audio file to text using Google's Speech Recognition API and saves the transcription in a text file within the respective output directory.
Dependencies:
-	os
-	logging
-	speech_recognition
-	multiprocessing
Functions:
-	transcribe_audio(audio_path): Transcribes audio from a given file path to text.
-	process_file(audio_file): Processes a single audio file by creating a directory for its output, transcribing the audio, and saving the transcription to a text file.
Usage:
-	Run the script directly to start processing the audio files.

transcribe_audio(audio_path)
Transcribes audio from the given file path to text using Google's Speech Recognition API.
Parameters:
-	audio_path (str): The path to the audio file to be transcribed.
Returns:
-	str: The transcribed text if successful, None otherwise.

process_file(audio_file)
Processes a single audio file by creating a directory for its output, transcribing the audio, and saving the transcription to a text file.
Parameters:
-	audio_file (str): The name of the audio file to be processed.
Returns:
-	None

sentiment_analysis.py
This script performs sentiment analysis on text transcriptions stored in multiple subdirectories within a specified output directory. The sentiment analysis is conducted using the TextBlob library.
Dependencies:
-	Pytube
-	Threading
-	Os
-	logging
Functions:
-	sentiment_analysis(text): This function takes a text string as input, performs sentiment analysis using TextBlob, and returns the sentiment polarity and subjectivity.
-	process_file(file_path): This function reads the transcription file from the provided file path, performs sentiment analysis on the text, and writes the resulting sentiment to a new file in the same subdirectory.
Usage:
-	Ensure that the TextBlob library is installed: `pip install textblob`
-	Place the script in the same directory level as the `outputs` folder containing the subdirectories with transcription files.
-	Run the script: `python script_name.py`
The script will read each `transcription.txt` file in the subdirectories, perform sentiment analysis, and save the sentiment results in a `sentiment.txt` file in the same subdirectory.

sentiment_analysis(text)
Perform sentiment analysis on the given text using TextBlob.
Parameters:
-	text (str): The text to analyze.
Returns:
-	TextBlob.sentiment: The sentiment of the text, represented as a named tuple containing polarity and subjectivity.

process_file(file_path)
Read the transcription file, perform sentiment analysis, and write the result to a new file.
Parameters:
-	file_path (str): The path to the transcription file.
Returns:
-	None
Reads the content of the transcription file, performs sentiment analysis, and writes the sentiment result to a new file named 'sentiment.txt' in the same directory as the transcription file.

translate_text.py
This script translates transcription files from English to a target language (default is Spanish) using Google Translate API. The translated files are saved in the same directory as the original transcription files.
Dependencies:
-	os
-	logging
-	deep_translator
-	multiprocessing
Functions:
-	translate_file(file_path, target_language='es'): Translates the content of a transcription file into the target language and saves it as a new file.
-	main(): Identifies transcription files in the 'outputs/' directory and translates them in parallel using multiprocessing.
Usage:
-	Run the script directly to process all transcription files in the 'outputs/' directory and save their translations.

translate_file(file_path, target_language=’es’)
Translates the content of a transcription file into the target language and saves it as a new file.
Parameters:
-	file_path (str): The path to the transcription file to be translated.
-	target_language (str): The language code to translate the text into (default is 'es' for Spanish).
Returns:
-	None

extract_emotions.py
This script reads transcription files, performs sentiment analysis to extract emotions, and writes the results to new files in the same directories as the original transcriptions.
Dependencies:
-	spacy
-	nltk
-	multiprocessing
-	nrclex
Functions:
-	extract_emotions: Extracts emotions from a given text using NRCLex.
-	process_file: Reads a transcription file, performs sentiment analysis, and writes the results to a new file.
Usage:
-	Ensure the necessary packages are installed.
-	Place transcription files in the 'outputs/' directory, where each transcription is in its own subdirectory.
-	Run the script.
The script will create new files named 'emotions.txt' in each subdirectory, containing the detected emotions and their frequencies.

extract_emotions(text)
Extracts emotions from a given text using NRCLex.
Parameters:
-	text (str): The text from which to extract emotions.
Returns:
-	NRCLex: An NRCLex object containing the detected emotions and their frequencies.

process_file(file_path)
Reads a transcription file, performs sentiment analysis, and writes the results to a new file. Parameters:
-	file_path (str): The path to the transcription file.
Returns:
-	None

Implementation Strategy

Choosing the Right Strategy

Processes (Multiprocessing)
Best for:
-	CPU-bound tasks that can benefit from parallel execution without the complexity of managing shared resources.
Pros:
-	Exploits multi-core processors.
-	Each process runs in its own memory space, avoiding issues with Global Interpreter Lock (GIL) in Python.
Cons:
-	Higher memory usage due to separate memory spaces.
-	Inter-process communication (IPC) can be complex.
Applicable Steps:
-	Audio extraction, sentiment analysis, emotion extraction, and possibly transcription if using libraries like pydub or nltk which benefit from CPU parallelism.

Threads (Multithreading)
Best for:
-	I/O-bound tasks where the primary wait time is due to I/O operations (e.g., downloading files, waiting for API responses).
Pros:
-	Lower memory overhead compared to multiprocessing.
-	Simplifies data sharing via shared memory.
Cons:
-	Limited by Python's GIL for CPU-bound tasks.
-	Risk of race conditions if not managed properly.
Applicable Steps:
-	Downloading videos, as it involves network I/O which can benefit from concurrent connections.

Asynchronous Programming (Asyncio)
Best for:
-	High-level concurrency in I/O-bound operations where tasks spend a lot of time waiting (e.g., network requests, file I/O).
Pros:
-	Efficient context switching, suitable for high-concurrency applications.
-	Lower overhead compared to threading.
Cons:
-	More complex to implement and debug.
-	Requires libraries and APIs that support asynchronous operations.
Applicable Steps:
-	Downloading videos and possibly API interactions for transcription, sentiment analysis, and translation if using non-blocking libraries.

Proposed Strategy for Each Step

Installing Required Python Packages
Strategy: 
-	Simple synchronous execution.
Reason:
-	Package installation is typically a one-time, blocking operation that doesn’t benefit from parallel execution.

Downloading Videos
Strategy:
-	Multithreading.
Reason:
-	Video downloading is I/O-bound, and asynchronous programming allows handling multiple downloads concurrently without the overhead of threads or processes.

Extracting Audio from Videos
Strategy: 
-	Multiprocessing.
Reason:
-	Audio extraction is CPU-bound, especially if the files are large or numerous. Multiprocessing can utilize multiple cores to handle multiple files in parallel.

Transcribing the Audio
Strategy:
-	Multiprocessing.
Reason:
-	CPU-intensive transcription is performed.

Performing Sentiment Analysis
Strategy: 
-	Multiprocessing.
Reason:
-	Sentiment analysis can be CPU-intensive, especially if processing large texts or using complex models. Multiprocessing can distribute the workload across multiple cores.

Translating the Text
Strategy:
-	Multiprocessing.
Reason: 
-	Translation is typically I/O-bound but the translation API or library doesn’t support async operations, in this case, multiprocessing prevents issues by .

Extracting Emotions
Strategy:
-	Multiprocessing.
Reason:
-	Emotion extraction involves analyzing text, which can be CPU-bound if using comprehensive models or processing large amounts of text.

Observations

Compare serial and parallel executions for your video download script
The file video_download_compare.py runs the video download process using serial execution and parallel execution using multithreading.
-	Serial execution takes 44 seconds.
-	Parallel execution - multithreading takes 16 seconds. 
The parallel execution is around 2.5 times faster than the serial execution.

Discuss the complexity of your video download scripts' time and space
The time complexity of the `video_download.py` script is influenced by reading URLs, downloading videos, and logging activities.
-	Reading URLs: Time complexity of O(N) where N is the number of lines in the file. Space complexity of O(N * L) where L is the average length of each URL. 
-	Downloading videos: Time complexity of O(N) where N is the number of videos. Space complexity of O(N * S) where S is the average size of a file.
-	Thread management: Space complexity is O(M) where M is the number of concurrent threads.
-	Logging: Time complexity is O(N) where N is the number of videos. Space complexity is O(N * T) where T is the average size of a log entry.
Combined time complexity is O(N * l) where N is the number of videos and l is the average download time for a video.
Combined space complexity is  O(N + N * S) where N is the number of videos and S the average size of a video.
Compare serial, multiprocessing, threading, and concurrency for at least one of the subtasks, such as the extracting audio functionality
A comparison of serial vs mutliprocessing vs multithreading vs concurrency has been done for the extract_audio feature. The file extracting_audio_compare.py generates execution time for serial, mutliprocessing and multithreading executions. The file extracting_audio_compare2.py generates time for concurrency execution.
-	Serial execution takes 18 seconds.
-	Parallel execution - mutliprocessing takes 6 seconds.
-	Parallel execution - multithreading takes 12 seconds.
-	Concurrency execution takes 20 seconds.
