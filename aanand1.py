#WAP TO FIND THE NO. OF VOWELS AVAILABLE IN THE FILE
g = open("ap1.txt","w")
g.write("Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code.")
g.close()
f = open("ap1.txt","r")
a = f.read()
print(a)
count = 0
for i in a :
    if i == "a" or i == "A"  or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i =="O" or i == "u" or i == "U":
        count+=1
print("\nNO. OF VOWELS IN THE PARAGRAPH :  ",count)
f.close()