#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

var_int = 1234
a=var_int//1000
b=var_int%1000//100
c=var_int%100//10
d=var_int%10

print(a%2==0, b%2==0, c%2==0, d%2==0)


#Print the number of even digits in the variable "var_int".
