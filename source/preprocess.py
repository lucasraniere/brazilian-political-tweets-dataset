import re
import string
from nltk.corpus import stopwords

def remove_spaces(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def remove_mentions(text):
    return re.sub(r'@\w+', '', text).strip()


def remove_hashtags(text):
    return re.sub(r'#\w+', '', text).strip()


def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)


def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emojis de emoções
        "\U0001F300-\U0001F5FF"  # Símbolos e pictogramas
        "\U0001F680-\U0001F6FF"  # Transporte e mapas
        "\U0001F700-\U0001F77F"  # Símbolos diversos
        "\U0001F780-\U0001F7FF"  # Novos emojis
        "\U0001F800-\U0001F8FF"  # Adicionais
        "\U0001F900-\U0001F9FF"  # Mais emojis de emoções e gestos
        "\U0001FA00-\U0001FA6F"  # Emojis de objetos
        "\U0001FA70-\U0001FAFF"  # Outros emojis recentes
        "\U00002702-\U000027B0"  # Outros símbolos e dingbats
        "\U000024C2-\U0001F251"  # Letras dentro de caixas
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)


def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def remove_stopwords(text):
    stop_words = set(stopwords.words('portuguese'))
    words = text.split()
    return ' '.join([word for word in words if word not in stop_words])


def preprocess_text(text):
    text = text.lower()
    text = remove_mentions(text)
    text = remove_hashtags(text)
    text = remove_urls(text)
    text = remove_emojis(text)
    text = remove_spaces(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    return text
