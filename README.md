# Text Analysis for Interview Responses

## Overview

Analyze transcribed interview responses using Python libraries `TextBlob` for sentiment analysis and `spaCy` for key phrase extraction.

## Features

- **Sentiment Analysis**: Classifies responses as Positive, Negative, or Neutral.
- **Key Phrase Extraction**: Identifies important noun phrases.
- **Quality Assessment**: Rates response quality based on sentiment and key phrases.

## Installation

1. Install dependencies:
   ```sh
   pip install spacy textblob pandas
   ```
2. Download spaCy model:
   ```sh
   python -m spacy download en_core_web_sm
   ```
3. Download TextBlob corpora:
   ```sh
   python -m textblob.download_corpora
   ```

