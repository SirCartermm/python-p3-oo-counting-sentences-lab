def count_sentences(self):
    sentences = self.value.replace('?', '.').replace('!', '.')
    sentences = sentences.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)