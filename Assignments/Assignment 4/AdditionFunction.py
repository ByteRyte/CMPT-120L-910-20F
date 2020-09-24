def total_range_sum(max_num: int):
    total_sum = 0
    for value in range(max_num + 1):
        total_sum += value
    return total_sum

def print_sum_range(max_num: int) -> any:
    final_sum = total_range_sum(max_num)
    print(final_sum)

print_sum_range(10)

