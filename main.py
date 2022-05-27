
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name:str,age:int,tracks:list,score:float):
        self.name:str = name
        self.age:int = age
        self.tracks:list = tracks
        self.score:float = score

    def change_name(self):
        return ("My name is " '{}'.format(self.name))

    def change_age(self):
        return ("My age is " '{}'.format(self.age))

    def add_track(self):
        return ("My track is " '{}'.format(self.tracks))

    def get_score(self):
        return ("The score is " '{}'.format(self.score))

student1 = Student("Bob", 26, "FE", 20)
student2 = Student("Peter", 360, "UI", 30)

print(Student.change_age(student2))



# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
