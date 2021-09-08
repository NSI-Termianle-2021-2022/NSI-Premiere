def my_grade(good, bad, bonus):
    pg = good*3
    pb = bonus*3

    a = (pg + pb) - bad
    note = a/2.1
    note = round(note, 1)

    if note>20:
        note = 20

    return print(note)