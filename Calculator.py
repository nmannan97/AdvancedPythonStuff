def mult(x,y):
    return(float(x)*float(y))

print('This is the Basic Calculator')
A = input('Type in first Input : ')
op = input('Math operation : ')
B = input('Type in second input : ')

if("*" in op):
    print(mult(A,B)) 