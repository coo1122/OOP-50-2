def binary_search(values, num):
    left, right = 0, len(values) - 1

    while left <= right:
        mid = (left + right) // 2
        if values[mid] == num:
            return True
        elif values[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 13))