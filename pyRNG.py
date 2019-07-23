import random

def main():
    #lst = userInput()
    #test = randomInput(lst)
   # print(test)
    print(dictInput())

def userInput():
    userInput  = [int(x) for x in input().split()]
    return userInput

def randomInput(lst):
    maxrange = max(lst)
    minrange = min(lst)
    length = len(lst)
    randlst = random.sample(lst, length)
    return randlst

def dictInput():
    class_list = dict()
    data = input('Enter name & score separated by ":" ')
    temp = data.split(':')
    class_list[temp[0]] = int(temp[1])
    print(class_list.items()) 
    # Displaying the dictionary
    for key, value in class_list.items():
    	print('Name: {}, Score: {}'.format(key, value))
    
main()
