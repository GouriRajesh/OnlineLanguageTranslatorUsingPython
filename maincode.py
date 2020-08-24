# This is an offline translator tool that reads text from a file and converts it into the desired language
from translate import Translator
try:
    with open('translatortext.txt',mode='r') as my_file:
        read_text=my_file.read()
except FileNotFoundError:
    print('File not found! Please recheck if file exists.')

translator=Translator(to_lang='es')  # Translate to Spanish
translated_text=translator.translate(read_text)
print(f'*****The original text is:*****\n{read_text}')
print(f'*****The translated text is:*****\n{translated_text}')
