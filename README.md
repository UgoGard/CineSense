# CineSense

CineSense is an innovative video-processing startup that extracts valuable insights from social media video
content. It uses advanced natural language processing (NLP) and computer vision techniques to analyse
videos' sentiments and emotions. This analysis is crucial for businesses seeking to understand their
audience, improve customer experiences, and make data-driven decisions.
On your first day at CineSense as a data engineer, you were assigned a critical project: find the best
strategy to download and analyse videos. CineSense uses YouTube videos posted by its target audience.
Each video must be analysed, and results should be extracted and shared with customers. Usual tasks
include extracting video, audio, transcripts, sentiments, and emotions. Since you are paired with a
customer from Madrid, you will also need to transcribe videos in Spanish.
Thanks to Python, you can showcase your skills and automate the tasks. Your project leader is particularly
looking for a strategy to complete tasks faster! Parallel processing concepts can help you speed up your
analysis tasks, contributing to your company's success. Your colleagues prepared a project description
and a set of skeleton scripts for your developments provided.

Part 1: Project description

Develop a Python application using multiprocessing, threading or asynchronous programming
concepts to download and analyse YouTube videos.
Compare and contrast different solutions for serial and parallel processing executions.
You have four weeks to complete all the tasks and document your solutions.


#Tasks:

1. Manually retrieve 10-15 random video URLs from YouTube.
Save the URLs in a text file called video_urls.txt , where each URL should be stored on a
separate line.
Consider YouTube videos that are 2-3 minutes in duration.

ANSWER:
The file video_urls.txt contains the urls of bbc news videos on youtube.


2. Develop a Python script to read the URLs.
Assuming you have the text file named video_urls.txt containing the URLs of YouTube videos,
load it in Python and extract the URLs using your preferred data structure.

ANSWER:
The file video_download.py contains the function read_video_urls which reads the urls from video_urls.txt and retruns a list of urls.


3. Develop a Python script to download the videos using their URLs.
Test your solution by downloading the files serially.
Use parallel programming such as multiprocessing or threading to handle downloads. Your
decision will determine the best strategy.
For testing reasons, ensure the script can download up to 5 videos simultaneously to avoid
YouTube blocks.
You are advised to use threads and semaphores to control the downloads.
Compare serial and parallel executions for your video download script.
Discuss the complexity of your video download scripts' time and space.

ANSWER:
The file video_download.py contains the function download_video which is implemented using semaphores so that multithreading can be used to speed-up the process.

The file video_download_compare.py runs the video download process using serial execution and parallel execution using multithreading.
Serial execution takes 44 seconds.
Parallel execution - multithreading takes 16 seconds.
The parallel execution is around 2.5 times faster than the serial execution.
(times above will vary)

The time complexity of the `video_download.py` script is influenced by reading URLs, downloading videos, and logging activities.
Reading URLs:
Time complexity of O(N) where N is the number of lines in the file.
Space complexity of O(N * L) where L is the average lenght of each URL. 
Downloading videos:
Time complexity of O(N) where N is the number of videos.
Space complexity of O(N * S) where S is the average size of a file.
Thread management:
Space complexity is O(M) where M is the number of concurrent threads.
Logging:
Time complexity is O(N) where N is the number of videos.
Space complexity is O(N * T) where T is the average size of a log entry.
Combined time complexity is O(N * l) where N is the number of videos and l is the average download time for a video.
Combined space complexity is  O(N + N * S) where N is the number of videos and S the average size of a video.


4. Develop a Python script to keep a log for each download.
After downloading each video, create a logger to record which video was downloaded by which
process or thread.
Save the log entries to the same file, e.g., download_log.txt .
For this script, you have to use threads and a mutex .

ANSWER:
The file video_download.py reads the urls from a text file, download each video and create a log file to record which video was downloaded and save it as download_log.txt.
The script leverages threads and a mutex.


5. Develop Python scripts to perform various video analysis tasks.
After downloading a video, perform the following tasks.
It is preferable to develop a separate script for each functionality.
The five analysis subtasks that you have to develop include the following:
Extract audio from a video file.
Transcribe audio to text.
Perform the sentiment analysis on a video's content, extracting its polarity and sensitivity.
Translate the text into another language, e.g. Spanish.
Extract the emotions of a text.
Each output task should store its results in a dedicated folder designated for each video, using
the video title. Feel free to organise your folder structure as you prefer.
You can use any library, including moviepy for loading video and speech_recognition or
textblob for sentiment analysis.
To implement the analysis subtasks, you must use at least one of the following libraries:
multiprocessing , threading , or asyncio .
You must compare serial, multiprocessing, threading, and concurrency for at least one of the
subtasks, such as the extracting audio functionality. You do not have to do it for the rest of the
subtasks.

ANSWER:
The file extract_audio.py extracts audio from videos.
The file transcribe_audio.py transcribes audio into text.
The file sentiment_analysis.py performs the sentiment analysis of the transcribed text.
The file tranlate_text.py translates the text from emglish to spanish.
The file extract_emotions.py extracts emotions from transcribed text.

ALL the files mentioned above use mutliprocessing to speed-up the precssing.
Multiprocessing has been chosen over multithreading because of the CPU intensice nature of each process.

A comparison of serial vs mutliprocessing vs multithreading vs concurrency has been done for the extract_audio feature.
the file extracting_audio_compare.py generates time for serial, mutliprocessing and multithreading executions.
the file extracting_audio_compare2.py generates time for concurrency execution.
serial execution takes 18 seconds.
parallel execution - mutliprocessing takes 6 seconds.
parallel execution - multithreading takes 12 seconds.
concurrency execution takes 20 seconds.
(times above will vary) 


