words = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(word):
    if word.istitle():
        i = words.get(word.lower())
        print(i.title())
    else:
        print(words.get(word))


num_translate_adv('One')
num_translate_adv('one')
num_translate_adv('eight')
num_translate_adv('123')
