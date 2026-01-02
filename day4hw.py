web_development=["rohit","manu","rohini"]
data_science=["asha","aleena","nived"]
ui_ux_design=["nithin","ninav","anitha"]
all_participants=[web_development,data_science,ui_ux_design]
print(all_participants)
web_development.append("geetha")
print(web_development)
data_science.insert(1,"jithin")
print(data_science)
ui_ux_design.pop()
print(ui_ux_design)
new_data_science=data_science.copy()
print(new_data_science)
data_science.clear()
print(web_development[:2])
len_participants=[len(x) for x in new_data_science]
print(len_participants)
if "asha" in web_development or new_data_science or ui_ux_design:
    print("yes,Asha is a participant")
first_tuple=(web_development[0],new_data_science[0],ui_ux_design[0])
print(first_tuple)
