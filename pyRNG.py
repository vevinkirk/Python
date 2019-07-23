import random

def main():
    lst = userInput()
    test = randomInput(lst)
    print(test)
def userInput():
    userInput  = [int(x) for x in input().split()]
    return userInput

def randomInput(lst):
    maxrange = max(lst)
    minrange = min(lst)
    length = len(lst)
    randlst = random.sample(range(maxrange), length)
    return randlst
main()
