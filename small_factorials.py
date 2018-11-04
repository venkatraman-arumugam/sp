
factorials = [0] * 101
test_case = int(input())

for i in range(test_case):
    n = int(input())
    factorial = 1
    if factorials[n] != 0:
        print(factorials[n])
    else:
        for i in range(1, n+1):
            factorial *= i
            factorials[i] = factorial
        print(factorial)