import re
import contractions

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Important refinery / industrial words
industrial_terms = {
    "ppe",
    "loto",
    "h2s",
    "scba",
    "msds",
    "fire",
    "gas",
    "valve",
    "pump",
    "compressor",
    "boiler",
    "pipeline",
    "reactor",
    "tank",
    "chemical",
    "explosion",
    "fall",
    "electrical",
    "maintenance",
    "refinery"
}


def clean_text(text):
    """
    Cleans incident text exactly the same way
    as used during model training.
    """

    if text is None:
        return ""

    text = str(text)

    # Expand contractions
    text = contractions.fix(text)

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove Emails
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove HTML
    text = re.sub(r"<.*?>", " ", text)

    # Remove Numbers
    text = re.sub(r"\d+", " ", text)

    # Remove punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()

    cleaned = []

    for word in words:

        if word in industrial_terms:
            cleaned.append(word)

        elif word not in stop_words:
            cleaned.append(
                lemmatizer.lemmatize(word)
            )

    return " ".join(cleaned)