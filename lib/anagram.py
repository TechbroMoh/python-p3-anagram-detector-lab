# lib/anagram.py
class Anagram:
    def __init__(self, word):
        self.word = word

    def is_anagram(self, other_word):
        """Check if the given word is an anagram of the instance's word."""
        return sorted(self.word) == sorted(other_word)

    def match(self, word_list):
        """Return a list of words from word_list that are anagrams of the instance's word."""
        return [word for word in word_list if self.is_anagram(word)]
