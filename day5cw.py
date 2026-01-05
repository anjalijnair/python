python={"arya","vivek","revathy","amal","ammu"}
data_science={"amalu","venu","revathy","arya","nithin"}
python.add("meenakshi")
print(python)
data_science.remove("venu")
print(data_science)
print("enrolled in both course",python&data_science)
print("only in python couse",python-data_science)
print("combined list of all students",python|data_science)
course_num={
    "python":6,
    "data_science":4
}
print(course_num)
for x,y in course_num.items():
    print("course:",x,",students:",y)
    print("dictionary comprehension")
new_student_course={course:count*2 for course,count in course_num.items()}    
print(new_student_course)






      


      