def two_sum(srt_lst, target):
    left, right = 0, len(srt_lst) - 1

    while left < right:
        curr_sum = srt_lst[left] + srt_lst[right]

        if curr_sum == target:
            return (left, right)
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return None
