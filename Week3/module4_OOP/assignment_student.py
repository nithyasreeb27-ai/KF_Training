class student:
    def __init__(self,maths,phy,chem):
        self.maths=maths
        self.phy=phy
        self.chem=chem
    def average(self):
        return (f"{(self.maths+self.phy+self.chem)/3:.2f}")
def get_input():
    m=int(input("enter maths mark:"))
    p=int(input("enter physics mark:"))
    c=int(input("enter chemistry mark:"))
    return m,p,c
def main():
    maths,phy,chem=get_input()
    s1=student(maths,phy,chem)
    return s1.average()
print(main())