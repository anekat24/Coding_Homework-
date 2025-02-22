def split_parity(lst):
    i, j = 0, len(lst) - 1

    while i < j:
        while i < len(lst) and lst[i] % 2 != 0:
            i += 1
        while j >= 0 and lst[j] % 2 == 0:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
