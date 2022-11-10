def top_3_words(text):
    import re
    from collections import Counter
    text = re.sub(r"[^a-zA-Z0-9']+", ' ', text.replace("''", "").replace('""', ''))
    text = text.lower().split()
    text = [word for word in text if word != "'"]
    text = Counter(text)
    return [word for word, count in text.most_common(3)]