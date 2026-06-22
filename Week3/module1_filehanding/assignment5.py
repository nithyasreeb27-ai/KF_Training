with open("Week3/file.txt","r") as file:
    count_line=0
    for i in file:
        count_line+=1
    print(count_line)

    file.seek(0)
    count_words=0
    wrd=file.readlines()
    print(wrd)
    for i in wrd:
        sp=len(i.split())
        count_words+=sp
    print(count_words)

    file.seek(0)
    count=0
    n=file.read()
    for i in n:
        count+=1
    print(count)