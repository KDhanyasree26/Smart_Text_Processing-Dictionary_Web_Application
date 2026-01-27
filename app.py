from flask import Flask, render_template, request
import nltk, string
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# ---------------- SUMMARIZER ----------------
def summarize_text(text, n=3):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    freq = {}
    for w in words:
        if w not in stop_words and w not in string.punctuation:
            freq[w] = freq.get(w, 0) + 1

    sentences = sent_tokenize(text)
    scores = {}

    for sent in sentences:
        for w in word_tokenize(sent.lower()):
            if w in freq:
                scores[sent] = scores.get(sent, 0) + freq[w]

    return " ".join(sorted(scores, key=scores.get, reverse=True)[:n])

# ---------------- DICTIONARY ----------------
def dictionary_data(word):
    meanings, synonyms, antonyms, examples = [], set(), set(), []

    synsets = wordnet.synsets(word)
    if not synsets:
        return meanings, [], [], []

    for syn in synsets[:3]:
        meanings.append(syn.definition())

        if syn.examples():
            examples.extend(syn.examples())

        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())

    return meanings, list(synonyms), list(antonyms), examples

history = []

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    meanings, synonyms, antonyms, examples = [], [], [], []
    translation = None

    if request.method == "POST":
        # -------- SUMMARIZER --------
        if "summarize" in request.form:
            summary = summarize_text(request.form["text"])

        # -------- DICTIONARY --------
        if "dictionary" in request.form:
            word = request.form["word"]
            meanings, synonyms, antonyms, examples = dictionary_data(word)

            if meanings:
                translation = translator.translate(meanings[0], dest="hi").text

            if word not in history:
                history.insert(0, word)

    return render_template(
        "index.html",
        summary=summary,
        meanings=meanings,
        synonyms=synonyms,
        antonyms=antonyms,
        examples=examples,
        translation=translation,
        history=history[:5]
    )

if __name__ == "__main__":
    app.run(debug=True)
