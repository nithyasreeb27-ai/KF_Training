dict={
    "name":"nithya"
}

print("name:",dict["name"])

# PRINT NON EXISTING KEY-- GET
# print(dict["age"])
print("age",dict.get("age"))
print("age with default 0:",dict.get("age",0))

# ADD NEW VALUE
dict["marks"]=98
print("marks:",dict["marks"])

# UPDATING EXISTING VALUE
##1st way
dict["marks"]=100
print("updated marks:", dict["marks"])
##2nd way
dict.update({
    "id":1
})

# ALL KEYS
print(dict.keys())

# ALL VALUES
print(dict.values())

# ALL ITEMS BOTH KEY AND VALUE
print(dict.items())