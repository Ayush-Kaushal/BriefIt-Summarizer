# BriefIt-Summarizer

- A web application that summarizes your texts and articles. You can directly paste your article or paste the URL of the article you want to summarize.
- It is a **Django** web app which uses **Hugging Face transformers** to summarize the text. 
- To validate and extract text from url **newspaper3k** library has been used.

## Getting Started
You can run this project on your local machine. To start with, pull the repo to your local machine.

### Installation
1. Open terminal in the folder you want to clone the project and type:

```git clone https://github.com/Ayush-Kaushal/BriefIt-Summarizer.git```
2. Install the project dependencies:
```pip install -r requirements.txt```

### Running the app
- To run this on your local host type :
```python manage.py runsslserver 127.0.0.1:9000```
