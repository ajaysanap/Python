
"""
#LESSER OF TWO EVENS: Write a function that returns the lesser of two
#given numbers if both numbers are even, but returns
#the greater if one or both numbers are odd

def even_odd(a,b):
    if a%2 == 0 and b%2 == 0: #if both number is even
        if a < b:             # check smaller   we can use min(a,b) function
            return a            
        return b
    else:                     # we can use max(a,b) in built function
        if a < b:
            return b
        return a


print(even_odd(2,4))
print(even_odd(2,5))



""" 

"""
# ANIMAL CRACKERS: Write a function takes a two-word string and
# returns True if both words begin with same letter

def animal_crackers(a):
    c1 = a[0]
    c2 = a.split(" ")[1][0]
    print(c2)
    if c1.lower() == c2.lower():
        return True
    return False

print(animal_crackers("Levelheaded lqlama"))

"""

"""

# Ques MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or
#   if one of the integers is 20. If not, return False


def makes_twenty (a,b):
    if a == 20 or b == 20 or a+b ==20:  # Or directly use return
        return True                     # return a == 20 or b == 20 or a+b ==20
                                        # above statement has booloean outpur                
    return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

"""


#########   Level One

#   OLD MACDONALD: Write a function that capitalizes the first and fourth
#   letters of a name
"""
## Meathod First (using indexing and slicing)
def old_macdonald(name):
    a = name[0].upper()
    a += name[1:3]
    a += name[3].upper()
    a += name[4:]
    
    return a

print(old_macdonald('macdonald'))

## meathod second (using Capitalized meathod)

def old_macdonald(name):
    a = name[0:3].capitalize()
    a += name[3:].capitalize()

    return a
   
print(old_macdonald('macdonald'))

"""

"""
# MASTER YODA: Given a sentence, return a sentence with the words reversed

# My meathod without join() function
def master_yoda(text):
    t1 = text[::-1]
    t = t1.split()
    r = " "
    for i in t:
        r += i[::-1]
        r+= " "
    return r    

print(master_yoda("I am happy to see you there"))


# Using join() meathod

def master_yoda(text):
    t = text.split()
    t_rev  = t[::-1]
    rev_word = " ".join(t_rev)

    return rev_word

print(master_yoda("hello everyone happy to see you all"))


"""


"""
## ALMOST THERE: Given an integer n, return True if n
## is within 10 of either 100 or 200¶



def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n)<=10)


print(almost_there(90))        
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

        
"""        

"""
###  Level 2

## Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:  #if nums[i:i+2] ==[3,3]:
            return True                      #    return True

    return False    
            

print(has_33([1,2,4,6,43,4,3,3,45]))

"""

"""

## PAPER DOLL: Given a string, return a string where for every character
## in the original there are three characters

def paper_doll(text):
    result = ''

    for i in text:
        result += i + i + i

    return result


print(paper_doll("hello"))


"""


"""
## BLACKJACK: Given three integers between 1 and 11,
## if their sum is less than or equal to 21, return their sum.
## If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
## Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    s = sum([a,b,c])
    if s <= 21:
        return s
    if s <= 31 and 11 in [a,b,c]:
       return s -10
    else:
        return "bust"


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


"""
        
"""

## SUMMER OF '69: Return the sum of the numbers in the array, except ignore
## sections of numbers starting with a 6 and extending to the next 9
## (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(a):
    total = 0
    f = True
    for i in a:
        while f:
            if i != 6:
                total +=i
                break
            else:
                f = False

        while not f:
            if i == 9:
                f = True
            else:
               break      
    return total
    
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))                
print(summer_69([2, 1, 6, 9, 11]))

"""



###### CHALLENGING PROBLEMS¶

## SPY GAME: Write a function that takes in a list of integers and returns True
## if it contains 007 in order


"""
def spy_game(nums):
    s = [0,0,7]
    for i in nums:
        if i == s[0]:
            s.pop(0)
        if s == []:
            break
           
    return s == []

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))



"""


"""

## COUNT PRIMES: Write a function that returns the number of prime numbers
## that exist up to and including a given number


def count_primes(num):

    if num < 2:
        return 0
    li = 1
    for i in range(3,num):
        for j in range(2,i):
               if i % j == 0:
                         break
        else:
            li+=1

    return li


print(count_primes(100))


## Above program using While Loop

def prime_while(num):
    if num < 2:
        return 0 

    li = 1
    i = 3
    while i < num:
        for j in range(3,int(i/2),2):
            if i % j == 0:
                i +=2
                break
        else:
            i+=2
            li+=1

    return li


print(prime_while(100))
    

"""

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply([5,2,3,4,5]))































































        
    







































