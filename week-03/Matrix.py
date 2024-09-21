number = input("type a number between 2 and 9: ")
number = int(number)
list=[]
if 2<=number<=9:
    for iteration in range(number):
        nestedList = []
        for num in range(number):
          list.append(0)


print(list)

wholeRow = ""
for index,item in enumerate(list):
        wholeRow+= str(item)+" "
        if (index+1) % number ==0 :
            print(wholeRow)
            wholeRow = ""
