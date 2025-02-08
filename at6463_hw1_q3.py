def sum_of_the_squares(n):
    total = 0
    for i in range(1, n):
        total += i**2
    return total



def sum_of_the_squares_command(n):
    return sum(i**2 for i in range(1, n))



def sum_of_the_squares_odd(n):
    total = 0
    for i in range(1, n, 2):
        total += i**2
    return total


def sum_of_the_squares_odd_command(n):
    return sum(i**2 for i in range(1, n, 2))
