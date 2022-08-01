#WAP TO COUNT THE SPECIFIC WORD IN THE TEXT FILE 
f = open("ap1.txt","r+")
a = f.read()
print(a)
c = a.split()
print(c)
count = 0
b = input("ENTER THE WORD YOU WANNA COUNT : ")
for i in c :
    if i == b:
        count+=1
print("\n\nTOTAL NO. OF ENTERED WORD : ",count)
f.close()