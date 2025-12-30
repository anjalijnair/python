import random
apple,orange,grape=15.5,20,10.25
total=apple+orange+grape
print("total volume",total)
vol_int=int(total)
print("convert volume to int",vol_int)
print(type(vol_int))
vol_str=str(total)
print(vol_str)
print("convert volume to string",type(vol_str))
print("additional bonus liters")
final_volume=random.randrange(5, 10)+total
print(final_volume)