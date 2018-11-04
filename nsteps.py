test_case = int(input())

for i in range(test_case):
    x, y = map(int, input().split())
    equation1 = (x - y)
    equation2 = (x-2) - y

    if equation1 == 0 or equation2 == 0:
        if x%2 == 1 or y%2 == 1:
            print((x+y)-1)
        else:
            print(x+y)
    else:
        print("No Number")
        