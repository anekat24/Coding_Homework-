def findChange(lst01):
    left, right = 0, len(lst01) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst01[middle] == 1:
            if middle == 0 or lst01[middle - 1] == 0:
                return middle
            else:
                right = mid - 1
        else:
            left = mid + 1

    return -1
