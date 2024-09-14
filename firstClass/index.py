list = range(1,101)






for number in list:
    word =""        
    if (number %3 == 0 ):
        word+= "fizz"
    if (number %5 == 0):
        word+="buz"
    print(word + str(number))





