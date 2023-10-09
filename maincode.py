# Online translator tool using Python that reads text from a file and converts it into the desired language
# Since we make use of translate module, first run on the terminal: pip install translate
from translate import Translator

try:
    with open('translatortext.txt',mode='r') as my_file:
        read_text=my_file.read()
except FileNotFoundError:
    print('File not found! Please recheck if file exists.')

 # Translate to Spanish
translator=Translator(to_lang='es') 
translated_text=translator.translate(read_text)

print(f'*****The original text is:*****\n{read_text}')
print(f'*****The translated text is:*****\n{translated_text}')