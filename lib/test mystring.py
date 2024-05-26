from .string_utils import count_sentences

class MyString:
    def __init__(self, value):
        self.value = value

    def count_sentences(self):
        return count_sentences(self.value)