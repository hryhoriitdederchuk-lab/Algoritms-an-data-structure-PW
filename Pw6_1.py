def nearest_smaller(arr):
    stack = []
    result = []
    for x in arr:
        while stack and stack[-1] >= x:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(x)
    return result


if __name__ == "__main__":
    data = [4, 5, 2, 10, 8]
    print("Вхідний масив:", data)
    print("Результат:   ", nearest_smaller(data))