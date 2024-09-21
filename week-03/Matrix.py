number = input("type a number between 2 and 9: ")
number = int(number)
list=[]
if 2<=number<=9:
    for iteration in range(number):
        nestedList = []
        for num in range(number):
          nestedList.append(0)
        list.append(nestedList)


print(list)
for row in list:
    wholeRow = ""
    for square in row:
        wholeRow+= str(square)+" "
    print(wholeRow)