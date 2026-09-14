#Dataypes in python
a=10 # int
print(a)
print(type(a))

"Float type"
b=10.23
print(b)
print (type(b))
print(a+b) # addition of int and float

"Complex number data type"
c=10+3j
d=2+4j
print(c)
print("addition of  c and d",c+d)
print(type(c))

"Boolean data type"

tr= True
fl= False
print (" The true is", tr ," and the false if",fl)
print(type(tr))
print( tr+fl) # True=1 and false =0

#String data type
s1='Rohit'
s2="Shrikant Kamble"
s3='''This type of triple quotes are userd
to print the string values in 
multiple line'''
print(s1)
print(s2)
print (s1+" "+s2)
print (s1+s3)

'''slice means a piece
[ ] operator is called slice operator,which can be used to retrieve parts of String.
In Python Strings follows zero based index.
The index can be either +ve or -ve.
+ve index means forward direction from Left to Right
-ve index means backward direction from Right to Left'''

s4= "Rohit Shrikant Kamble"
print(s4[3])
print(s4[0])
print(s4[5])
#print(s4[58]) IndexError: string index out of range
print(s4[-3])