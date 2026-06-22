def employee(id, name, salary):
    print(id, name, salary)

# Positional argument
employee(101,"ns",65000)

# Keyword argument
employee(id=101, name="Nithya", salary=50000)

#Positional+Keyword argument
employee(102,salary=75000,name="Nithyasree") #ALWAYS POSITIONAL THEN ONLY KEYWORD ARGUMENT

