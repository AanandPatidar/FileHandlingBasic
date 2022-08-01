#WAP TO COUNT THE NO. OF BLANK SPACES IN THE FILE 
f = open("ap1.txt","r+")
a = f.read()
print(a)
count = 0
for i in a :
    if i == " ":
        count+=1
print("\n\nTOTAL NO. OF BLANK SPACES : ",count)
f.close()