def insertion(t : list,i : int):
    """
    In: t une liste de int, float ou str. i est un int
    Out:t une liste de int, float ou str.
    Insertion de t[i] dans t[0...i[
    """
    m = t[i]

    while i > 0 and m <t[i -1]:
        t[i] = t[i-1]
        i -= 1

    t[i] = m
    return t

print(insertion([1, 5, 6, 'lqjf'], 3))