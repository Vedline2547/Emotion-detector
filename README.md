# 😊 Emotion Detector using NLTK and VADER

A simple Natural Language Processing (NLP) project that analyzes text sentiment using **NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner)** and maps the sentiment scores to basic emotions such as **Joy, Sadness, Anger, Neutral, and Mixed Emotion**.

## 📌 Project Overview

This project demonstrates how Natural Language Processing can be used to analyze the emotional tone of written text.

The program takes a piece of text as input and uses the VADER sentiment analyzer to calculate four sentiment scores:

* **Positive (`pos`)**
* **Negative (`neg`)**
* **Neutral (`neu`)**
* **Compound (`compound`)**

The compound score and sentiment values are then passed through a set of rule-based conditions to determine the detected emotion.

## 🧠 How It Works

The project follows this workflow:

```text
Input Text
    ↓
NLTK
    ↓
VADER Sentiment Analyzer
    ↓
Sentiment Scores
    ↓
Rule-Based Classification
    ↓
Detected Emotion
```

For example:

```text
"I am so happy today! Everything is going well."
```

The text receives a strongly positive sentiment score and is classified as:

```text
Detected Emotion: Joy
```

## 🛠️ Technologies Used

* **Python**
* **NLTK**
* **VADER Sentiment Analysis**

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Vedline2547/Emotion-detector.git
```

Navigate to the project directory:

```bash
cd Emotion-detector
```

Install the required library:

```bash
pip install nltk
```

## 📚 Download NLTK Data

The project requires the VADER lexicon. The program automatically downloads it using:

```python
nltk.download("vader_lexicon")
```

## ▶️ Running the Project

Run the Python script:

```bash
python main.py
```

The program will analyze the sample text and display the sentiment scores and detected emotion.

Example output:

```text
Sentiment Scores: {'neg': 0.0, 'neu': 0.25, 'pos': 0.75, 'compound': 0.85}

Detected Emotion: Joy
```

## 📊 Emotion Classification

The current rule-based system uses the following logic:

| Condition       | Detected Emotion |
| --------------- | ---------------- |
| Compound ≥ 0.5  | Joy              |
| Compound ≤ -0.5 | Sadness          |
| Negative ≥ 0.5  | Anger            |
| Neutral ≥ 0.5   | Neutral          |
| Otherwise       | Mixed Emotion    |

## 📁 Project Structure

```text
Emotion-detector/
│
├── main.py
└── README.md
```

## ⚠️ Limitations

This project uses **VADER sentiment analysis**, which is primarily designed for sentiment rather than detailed emotion classification.

Therefore, emotions such as **anger and sadness** are approximated using sentiment scores and simple rules. The system should be viewed as an introductory NLP project rather than a sophisticated emotion-classification model.

## 🚀 Future Improvements

Possible improvements include:

* Use a labeled emotion dataset
* Train a machine learning classification model
* Add more emotion categories
* Create a web interface using Flask
* Allow users to enter text interactively
* Compare different NLP classification algorithms
* Use Transformer models such as BERT for more advanced emotion detection

## 🎯 Learning Objectives

This project helped demonstrate:

* Working with NLTK
* Sentiment analysis
* VADER sentiment scoring
* Basic NLP concepts
* Rule-based classification
* Python functions
* Interpreting sentiment scores

## 👨‍💻 Author

**Vedline Ochieng**

Civil Engineering Student | ML & AI Enthusiast | Python Developer

---

⭐ If you found this project useful, feel free to star the repository!
