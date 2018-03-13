# TO LEARN:
# - majority vote algorithm
# - remove all adjacent (3.11) - the other algorithm
# - regular expression matching (3.10)

# 3.7. Remove set of characters from a string
def removeCharacter(arr, string):
    chars = set()
    for thing in arr:
        chars.add(thing)
    newString = ""
    for char in string:
        if char not in chars:
            newString += char
    return newString

# 3.8. Checks that number of opening and close parens match.
# assumes all characters are either open or close parens.
def matchingParens(string):
    numOpen, numClose = 0, 0
    for char in string:
        if char == "(":
            numOpen +=1
        else:
            numClose +=1
    return numOpen == numClose

# 3.9. First non-repeating character
def nonRepeating(string):
    once = set()
    morethanonce = set()
    for char in string:
        if char in once:
            morethanonce.add(char)
        once.add(char)
    for char in string:
        if char not in morethanonce:
            return char
    return None

# 3.10. Returns the number of words that have 3 continuous vowels or more.
def threeContinuousVowels(string):
    words = string.split()
    hasThree = 0
    vowels = {"a", "e", "i", "o", "u", "y"}
    for word in words:
        v = 0
        for letter in word:
            if letter in vowels:
                v += 1
                if v >= 3:
                    hasThree += 1
                    break
            else:
                v = 0
# 3.11. Removes adjacent matching characters
def removeAdjacent(string):
    if len(string) == 0:
        return ""
    newString = string[0]
    curChar = string[0]
    for index in range(1, len(string)):
        if string[index] != curChar:
            curChar = string[index]
            newString += curChar
    return newString

def findMajority(arr):
    elemCount = {}
    for elem in arr:
        if elem in elemCount:
            elemCount[elem] += 1
        else:
            elemCount[elem] = 1
    for k in elemCount:
        if elemCount[k] > len(arr)/2:
            return k
    # in case there is no majority element
    return None

# def lightBulb(n):
#     bulbStatus = [False] * 100
#     for person in range(1, n+1):
#         for bulb in range(n-1, 100, n):
#             if bulbStatus[bulb]:
#                 bulbstatus[bulb] = False
#             else:
#                 bulbStatus[bulb] = True

# 3.14. List of integers that overlap in two ranges.
# lol my algorithm is the exact same as the Coderbyte one.
def rangeOverlap(range1, range2):
    overlap = []
    for num in range(range1[0], range1[1] + 1):
        if (num >= range2[0]) and (num <= range2[1]):
            overlap.append(num)
    return overlap

