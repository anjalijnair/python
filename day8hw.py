class employee:
    def __init__(self, name, role):
        super().__init__()
        self.name=name
        self.role=role
    def display(self):
        print("name :",self.name,"role : ",self.role)
class trainer(employee):
    def __init__(self, name, role, specialization):
        super().__init__(name,role)
        self.specialization=specialization
    def display(self):
        print("Name : ",self.name,"role :",self.role,"specialization :",self.specialization)
class YogaInstructor(employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style=yoga_style
    def display(self):
        print("Name : ",self.name,"role : ",self.role,"yoga style : ",self.yoga_style)
class MuitiTrainer(trainer,YogaInstructor):
    def  __init__(self, name, role, specialization, yoga_style):
        #super().__init__(name, role, specialization,yoga_style)
        employee.__init__(self,name,role)
        self.specialization=specialization
        self.yoga_style=yoga_style
    def display(self):
        print("Name : ",self.name,"role : ",self.role,"specialization : ",self.specialization,"Yoga style : ",self.yoga_style)
ob1=employee("anand","staff")
ob2=trainer("rahul","trainer","weight training")
ob3=YogaInstructor("ammu","yoga ainstructor","hatha yoga")
ob4=MuitiTrainer("madhav","muiti tariner","cardio","vinyasa yoga")
ob1.display()
ob2.display()
ob3.display()
ob4.display()

        


        