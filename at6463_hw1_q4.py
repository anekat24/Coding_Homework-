def main():
    tenth_power = [10 ** i for i in range(6)]
    another_list = [i * (i + 1) for i in range(10)]
    the_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    return tenth_power, another_list, the_alphabet

main()
