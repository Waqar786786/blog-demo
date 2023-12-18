from googletrans import Translator

translator = Translator()
txt = 'comment allez vous ?'
output = translator.Translator(txt, dest='en')
print(output.text)