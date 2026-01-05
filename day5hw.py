frontend={"ardra","anjali","anupama","avani","anandhu"}
backend={"anupama","avani","ameena","anjali","deepak"}
print("add a student ",backend.add("ninav"))
print("remove a student",frontend.remove("anandhu"))
print("Enrolled in both courses",frontend&backend)
print("Only in backend not in frontend",backend-frontend)
print("Total no of unique students",len(frontend|backend))
course_dictioary={
    "frontend":4,
    "backend":6
}
for x,y in course_dictioary.items():
    print("course: ",x,"students: ",y)
new_dictionary={course:count for course,count in course_dictioary.items()}
new_dictionary["fullstact"]=course_dictioary["backend"]+course_dictioary["frontend"]
print(new_dictionary)
