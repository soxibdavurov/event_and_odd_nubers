#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

var_int = int()
sum_even = 0


while var_int > 0:
    var = var_int % 10
    if(var % 2 != 0 ):
        sum_even+=var
    var_int//=10
print(sum_even)
#Find the sum of the odd digits in the variable "var_int".
