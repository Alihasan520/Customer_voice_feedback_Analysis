# Support Call Analysis API

## Overview

This project is a **Support Call Analysis API** built with FastAPI. It transcribes audio files, extracts keywords using spaCy, and performs sentiment analysis using NLTK's VADER. The API is designed for analyzing customer support calls, providing insights into the content and sentiment of conversations.

## Features

- **Speech-to-Text Conversion**: Uses OpenAI's Whisper model to transcribe audio files.
- **NLP Analysis**: Extracts keywords and entities from the transcribed text using spaCy.
- **Sentiment Analysis**: Evaluates the sentiment of the transcribed text using NLTK's VADER.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or later
- FastAPI
- Uvicorn (for running the FastAPI server)
- Whisper
- spaCy
- NLTK

## Install dependencies
  pip install -r requirements.txt
## Download required models and data:
  ```
  python -m spacy download en_core_web_sm
  python -c "import nltk; nltk.download('vader_lexicon')"
  ```

## Usage:
  1) Use Uvicorn to start the FastAPI server:
    ``` 
    uvicorn main:app --reload
    ```
  2) API Endpoints:

  POST /analyze_support_call/
  
  Upload an audio file to transcribe, extract keywords, and analyze sentiment.
  
  Example request:
    ``` curl -X POST "http://127.0.0.1:8000/analyze_support_call/" -F "audio_file=@path_to_audio_file.wav"
    ```
  3) Sample Response:
      ``` 
          {
        "transcribed_text": "Thank you for calling support. How can I assist you today?",
        "sentiment": {
          "neg": 0.0,
          "neu": 0.8,
          "pos": 0.2,
          "compound": 0.4019
        },
        "keywords": ["support"]
        }```
## Project Structure:
  ```support-call-analysis/
├── main.py              # API implementation
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
```
##Dependencies
  FastAPI
  Uvicorn
  Whisper
  spaCy
  NLTK
  
     

    

  
