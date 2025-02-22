def factors(num):
    small_fac = []
    large_fac = []

    i = 1
    while i * i <= num:
        if num % i == 0:
            small_fac.append(i)
            if i != num // i:
                large_fac.append(num // i)
        i += 1

    for fac in small_fac:
        yield fac
    for fac in reversed(large_fac):
        yield fac
