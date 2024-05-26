import pytest
from conftest import MyString

@pytest.fixture
def mystring():
    return MyString()

def test_is_sentence(mystring):
    mystring.value = "This is a sentence."
    assert mystring.is_sentence()
    mystring.value = "This is not a sentence"
    assert not mystring.is_sentence()

def test_is_question(mystring):
    mystring.value = "Is this a question?"
    assert mystring.is_question()
    mystring.value = "This is not a question."
    assert not mystring.is_question()

def test_is_exclamation(mystring):
    mystring.value = "This is an exclamation!"
    assert mystring.is_exclamation()
    mystring.value = "This is not an exclamation."
    assert not mystring.is_exclamation()

def test_count_sentences(mystring):
    mystring.value = "This is a sentence. It has two sentences."
    assert mystring.count_sentences() == 2
    mystring.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
    assert mystring.count_sentences() == 3
    mystring.value = ""
    assert mystring.count_sentences() == 0