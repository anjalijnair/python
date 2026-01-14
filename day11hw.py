from tracker import create_record
from datetime import datetime
import json
records=[create_record("London","amazing museums","11-03-2025"),create_record("Dubai","loved the skyline","21-11-2025"),create_record("Sydney","beautiful beaches","25-09-2024")]
for record in records:
    date_obj=datetime.strptime(record["visit_date"],"%d-%m-%Y")
    record["visit_date"]=date_obj.strftime("%B %d,%Y")
json_data=json.dumps(records,indent=4)
print(json_data)
parsed_data=json.loads(json_data)
print("Travel records")
for record in parsed_data:
    print(f"city:{record['city']},Date:{record['visit_date']},comment:{record['comment']}")