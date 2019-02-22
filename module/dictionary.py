import difflib

class Dictionary:

    def __init__(self, data):
        self.data = {k.lower(): v for k, v in data.items()}

    def search_word(self, word):
        if self.is_word_exists(word):
            return self.retrieve_definition(word)

        near_words = self.find_near_words(word)
        if len(near_words) == 0:
            return "The word doesn't exist, please double check it!"

        return self.search_word(self.select_word(near_words))

    def retrieve_definition(self, word):
        return self.data[word.lower()]

    def is_word_exists(self, word):
        if word in self.data:
            return True

        return False

    def find_near_words(self, word):
        return difflib.get_close_matches(word, self.data.keys(), 10, cutoff=0.75)

    def select_word(self, near_words):
        for word in near_words:
            action = input("Did you mean {} instead? [y or n]: ".format(word)).lower()
            if action == "y":
                return word

        return ""

    def print_result(self, definition):
        if type(definition) == list:
            for item in definition:
                print("-",item)
        else:
            print("-", definition)
