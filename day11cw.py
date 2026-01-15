from tripdata import trip_details
from datetime import datetime
import json
trips=[trip_details("kerala","12-02-2020","God's own Country"),trip_details("varanasi","17-12-2020","City of temples"),trip_details("agra","21-03-2020","Taj city")]
for trip in trips:
    date_obj=datetime.strptime(trip["visited_date"],"%d-%m-%Y").date()
    trip["visited_date"]=date_obj.strftime("%B %d,%Y")
    json_data=json.dumps(trips,indent=4)
    print(json_data)