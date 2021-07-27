from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом", 'слон']
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "летом", "когда-то", "как-то", 'порой']
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", 'липкий', 'терпкий']


def get_jokes(n, f=False):
    """ Функция возвращает "n" случайных шуток, "f" - флаг уникальности шуток"""
    nouns_t, adverbs_t, adjectives_t = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    while n and len(min(nouns_t, adverbs_t, adjectives_t)):
        if f:
            jokes.append(f'{nouns_t.pop(randrange(len(nouns_t)))} {adverbs_t.pop(randrange(len(adverbs_t)))} '
                         f'{adjectives_t.pop(randrange(len(adjectives_t)))}')
        else:
            jokes.append(f'{choice(nouns_t)} {choice(adverbs_t)} {choice(adjectives_t)}')
        n -= 1
    return jokes


print(get_jokes(10, True))
print(get_jokes(8))