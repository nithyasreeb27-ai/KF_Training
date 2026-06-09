print("STUDENT CALCULATOR")
name=input("enter name:")
maths,biology,chemistry,physics=map(int,input("enter marks:").split())
total=maths+biology+chemistry+physics
avg=total/4

if(avg>=90):
    grade="A"
elif(avg>=75):
    grade="B"
elif(avg>=50):
    grade="C"
elif(avg>=35):
    grade="D"
elif(avg<35):
    grade="F"

if(maths >= 35 and biology >= 35 and chemistry >= 35 and physics >= 35):
    print("Overall Pass")
else:
    print("fail")

print("Highest mark: ",max(maths,biology, chemistry, physics))
print("Lowest mark: ",min(maths,biology, chemistry, physics))

print("Grade: ",grade)
print(f"total: {total}")
print("average: ",avg)