def Add(x, y):
    return  x + y

def Subs(x,y):
    return x - y

def Multi(x,y):
    return x*y

def div(x,y):
    return x/y


operation = {
    "+" : Add,
    "-" : Subs,
    "*" : Multi,
    "/" : div
}

x = int(input("Enter the Num 1 : \n"))
y = int(input("Enter the Num 2 : \n"))

for k in operation:
    print(k)

operation_sys = (input("Enter the sysmbol \n")) 

calculation_operation = operation[operation_sys] 

ans = calculation_operation(x,y)

print(f"{x} {operation_sys} {y} = {ans}")
