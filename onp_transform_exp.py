test_case = int(input())

for i in range(test_case):
    brackets = []
    operators = []
    variables = []
    exp = input()
    brac = ["(", ")"]
    oper = ["+", "-", "*", "/", "^"]
    new_exp = ""
    for i in exp:
        if i in brac:
            if i == ")":
                new_exp += operators.pop()
                brackets.pop()
            else:
                brackets.append(i)
        elif i in oper:
            operators.append(i)
        else:
            new_exp += i
    print(new_exp)

