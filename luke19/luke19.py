import time

starttime = time.time()

def isHiddenPalindrome(number):
    if (str(number) != str(number)[::-1]): #Hiddenpalindromes can´t be palindromes?
        nSum = int(str(number)) + int(str(number)[::-1])
        return str(nSum) == str(nSum)[::-1]
    return False

assert (isHiddenPalindrome(38) == True)
assert (isHiddenPalindrome(49) == False)

sumPalindrom = 0

for i in range(1,123454321):
    if (isHiddenPalindrome(i)):
        sumPalindrom += i
        if (i % 100000 == 0): #Skriv bare ut hver 100.000 tall
            print("Found hidden palindrom: ", i)

print("Sum of hidden palindromes is: ", sumPalindrom)
print("Run time: ", time.time() - starttime)