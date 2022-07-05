#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

var_int = int(input())
a=var_int//1000
b=var_int%1000//100
c=var_int%100//10
d=var_int%10

if(a%2==0):
    print(a)
if(b%2==0):
    print(b)
if(c%2==0):
    print(c)
if(d%2==0):
    print(d)


#Print the number of even digits in the variable "var_int".
