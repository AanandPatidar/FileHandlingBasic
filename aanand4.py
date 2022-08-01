#WAP TO REPLACE "a" FROM FILE TO "#"
f = open("ap1.txt","r+")
a = f.read()
print("ORIGINAL PARAGRAPH :",a)
for i in a :
    if i == "a":
        b = a.replace("a","#")
        print("\nUPDATED PRAGRAPH : ",b)
        break
f.write("\nUPDATED PRAGRAPH : "+b)
#f.write("\n"+b)
f.close()