"""Traditional Logic"""

# import math
# test_case = int(input())
# prime_number = dict()
# for i in range(test_case):
#     strg , edrg = list(map(int, input().split()))
#     for i in range(strg, edrg+1):
#         if prime_number.get(i):
#             print(i)
#         elif i != 1:
#             prime = True
#             for j in range(2, int(math.sqrt(i)+1)):
#                 if j!=1 and i!=j and i%j == 0:
#                     prime = False
#                     break
#             if prime:
#                 prime_number[i] = True
#                 print(i)



"""Sieve of Eratosthenes"""


test_case = int(input())
max_elem = 0
min_elem = 1000000001
ranges = []
for i in range(test_case):
    start, end = list(map(int, input().split()))
    if start < min_elem:
        min_elem = start
    
    if end > max_elem:
        max_elem = end

    ranges.append((start, end))

all_elements = list(range(min_elem, max_elem+1))

prime_numbers = []

for i, j in enumerate(all_elements):
    if all_elements[i] == 1:
        all_elements[i] = 0
    elif all_elements[i] != 0:
        prime_numbers.append(j)
        for k, l in list(enumerate(all_elements))[i+1:]:
            if l%j == 0:
                all_elements[k] = 0

for i in ranges:
    for prime in prime_numbers:
        if prime >= i[0] and prime <= i[1]:
            print(prime)
    print()


# test_case = int(input())
# print()
# for i in range(test_case):
#     start, end = list(map(int, input().split()))

#     all_elements = list(range(start, end+1))

#     for i, j in enumerate(all_elements):
#         if all_elements[i] == 1:
#             all_elements[i] = 0
#         elif all_elements[i] != 0:
#             for k, l in list(enumerate(all_elements))[i+1:]:
#                 if l%j == 0:
#                     all_elements[k] = 0
    
#     for i in all_elements:
#         if i != 0:
#             print(i)

#     print()


