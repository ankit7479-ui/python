hash_table = {}

hash_table["key1"] = "value1"
hash_table["key2"] = "value2"

print(hash_table.get("key"))

#del hash_table["key1"]

for key,value in hash_table.items():
    print(f"{key}:{value}")
    
    
#counter Example
from collections import Counter
    