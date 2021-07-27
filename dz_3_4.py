def thesaurus_adv(*args):
    res = {}
    for i in sorted(args):
        n, s = i.split()
        val = res.setdefault(s[0], {n[0]: [i]})
        n_val = val.setdefault(n[0], [i])
        if i not in n_val:
            n_val.append(i)
    return res


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", 'Алексей Петров',
                    'Ольга Игнатьева', 'Андрей Серафимов'))
