# 📚 Smart Text App

A Flask-based web application that provides text summarization and dictionary lookup features with text-to-speech capabilities.

## ✨ Features

### 📝 Text Summarizer
- Extracts key sentences from long text using frequency-based algorithm
- Uses NLTK for natural language processing
- Provides audio playback of summaries using Web Speech API

### 📘 Dictionary
- Word definitions powered by WordNet
- Synonyms and antonyms lookup
- Example sentences for context
- Hindi translation of meanings using Google Translate
- Search history tracking (last 5 words)
- Text-to-speech for all definitions

## 🛠️ Technologies Used

- **Flask** - Web framework
- **NLTK** - Natural Language Toolkit for text processing
- **WordNet** - Lexical database for dictionary features
- **Google Translate API** - For Hindi translations
- **Web Speech API** - For text-to-speech functionality

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone or download this repository**

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Download NLTK data (one-time setup):**
   
   **Option A - Global installation (recommended):**
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
   ```
   This downloads data to your system globally and can be used by any Python project.
   
   **Option B - Local installation (project-specific):**
   ```bash
   python -c "import nltk; nltk.download('punkt', download_dir='./nltk_data'); nltk.download('stopwords', download_dir='./nltk_data'); nltk.download('wordnet', download_dir='./nltk_data')"
   ```
   This downloads data to the `nltk_data/` folder in your project directory only.
   
   > **Note:** The app code doesn't include download commands - it expects the data to be pre-downloaded using one of the above methods.

## 💻 Usage

1. **Activate your virtual environment (if using one):**
   ```bash
   venv\Scripts\activate
   ```

2. **Start the Flask application:**
   ```bash
   python app.py
   ```

3. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

4. **Use the features:**
   - **Text Summarizer**: Paste your text and click "Summarize"
   - **Dictionary**: Enter a word and click "Search"
   - **Audio**: Click the 🔊 button to hear any text

## 📁 Project Structure

```
Summarize Topic/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── venv/                 # Virtual environment (if created)
│
├── static/
│   └── style.css         # CSS styling
│
├── templates/
│   └── index.html        # Main HTML template
│
└── nltk_data/            # NLTK data files (if downloaded locally)
```

> **Note:** The `nltk_data/` folder only exists if you choose local NLTK data installation. For global installation, data is stored in your Python's system directory.

## 🔧 How It Works

### Text Summarization
1. Tokenizes input text into words and sentences
2. Removes stopwords and punctuation
3. Calculates word frequency
4. Scores sentences based on word frequency
5. Returns top 3 highest-scoring sentences

### Dictionary Lookup
1. Queries WordNet for word definitions
2. Extracts synonyms and antonyms from lemmas
3. Retrieves example sentences
4. Translates first meaning to Hindi using Google Translate
5. Stores word in search history

## 🎨 Features in Detail

- **Real-time Processing**: Instant summarization and dictionary lookup
- **Audio Output**: Browser-based text-to-speech for accessibility
- **Search History**: Keeps track of last 5 searched words
- **Multi-language Support**: Hindi translation for word meanings
- **Responsive UI**: Clean and intuitive interface

## 📦 Dependencies

```
flask
nltk
pyttsx3
googletrans==4.0.0-rc1
```

## 🐛 Troubleshooting

**Virtual Environment:**
- Always activate your venv before running the app: `venv\Scripts\activate` (Windows)
- To deactivate: `deactivate`

**NLTK Data Error:**
If you get "Resource not found" errors, download NLTK data:

**Global installation:**
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

**Local installation (to project folder):**
```bash
python -c "import nltk; nltk.download('punkt', download_dir='./nltk_data'); nltk.download('stopwords', download_dir='./nltk_data'); nltk.download('wordnet', download_dir='./nltk_data')"
```

- Global: One-time setup, accessible by all Python projects
- Local: Data stored in your project's `nltk_data/` folder only
- The application code doesn't download data automatically - you must do it manually first

**Google Translate API Error:**
Make sure you're using the correct version (`googletrans==4.0.0-rc1`)

**Speech Synthesis Not Working:**
Ensure you're using a modern browser that supports the Web Speech API (Chrome, Edge, Safari)

---

**Note:** This application runs in debug mode by default. For production deployment, set `debug=False` in [app.py](app.py#L91).
