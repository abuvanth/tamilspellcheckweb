import os
import traceback
from .bloomfilter import BloomFilter

class TamilwordChecker:

    def __init__(self,unique_word_count, bloomfilter_file_path):
        falsepositive_probability = 0.001
        self.bloom_tamil = BloomFilter(unique_word_count,falsepositive_probability,bloomfilter_file_path)

    def tamil_word_exists(self,word):
        if self.bloom_tamil.check(word):
            return True
        else:
            return False
    

if __name__ == "__main__":
    tamilwordchecker = TamilwordChecker(2392064,"tamil_bloom_filter_all_tamil_words.txt")
    print(tamilwordchecker.tamil_word_exists("மேகம்"))    
    
