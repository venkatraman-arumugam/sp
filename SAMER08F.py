squares = [i**2 for i in range(101)]
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(squares[:n+1]))