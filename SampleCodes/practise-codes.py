a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, "gautam"]
c = []
for i in range(len(b)):
    if len(a) > i:
        c.append(a[i])
        c.append(b[i])
    else:
        c.append(b[i])
print(c)

a = [1, 2, 3, 4, 2, 2, 3]
for i in a:
    # print(a)
    if i == 2:
        a.remove(i)
# print(a)


f = None

for i in range(5):

    with open("data.txt", "w") as f:

        if i > 2:
            break


# print(f'f.closed : {f.closed}')

# a = [int(value) for value in input().split()]
# b = [int(value) for value in input().split()]
# print(a)
# print(b)
# from itertools import product
# result = list(product([a,b]))
# print(result)

# Binary Search
def binary_search(data, search_value):
    start = 0
    end = len(data) - 1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == search_value:
            return True
        elif data[mid] < search_value:
            start = mid + 1
        else:
            end = mid - 1
    return False


arr = [1, 3, 5, 7, 8, 9, 2];
x = 4;


# print(binary_search(arr, x))

def factorial(num):
    result = 1
    if num == 0 or num == 1:
        return 1
    else:
        for i in range(2, num):
            result *= i
        return result


# for i in range(10):
#     print(f'{i} : {factorial(i)}')

def fibonacciSeries(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        nextTerm = n1 + n2
        print(n1, end=' ')
        n1 = n2
        n2 = nextTerm


# fibonacciSeries(20)

def isPrime(num):
    if num >= 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True


allPrimes = []
for i in range(100):
    if isPrime(i):
        allPrimes.append(i)

# print(allPrimes)

# reverse words in sentence expect digits
a = "I am 54 Gautam and 34 student"
a_list = a.split()
rev = ""
for word in a_list:
    if word.isalpha():
        rev += word[::-1] + " "
    else:
        rev += word + " "


# print(rev)


# find all combination of substrings in string

def findSubstrings(string1):
    substring_set = []
    for i in range(len(string1)):
        for j in range(i + 1, len(string1) + 1):
            substring_set.append(string1[i:j])

    return substring_set

# print(findSubstrings("abc"))
