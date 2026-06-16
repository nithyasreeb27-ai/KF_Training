"""Ask how many students, take name and marks for Math, Science, English for each student, then calculate total, average and grade (A for 90+, B for 80+, C for 70+, D for 60+, F below 60), and mark result as Fail if any subject is below 35 otherwise Pass.
Print the following items too,
Option 1 : Get Student name and print his person info :
Name
Total
Average
Grade
Result
Option 2 :  Overall info:
Top Scorer
Class Average
Number of Passes
Number of Fails
Highest Subject Mark
Lowest Subject Mark"""

n=int(input("enter:"))
names=[]
maths_all=[]
science_all=[]
english_all=[]
overall_total=[]
avg_all=[]
grade_all=[]
result_all=[]
pass_num=0
fail_num=0

for i in range(n):
    name=input("enter name:")
    names.append(name)
    math,science,english=map(int,input("enter marks:").split())
    maths_all.append(math)
    science_all.append(science)
    english_all.append(english)
    total=math+science+english
    overall_total.append(total)
    avg=total/3
    avg_all.append(avg)
    
    if(avg>=90 and math>=35 and science>=35 and english>=35):
        grade="A"
        result="pass"
    elif(avg>=80 and math>=35 and science>=35 and english>=35):
        grade="B"
        result="pass"
    elif(avg>=70 and math>=35 and science>=35 and english>=35):
        grade="C"
        result="pass"
    elif(avg>=60 and math>=35 and science>=35 and english>=35):
        grade="D"
        result="pass"
    elif(avg<60 and avg>=35 and math>=35 and science>=35 and english>=35):
        grade="F"
        result="pass"
    elif(avg<35 or math<35 or science<35 or english<35):
        grade="fail"
        result="fail"
    if(result=="pass"):
        pass_num+=1
    if(result=="fail"):
        fail_num+=1
    grade_all.append(grade)
    result_all.append(result)

print("""option1: Person info:
option2: overall info:""")
c=int(input("enter choice:\n"))

if(c==1):
    new_name=input("enter the name:")
    if new_name in names:
        idx=names.index(new_name)
        print("name:",names[idx])
        print("Total mark:",overall_total[idx])
        print(f"Average mark: {avg_all[idx]:.2f}")
        print("Grade:",grade_all[idx])
        print("Result",result_all[idx])
    else:
        print("invalid entry")

if(c==2):
    top_index=overall_total.index(max(overall_total))
    print("Top scorer:",names[top_index], "and their score is ",overall_total[top_index])
    print("Class average is", round(sum(avg_all)/n,2))
    print("Number of passes:",pass_num)
    print("Number of fail:",fail_num)
    print(f"highest Subject mark: maths:{max(maths_all)},science: {max(science_all)},english: {max(english_all)}")
    print(f"Lowest Subject mark: maths:{min(maths_all)},science: {min(science_all)},english: {min(english_all)}")