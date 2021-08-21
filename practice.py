#if-else statements (conditional statements)

#1
x = 3
if x < 5:
    print('hi')
print('bye')

#2
user_name = input('Please enter name')

print('Nice to meet you', user_name)

ask = input('are you enjoying the course?')

if ask == 'yes':
    print('good')
else:
    print('saddening')
print('Bye')


#FUNCTIONS
 
#1
user = input('do you like food? ')
 
def myFunction():
    if user == 'yes':
        print('yeyy that is amazing')
    elif user == 'no': 
        print("yaaakkky")
    else: 
        print('ohh well')
myFunction()

#2
def secondFunction(firstname, secondname, age):
    print('Hello your name is', firstname , secondname)
    print('You are', age, 'years old.')
    print('Nice to meet you!')

secondFunction("Nolitha", "Magagula", "45")

#3
name = "Princess"

def thirdFunction():
    print('Your name is', name)

thirdFunction()

#4
def fourthFunction(x):
    z = x % 5 
    if(z == 0): 
       print(True)
    else:
        print(False) 
    
fourthFunction(10)


#5
def fifthFunction(a):
    if((a % 3 == 0 or a % 5 == 0) and not (a % 3 == 0 and a % 5 == 0)): 
        print(True)
    else:
        print(False)

fifthFunction(30)

#6
def largernum(x, y):
    if(x > y): 
        print(x)
    else:
        print(y)

largernum(10, 21)

#LOOPS
    #for loops
numbers = [2, 4, 6, 11]
zq = []
for i in numbers:
    sq =  0
    sq = i * i
    zq.append(sq)
print(zq)


sum = 0
for value in range(1, 6):
    sum = sum + value
    print(sum) 


# Counting the 'e' in a word
def count(word):
    counter = 0
    for i in word:
        x = 'e'
        if(i == x):
            counter = counter + 1
    print(counter)

count('second')