def word_count(text):
    lst=st.split()
    freq={}
    count=0
    for item in lst:
        if item in freq:
            freq[item]+=1
        elif item not in freq:
            freq[item]=1
    return freq
st="ai ml ai data ai"
print(word_count(st))