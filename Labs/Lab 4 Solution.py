#Lab 4
print("Lab 4")
O = "-"*20
#Task 1
print(O+"\nTask 1\n")
three = 0
def fib(n):
    global three
    print('Computing fib('+str(n)+')'+'\n...')
    if n == 3:
        three += 1
    if n < 3:
        print('Leaving fib('+str(n)+') returning '+str(n)+'\n')
        return 1       
    else:   
        ret = fib(n-1) + fib(n-2)
        print('Leaving fib('+str(n)+') returning '+str(ret)+'\n')
        return ret

print('fib(10) = '+str(fib(10)))
print('\nfib(3) is counted "'+str(three)+'" times')

#Task 2
print("\n"+O+"\nTask 2\n")

def nCk(n, k): 
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif n < k:
        return 0   
    else:
        return (fact(n) / (fact(k) * fact(n - k)))
 
def fact(n):
    res = 1     
    for i in range(2, n+1):
        res = res * i
    return res

n = int(input('Enter n: '))
k = int(input('Enter k: '))
ans = str(int(nCk(n,k)))
print(str(n)+'C'+str(k)+' =',ans)

#Task 3
print("\n"+O+"\nTask 3\n")
def check(inp = "A man, a plan, a canal, Panama!"):
    if len(inp) < 2:
        return ('\nThis is a palindrome')
    elif not inp[0].isalpha():
        return check(inp[1:])
    elif not inp[-1].isalpha():
        return check(inp[:-1])
    elif (inp[0].lower() == inp[-1].lower()) and check(inp[1:-1]):
        return ('\nThis is a palindrome')
    else:
        return ('\nThis is not a palindrome')

print(check(input('If nothing is entered, default will be used\nEnter a string of characters to check if palindrome or not: ')))

#Task 4

#There is no function call hence the function f(x) will only be defined as an object.












