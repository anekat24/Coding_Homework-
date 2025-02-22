def e_approx(n):
    approx = 1.0
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        approx += 1 / factorial

    return approx
