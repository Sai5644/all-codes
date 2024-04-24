#1. Write a python program to accept a string and print alternate characters startfrom first character
 
#solution
word = input()
n = len(word)
    # n = 8
    # 0 1 2 3 4 5 
for index in range(0, n, 2):
    print(word[index], end = " ")
 
