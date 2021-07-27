def thesaurus(*args):
    res = {}
    for i in sorted(args):
        first_letter = i[0]
        if first_letter in res:
            res[first_letter] += [i]
        else:
            res[first_letter] = [i]

    print(res)


thesaurus("Иван", "Мария", "Петр", "Илья", "Александр")