# 3.15. Return mean, median, and mode of an array of numbers as a dictionary.
def meanMedianMode(arr):
    mean = sum(arr)/len(arr)
    sortedArr = sorted(arr)
    # if it's an even number, we return the middle one i guess
    # although you could also avg the two in the middle
    median = sortedArr[len(arr)//2]
    freqs = {}
    for num in arr:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
    # this is cool! learn this!
    # MAX: function that takes an iterable, and optionally a 'key'
    # function whose return value is the value that is actually used to
    # find the maximum
    # LAMBDA: specifies a function within the max function.
    # lambda <args>: <function body>
    # what happens w/ max when there is more than one maximum?
    mode = max(freqs, key = lambda k: freqs[k])
    return {"mean" : mean, "median": median, "mode": mode}

# 3.16. Replace consonants w/ following consonant in alphabet
def encodeConsonant(s):
    # assume it's ok to convert everything to lowercase
    s = s.lower()
    newString = ""
    vowels = {"a", "e", "i", "o", "u", "y", " "}
    for char in s:
        if char in vowels:
            newString += char
        else:
            o = ord(char) - 97
            while True:
                o = (o + 1) % 26
                if chr(o + 97) not in vowels:
                    break
            newString += chr(o + 97)
    return newString

# 3.17. Convert an array of strings into an object

# 3.18. Three sum problem.
# def threeSum(array, n):


# Chaining unary functions (from codewars)
# redo and understand this bc I currently am still reeling.
def chained(f1, f2):
    newFunction = lambda x: f2(f1(x))
    return newFunction

def number2words(n):
    words = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
    8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
    14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
    19:"nineteen", 20: "twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
    70:"seventy", 80:"eighty", 90:"ninety"}

    if n in words:
        return words[n]
    elif n >= 1000:
        r = n % 1000
        if r == 0:
            return number2words(n // 1000) + " thousand"
        else:
            return number2words(n // 1000) + " thousand " + number2words(r)
    elif n >= 100:
        r = n % 100
        if r == 0:
            return words[(n // 100)] + " hundred"
        else:
            return words[(n // 100)] + " hundred " + number2words(r)
    elif n >= 20:
        r = n % 10
        # case where the n is evenly divisible by 10 is covered by the first if
        return words[n - r] + "-" + words[r]
    else:
        return " WHOOPS "

# returns two numbers m and k such that m^k = n
def isPP(n):
    from math import sqrt, log, floor
    for i in range(2, floor(sqrt(n)) + 1):
        l = round(log(n) / log(i), 8)
        if l.is_integer():
            return [i, int(l)]
    return None

def check_divisors(divisor_array,  low,  high):
    for i in range(low, high + 1):
        allMatch = True
        oneMatch = False
        for divisor in divisor_array:
            if i % divisor == 0:
                oneMatch = True
            else:
                allMatch = False
        if allMatch:
            print(str(i) + " all_match")
        elif oneMatch:
            print(str(i) + " one_match")
        else:
            print(str(i))

def clock_angles(hour,  minute):
    minAngle = 6 * minute
    hourAngle = 30 * hour + minute / 2
    angle = abs(hourAngle - minAngle)
    if angle > 180: angle = 360 - angle
    return angle

def code(s):
    print(str(len(s)))
    import math
    n = math.ceil(math.sqrt(len(s)))
    for i in range(n**2 - len(s)):
        s += chr(11)
    newS = ""
    for col in range(n):
        # print("COL: " + str(col))
        for row in range(n-1, -1, -1):
            # print("ROW: " + str(row))
            newS += s[row*n + col]
        if row != 0: newS += "\n"
    return newS

# given a multidimensional nested array arr, return the flattened version of the
# array.
def flattenArray(arr, flattened):
    for item in arr:
        if not(isinstance(item, list)):
            flattened.append(item)
        else:
            flattenArray(item, flattened)
    return flattened

def flattenArrayToo(arr):
    flattened = []
    for item in arr:
        if not(isinstance(item, list)):
            flattened.append(item)
        else:
            for thing in flattenArrayToo(item):
                flattened.append(thing)
    return flattened

def flattenArrayTooToo(arr):
    flattened = []
    for item in arr:
        if not(isinstance(item, list)):
            flattened.append(item)
        else:
            flattened = flattened + flattenArrayTooToo(item)
    return flattened

# from CodeWars
def getAllPrimeFactors(n):
    if not(isinstance(n, int)) or n < 1:
        return []
    if n == 1:
        return [1]
    factors = []
    f = 2
    while n > 1:
        if n % f == 0:
            factors.append(f)
            n = n / f
        else:
            f += 1
    return factors

def getUniquePrimeFactorsWithCount(n):
    if not(isinstance(n, int)) or n < 1:
        return [[],[]]
    if n == 1:
        return [[1], [1]]
    unique, count = [], []
    f = 2
    while n > 1:
        if n % f == 0 and not(f in unique):
            unique.append(f)
            count.append(1)
            n = n / f
        elif n % f == 0 and f in unique:
            count[-1] += 1
            n = n / f
        else:
            f += 1
    return [unique, count]

def getUniquePrimeFactorsWithProducts(n):
    if not(isinstance(n, int)) or n < 1:
        return []
    if n < 1:
        return []
    counts = getUniquePrimeFactorsWithCount(n)
    return [f**counts[1][i] for i,f in enumerate(counts[0])]

def insertionSort(arr):
    # divider between sorted and unsorted portions of array
    sortIndex = 1

    while sortIndex < len(arr):
        curItem = arr[sortIndex]
        # default to the last item in case the item we're inserting really is the largest in the sorted section.
        insertIndex = sortIndex
        for i in range(sortIndex):
            if arr[i] > curItem:
                insertIndex = i
                break
        arr = arr[:insertIndex] + [curItem] + arr[insertIndex:sortIndex] + arr[sortIndex+1:]
        sortIndex += 1
    return arr

# uses katsubara algorithm to find the product of two large integers.
from math import log10, floor, ceil
def katsubaraMult(x, y):
    # base case: x and y are 2 digits each.
    if x < 100 and y < 100:
        return x * y
    else:
        # gets number of digits.
        n = len(str(x))
        # calculates 10^n
        raised2 = 10 ** (n // 2)
        raised = 10 ** (n // 2 * 2)
        a = x // raised2
        b = x % raised2
        c = y // raised2
        d = y % raised2
        ac = katsubaraMult(a, c)
        bd = katsubaraMult(b, d)
        abcd = katsubaraMult(a + b, c + d)
        return raised * ac + raised2 * (abcd - ac - bd) + bd

def karatsuba(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if len(x) == 1 or len(y) == 1:
		return str(int(x) * int(y))
	else:
		n = max(len(x), len(y))
		nby2 = n // 2

		a = int(x) // 10**(nby2)
		b = int(x) % 10**(nby2)
		c = int(y) // 10**(nby2)
		d = int(y) % 10**(nby2)

		ac = int(karatsuba(str(a),str(c)))
		bd = int(karatsuba(str(b),str(d)))
		ad_plus_bc = int(karatsuba(str(a+b),str(c+d))) - ac - bd

    	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = int(ac * 10**(2*nby2)) + int(ad_plus_bc * 10**nby2) + int(bd)

		return str(prod)

def karatsubaInt(x,y):
	if len(str(x)) == 1 and len(str(y)) == 1:
		return x * y
	else:
		n = max(len(str(x)), len(str(y)))
		nby2 = n // 2

		a = x // 10**(nby2)
		b = x % 10**(nby2)
		c = y // 10**(nby2)
		d = y % 10**(nby2)

		ac = karatsubaInt(a,c)
		bd = karatsubaInt(b,d)
		ad_plus_bc = karatsubaInt(a+b,c+d) - ac - bd

    	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod

# Merge sort main function.
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))

# Merge helper that merges already-sorted sub-arrays.
def merge(first, second):
    merged = []
    # while at least one of these aren't empty. Yay for falsey values in Python!
    while first or second:
        if first and ((not second) or (second and first[0] < second[0])):
            merged.append(first[0])
            first = first[1:]
        # in all other cases: this helps take care of duplicate items as well.
        else:
            merged.append(second[0])
            second = second[1:]
    return merged

# Inversion count main function.
def invCount(arr):
    if len(arr) < 2:
        return [arr, 0]
    mid = len(arr) // 2
    first, leftInv = invCount(arr[:mid])
    second, rightInv = invCount(arr[mid:])
    both, splitInv = invCountMerge(first, second)
    return [both, leftInv + rightInv + splitInv]

# Merge helper that merges already-sorted sub-arrays.
def invCountMerge(first, second):
    merged = []
    inversions = 0
    # while at least one of these aren't empty.
    while first or second:
        if first and second:
            if first[0] <= second[0]:
                merged.append(first[0])
                first = first[1:]
            else:
                # if item in second list comes before first.
                merged.append(second[0])
                second = second[1:]
                inversions += len(first)
        # only first contains more items.
        elif first:
            merged.append(first[0])
            first = first[1:]
        # only second contains more items.
        else:
            merged.append(second[0])
            second = second[1:]
    return [merged, inversions]

if __name__ == "__main__":
    # print(removeCharacter(["a", "b", "c"], "rrrabbbbrrrrrrcrrrrr"))
    # print(str(matchingParens("[[[]]]]")))
    # print(nonRepeating("hello henry"))
    # print(removeAdjacent("aaabbbrrr;;;;;;;f"))
    # print(str(findMajority([5, 5, 5, 6, 7])))
    # print(str(findMajority([5, 5, 6, 7])))
    # print(rangeOverlap([1, 20], [5, 10]))
    # mmm = meanMedianMode([1, 1, 6, 6, 7, 2, 3, 3, 2, 2, 2, 2, 2, 8])
    # for k in mmm:
    #     print (k + ": " + str(mmm[k]))

    # f1 = lambda x: x * 2
    # f2 = lambda y: y ** 2
    # print(str(chained(f1, f2)(2)))
    # print(encodeConsonant("hello world"))
    # print(isPP(125))
    # check_divisors([2, 3], 1, 6)
    # print(str(clock_angles(12, 30)))
    # data1 =  ("What do you remember? When I looked at his streaky glasses, I wanted "
    #      "to leave him. And before that? He stole those cherries for me at midnight. We were walking "
    #      "in the rain and I loved him. And before that? I saw him coming "
    #      "toward me that time at the picnic, edgy, foreign.")
    # # print(code(data1))
    # print(flattenArray([1, [2], [3, [4]], 5, 6], []))
    # print(flattenArrayToo([1, [2], [3, [4]], 5, 6]))
    # print(flattenArrayTooToo([1, [2], [3, [4]], 5, 6]))

    # print(getUniquePrimeFactorsWithCount(100))
    # print(getUniquePrimeFactorsWithCount("n"))
    # print(getUniquePrimeFactorsWithProducts(-4))

    # print(insertionSort([7, 3, 1, 9, 31, 0, 6, 4]))
    # print(katsubaraMult(1234, 5678))
    # print(katsubaraMult(12345678, 12345678))
    # x = "3141592653589793238462643383279502884197169399375105820974944592"
    # y = "2718281828459045235360287471352662497757247093699959574966967627"
    # b = karatsuba(x, y)
    # print(b)
    #
    # x = 3141592653589793238462643383279502884197169399375105820974944592
    # y = 2718281828459045235360287471352662497757247093699959574966967627
    # c = karatsubaInt(x, y)
    # print(str(c))
    # a = katsubaraMult(x, y)
    # print(str(a))
