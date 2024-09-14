list = [1,2,3,4,5,2,4,5]
uniqueList = []


for element in list:
    if(element not in uniqueList ):
        uniqueList.append(element)
        
print(uniqueList)


user = {
    "name":"adam",
    "job":"student",
    2:"ddd",
    {"f":""}:"f"
}

for key,value in user.items():
    print(f"user[\"{key}\"] = \"{value}\"")