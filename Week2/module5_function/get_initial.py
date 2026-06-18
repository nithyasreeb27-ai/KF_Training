# def get_initial(full_name):
#     str=""
#     for i in full_name:
#         lst=list(i)
#         str+=lst[0].upper()
#         str+="."
#     return str
# n=input("enetr full name:").split()
# print(get_initial(n))

a=10
def func(a=[]):
    a.append(1)
    return a
print(func())
print(func())