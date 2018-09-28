
class Student:
    
    def __init__(self, n, a, s=0):
        self.__name = n
        self.__age = a
        self.__score = s

    def __save(self,__file):
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')

    def __get_info(self):
        return(self.__name,self.__age,self.__score)


    def __get_score(self):
        return self.__score

    def __get_age(self):
        return self.__age

    def __set_student(self,name,age,score):
        self.name = name
        if 0<=score<=100:
            self.__score = score
        if 0<=age<=140:
            self.__age = age

    def __set_score(self,score):
        if 0<=score<=100:
            self.__score = score
    def __set_age(self,age):
        if 0 <= age <= 140:
            self.__age = age
    def __set_name(self,name):
        self.__name = name
