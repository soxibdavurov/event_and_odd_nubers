#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

var_int = int()


if(var_int < 10000):
    while var_int > 0:
        var = var_int % 10
        if(var % 2 == 0 ):
            print(var)
        var_int//=10
    
else:
    print("Not a four digit number")


#Print the number of even digits in the variable "var_int".
