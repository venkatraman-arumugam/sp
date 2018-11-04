

test_case = int(input())
for i in range(test_case):
    n = int(input())
    fives = 5
    total_trailing_zero = 0
    while True:
        trailing_zero = int(n / fives)
        if trailing_zero != 0:
            total_trailing_zero += trailing_zero
            fives *= 5
        else:
            break
    print(total_trailing_zero)