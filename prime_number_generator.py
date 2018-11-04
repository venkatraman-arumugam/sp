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
import math
def simple_sieve(high):
    all_elements = range(2, high+1)
    dummy_bava = [1] * len(all_elements)
    prime_numbers = []

    for i in range(len(all_elements)):
        if all_elements[i] == 1:
            dummy_bava[i] = 0
        elif dummy_bava[i] != 0:
            prime_numbers.append(all_elements[i])
            for k in range(i+1, len(all_elements)):
                if all_elements[k] % all_elements[i]  == 0:
                    dummy_bava[k] = 0

    return prime_numbers

"""Sieve of Eratosthenes"""


test_case = int(input())

for i in range(test_case):
    start, end = list(map(int, input().split()))
    all_elements = range(start, end+1)
    dummy_bava = ([1] * len(all_elements))
    first_segment = int(math.sqrt(end))
    primes = simple_sieve(first_segment)
    for prime in primes:
        closet_value = int(start/prime) * prime
        for i in range(closet_value, end+1, prime):
            if i != prime and i > start and (i) <= end:
                dummy_bava[i - start] = 0
                
    for index in range(len(all_elements)):
        if dummy_bava[index] != 0 and all_elements[index] != 1:
            print(all_elements[index])
    print()







