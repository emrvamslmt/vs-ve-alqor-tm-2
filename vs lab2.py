import random
def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j],end='    ')
        print()

s=0
n=4
m=4
a=[]
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(10,20))
printList(a)
print()
for i in range(n):
    for j in range(m):
        if i==j:
            a[i][j]=1
        else:
            a[i][j]=0
print("Bas dioqonal elementleri 1,qalanlari 0:")
printList(a)

