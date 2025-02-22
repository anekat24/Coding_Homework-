def findChange(lst01):
    left, right = 0, len(lst01) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst01[middle] == 1:
            if middle == 0 or lst01[middle - 1] == 0:
                return middle
            else:
                right = middle - 1
        else:
            left = middle + 1

    return -1
