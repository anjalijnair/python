para="""Python is a high-level, interpreted, and general-purpose programming language 
that emphasizes code readability with its clean,
 concise syntax. 
 Python created by Guido van Rossum in 1991, 
 Python is open-source and supports multiple programming paradigms, 
 including object-oriented, functional, and procedural styles"""
print("Length of the Paragraph")
print(len(para))
print("First letter :",para[0])
print("Last letter :",para[-1])
print("First 50 charecters from the paragraph :")
print(para[0:50])
print("Replace python to PYTHON")
print(para.replace("Python","PYTHON"))
print(para.strip())
print("convert paragraph to lowercase")
print(para.lower())
print("Split to individual words")
print(para.split(" "))
totallen=322
words=50
final_msg=f"The course description is {totallen} characters long and has {words} words"
print(final_msg)
