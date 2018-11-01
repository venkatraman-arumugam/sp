def reverse(value):
    if len(value) == 0:
        value = value + "0"
    return int(value[::-1])


n = input()
for i in range(int(n)):
    first, second = input().split(" ")
    reverse_first = reverse(first)
    reverse_second = reverse(second)
    reversed_sum = str(reverse_first + reverse_second)
    print(int(reversed_sum[::-1]))