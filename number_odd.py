#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

var_int = int(1234)

if(var_int > 999):
    while var_int > 0:
        b = var_int %10
        if(b % 2 != 0 ):
            print(b)
        var_int//=10
    
else:
    print("Not a four digit number")
#Print the number of odd digits in the variable "var_int".
