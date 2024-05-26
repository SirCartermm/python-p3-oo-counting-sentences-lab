from mystring import MyString

def test_my_string():
    my_string = MyString("This is a sentence. It has two sentences. And this is another one!")
    assert my_string.count_sentences() == 3