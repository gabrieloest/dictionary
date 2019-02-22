import json
import dictionary

data = json.load(open("./data/dictionary.json"))
dictionary = dictionary.Dictionary(data)

word_user = input("Enter a word:")
output = dictionary.search_word(word_user)
dictionary.print_result(output)
