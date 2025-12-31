multi_str="""DEVI Bookstore
Thrivandrum
pin:695427"""
book1Name="Python Basics"
book1Price=450
book2Name="Data Science Intro"
book2Price=600
book1=f"Book:{book1Name} Price:{book1Price}"
book2=f"Book:{book2Name} Price:{book2Price}"
print(book1)
print(book2)
total=book1Price+book2Price
total_book=f"total price: {total}"
msg="Thank you..."
finaloutput=multi_str+"\n"+book1+"\t"+book2+"\n"+total_book+"\n"+msg
print(finaloutput)
print(finaloutput.upper())