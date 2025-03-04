# AI DOC SUMMARIZER 
This is a FastAPI-based document analyzer that extracts and summarizes text from PDFs, DOCX, and TXT files using Google's Gemini AI.

## Features
- Upload and process PDF, DOCX, and TXT files.
- Extract text using PyMuPDF, python-docx.
- Summarize documents using Google Gemini AI.

### Clone of the repo 

```
 git clone https://github.com/shivamyeshu/AI-Doc-Summarizer
```

### Install dependencies:

```
pip install -r requirements.txt
```


### Set up environment variables:
- Create a .env file based on .env.example
- Add your GEMINI_API_KEY

### Run the server:
```
uvicorn app.main:app --reload
```

### API Usage
- Open FastAPI docs: http://127.0.0.1:8000/docs
- Upload a file using Postman or cURL.

#### A project by shivam yeshu 
-- Happy Coding </>