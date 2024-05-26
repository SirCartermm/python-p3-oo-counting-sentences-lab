def count_sentences(text):
    """
    Counts the number of sentences in a given text.

    Args:
        text (str): The input text.

    Returns:
        int: The number of sentences in the text.
    """
    sentences = text.replace('?', '.').replace('!', '.')
    sentences = sentences.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)