# Pattern 1- Reading Global

x = 100

def show():
    print(x)

show()

# Pattern 2- Local Shadows Global

x = 100

def show():
    x = 50
    print(x)

show()
print(x)

# Pattern 3- Read Global + Create Local

x = 100

def show():
    y = x + 1
    print(y)

show()


# Pattern 4- Modify Global Directly

x = 100

def show():
    x = x + 1

# Pattern 5- Using global

x = 100

def show():
    global x
    x += 1

show()

print(x)

# Pattern 6- Parameter vs Global

x = 100

def show(x):
    print(x)

show(50)