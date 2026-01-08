class person:
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.age=age
    def show_details(self):
        print("name : ",self.name,"age : ",self.age)
class employee(person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    def show_details(self):
       print("name : ",self.name,"age :",self.age,"employee_id : ",self.employee_id)
class parttime(person):
    def __init__(self,name,age,working_hours):
        super().__init__(name,age)
        self.working_hours=working_hours
    def show_details(self):
        print("Name : ",self.name,"Age : ",self.age,"working hrs : ",self.working_hours)
class consultant(employee,parttime):
    def __init__(self,name,age,employee_id,working_hours,project_name):
        person.__init__(self,name,age)
        self.employee_id=employee_id
        self.working_hours=working_hours
        self.project_name=project_name
    def show_details(self):
        print("Name : ",self.name,"Age : ",self.age,"employee_id : ",self.employee_id,"working hrs : ",self.working_hours,"project name : ",self.project_name)

ob1=person("anupama",27)
ob2=employee("karthila",26,"A001")
ob3=parttime("devid",30,12.4)
ob4=consultant("avani",25,"A004",10.5,"Antiforensic")
ob1.show_details()
ob2.show_details()
ob3.show_details()
ob4.show_details()
   
    