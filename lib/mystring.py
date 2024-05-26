class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.rstrip('.').endswith('.')

    def is_question(self):
        return self.value.rstrip('?').endswith('?')

    def is_exclamation(self):
        return self.value.rstrip('!').endswith('!')

    def count_sentences(self):
        sentences = self.value.replace('?', '.').replace('!', '.').split('.')
        return len([s for s in sentences if s.strip()])