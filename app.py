from fastapi import FastAPI, File, UploadFile
import whisper
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download additional resources required by nltk and spaCy
nltk.download('vader_lexicon')
spacy.cli.download("en_core_web_sm")

# Initialize FastAPI app
app = FastAPI()

# Load Whisper model for speech-to-text conversion
model = whisper.load_model("base")

# Load spaCy NLP model and NLTK's VADER sentiment analyzer
nlp = spacy.load("en_core_web_sm")
sid = SentimentIntensityAnalyzer()

@app.post("/analyze_support_call/")
async def analyze_support_call(audio_file: UploadFile = File(...)):
    # Read the audio file content
    audio = await audio_file.read()
    
    # Transcribe the audio to text using Whisper
    transcription = model.transcribe(audio)
    text = transcription["text"]

    # Perform NLP analysis using spaCy to extract keywords/entities
    doc = nlp(text)
    keywords = [ent.text for ent in doc.ents]

    # Analyze the sentiment of the text using VADER
    sentiment = sid.polarity_scores(text)

    # Return the transcription, sentiment analysis, and extracted keywords
    return {
        "transcribed_text": text,
        "sentiment": sentiment,
        "keywords": keywords
    }

@app.get("/")
async def root():
    return {"message": "Welcome to the Support Call Analysis API"}
