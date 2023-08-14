"""from googletrans import Translator
from this import s

translator = Translator()

result = translator.translate(s, dest='ru')
print(result.text)"""

"""def count_lines_of_code(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)


file_path = '/Users/maxim/pythonProject1/main.py'

lines_of_code = count_lines_of_code(file_path)
print("Total lines of code:", lines_of_code)"""

#  я чуть  доработал код
from googletrans import Translator

text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    return translated.text


source_language = 'en' #можем взять любой язык
target_language = 'ru' # аналогично любой язык

translated_text = translate_text(text, source_language, target_language)
print(translated_text)


