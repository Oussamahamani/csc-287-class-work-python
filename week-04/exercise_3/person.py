class Person:
    def __init__(self,first_name,last_name,social_security_number):
        self._first_name = first_name
        self._last_name = last_name
        self._social_security_number = social_security_number
        
person_1 = Person("bob",'jordan',446464)

person_1._first_name = "adam"
print(person_1._first_name)
print(person_1._last_name)
print(person_1._social_security_number)
