from .TamilwordChecker import TamilwordChecker
import os
import jellyfish
import traceback

class TamilSpellingAutoCorrect:

    def __init__(self,bloom_file_path,tamil_unique_word_list_file_path):

        self.edit_distance = 2
        self.tamil_unique_word_list_file_path = tamil_unique_word_list_file_path
        self.read_tamil_words_list_file()
        self.tamilwordchecker = TamilwordChecker(self.unique_word_count,bloom_file_path)

    
    def read_tamil_words_list_file(self):
        self.ta_words_unique = []
        self.unique_word_count = 0
        try:
            tamil_word_file = open(self.tamil_unique_word_list_file_path, 'r') 
            for line in tamil_word_file: 
                self.ta_words_unique.append(line.strip())
                self.unique_word_count = self.unique_word_count + 1
            tamil_word_file.close()    
        except Exception as e:
            track = traceback.format_exc()
            print(track)

    def tamil_correct_spelling(self,word):
        suggested_words = []
        try:
            if not self.tamilwordchecker.tamil_word_exists(word):
                for tamil_word in self.ta_words_unique:
                    if jellyfish.levenshtein_distance(tamil_word,word) < self.edit_distance:
                        suggested_words.append(tamil_word)
        except Exception as e:
            track = traceback.format_exc()
            print(track)
        return suggested_words


if __name__ == "__main__":
    
    spellchecker  = TamilSpellingAutoCorrect("tamil_bloom_filter_all_tamil_words.txt",'unique_sorted_words_in_words_master.txt')
    print(spellchecker.tamil_correct_spelling("வன்ம்"))





    