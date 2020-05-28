from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SpellCheckSerializer
from .TamilwordChecker import TamilwordChecker
from .TamilSpellingAutoCorrect import TamilSpellingAutoCorrect
from django.conf import  settings
# Create your views here.
import os
os.path.dirname(os.path.abspath(__file__))

class CheckSpell(APIView):
    serializer_class=SpellCheckSerializer
    def post(self, request, format=None):
        word = request.data.get('word')
        tamilwordchecker = TamilwordChecker(2392064, os.path.dirname(os.path.abspath(__file__))+"/tamil_bloom_filter_all_tamil_words.txt")
        if tamilwordchecker.tamil_word_exists(word):
           return Response({"result":"சரி"})
        else:
            spellchecker = TamilSpellingAutoCorrect(os.path.dirname(os.path.abspath(__file__))+"/tamil_bloom_filter_all_tamil_words.txt",
                                                    os.path.dirname(os.path.abspath(__file__))+'/unique_sorted_words_in_words_master.txt')
            return Response({"result":"தவறு","suggetions":spellchecker.tamil_correct_spelling(word)})

