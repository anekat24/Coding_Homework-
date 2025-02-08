def shift(lst, k, direction="left"):
    k = k % len(lst)
    if direction == "right":
        lst[:] = lst[-k:] + lst[:-k]
    else:
        lst[:] = lst[k:] + lst[:k]
