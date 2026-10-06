def print_1_to_n(n):
    if n > 1:
        print_1_to_n(n - 1)
    print(n, end=' ')

n = int(input())
print_1_to_n(n)

def print_a_to_b(a, b):
    print(a, end=' ')
    if a < b:
        print_a_to_b(a + 1, b)
    elif a > b:
        print_a_to_b(a - 1, b)

a = int(input())
b = int(input())
print_a_to_b(a, b)

def is_power_of_two(n):
    if n == 1:
        return "YES"
    if n <= 0 or n % 2 != 0:
        return "NO"
    return is_power_of_two(n // 2)

n = int(input())
print(is_power_of_two(n))

def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)

n = int(input())
print(sum_of_digits(n))

def print_digits_reverse(n):
    print(n % 10, end=' ')
    if n >= 10:
        print_digits_reverse(n // 10)

n = int(input())
print_digits_reverse(n)

def print_digits_direct(n):
    if n >= 10:
        print_digits_direct(n // 10)
    print(n % 10, end=' ')

n = int(input())
print_digits_direct(n)