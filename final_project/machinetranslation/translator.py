'''
importing modules
'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    english to french translation function
    '''
    translator = MyMemoryTranslator(source='english', target='fr-CA')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    '''
    french to english translation function
    '''
    translator = MyMemoryTranslator(source='fr-CA', target='english')
    english_text = translator.translate(french_text)
    return english_text
