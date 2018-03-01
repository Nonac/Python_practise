VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
import re

def checkio(text):
    text = text.upper()
    pattern1 = re.compile(r'(\b([BCDFGHJKLMNPQRSTVWXZ][AEIOUY])+[BCDFGHJKLMNPQRSTVWXZ]{0,1}\b)')
    pattern2 = re.compile(r'(\b([AEIOUY][BCDFGHJKLMNPQRSTVWXZ])+[AEIOUY]{0,1}\b)')
    words1 = pattern1.findall(text)
    words2 = pattern2.findall(text)
    return len(words1)+len(words2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
