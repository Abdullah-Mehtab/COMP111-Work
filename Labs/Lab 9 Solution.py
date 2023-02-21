from functools import reduce
# Lab 9
print('\t Lab 9')
# Task 1
O = '=-'*10
print(O+'\n\tTask 1')  
fib = lambda n: reduce(lambda x,i: x+[x[-1]+x[-2]],range(n-2), [0, 1])
print('')
print(fib(7))
# Task 2
print(O+'\n\tTask 2')
fact = lambda x : 1 if x <= 1 else x * fact (x-1)
print('')
print(fact(7))
print(O+'\n\tTask 3')
fib_sq = lambda n: reduce(lambda x,i: x+[x[-1]+x[-2]],range(n-2), [0, 1])
print('')
print(list(map(lambda x: x*x,fib_sq(7))))
print(O+'\n\tTask 4')
columbus = 'checking for vowels'
vow = list(filter(lambda x: x in "aeiou", columbus.lower()))
print('')
print(vow)