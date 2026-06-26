# class car:
#     def __init__(self,name,colour,engine_status):
#         self.name=name
#         self.colour=colour
#         self,engine_status=engine_status
#     def start(self):
#         print("Car started")
#     def stop(self):
#         print("Car stopped")
# def get_input():
#     name=(input("Enter Name:"))
#     colour=(input("Enter colour:"))
#     engine_status=(input("Enter engine_status:").lower())
#     return name,colour,engine_status
# def main():
#     name,colour,engine_status=get_input()
#     car1=car(name,colour,engine_status)
#     if engine_status=="on":
#         car1.start()
#     elif(engine_status=="off"):
#         car1.stop()
#     else:
#         print("Invalid entry")
# main()

class car:
    def __init__(self,name,colour,engine_status="off"):
        self.name=name
        self.colour=colour
        self.engine_status=engine_status
    def start(self):
        self.engine_status="on"
        print("Engine status now:",self.engine_status)
        print("Car started")
    def stop(self):
        self.engine_status="off"
        print("Engine status now:",self.engine_status)
        print("Car stopped")

def get_input():
    name=(input("Enter Name:"))
    colour=(input("Enter colour:"))
    return name,colour

def main():
    name,colour=get_input()
    car1=car(name,colour)
    car1.start()
    car1.stop()
main()