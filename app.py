from fastapi import FastAPI, File, UploadFile
import os
import fitz  # PyMuPDF for PDFs
from docx import Document
from dotenv import load_dotenv
from google import genai

print("The script has started...")
print(f"PyMuPDF version: {fitz.__version__}")

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the API key is loaded
if not GEMINI_API_KEY:
    raise ValueError("⚠️ GEMINI_API_KEY is not set in the .env file")

# Initialize Gemini API Client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file using PyMuPDF."""
    try:
        doc = fitz.open(file_path)
        text = "\n".join([page.get_text("text") for page in doc])
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

def extract_text_from_docx(file_path):
    """Extract text from a DOCX file using python-docx."""
    try:
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        return f"Error extracting text from DOCX: {str(e)}"

@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        
        # Extract text based on file type
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file.filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        elif file.filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            return {"error": "Unsupported file format"}
        
        os.remove(file_path)  # Clean up the temp file

        # Send text to Gemini for summarization
        model = "gemini-2.0-flash" 
        response = model.generate_content(
            "Summarize and extract key points from this document:\n{text}"
        )

        return {"summary": response.text if response else "No summary generated"}

    except Exception as e:
        return {"error": str(e)}

print("🚀 Script is running on http://127.0.0.1:8000")
