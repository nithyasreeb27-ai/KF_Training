# one has many marks-- DICT TO LIST

dic={
    "name":"a",
    "marks":[98,99]
}
# print(dic["name"])
# print(dic["marks"])
# print(dic["marks"][0])

# Multiple entries-- LIST TO DICT

mult=[
    {"id":1,"name":"nithya","marks":[100,95,97]},
    {"id":2,"name":"sree","marks":[90,96,98]}
]
print(mult[0])
print(mult[0]["id"])
print(mult[1]["marks"][2])

# Dictionary lookup pattern(find details by one detail)-- DICT TO DICT

lookup={
    101:{"id":1,"name":"nithya","marks":[100,95,97]},
    102:{"id":2,"name":"sree","marks":[90,96,98]}
}
print(lookup[101])
print(lookup[101]["name"])
i=0
for key, value in lookup.items():
    for id, details in value.items():
        if(id=="name"):
            print(id,details)