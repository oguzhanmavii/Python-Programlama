
import json 
data = '{"firstName":"Oguzhan","lastName":"Mavi","Job":"Computer Engineer","Age":"24"}'

dataTransfer=json.loads(data)

print(dataTransfer["firstName"],"\n"+dataTransfer["lastName"],"\n"+dataTransfer["Job"],"\n"+dataTransfer["Age"])