def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2
    
def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


calculate_again=True
while(calculate_again==True):
    n1=int(input("Enter your first number : "))
    key=input("Enter any operator '+', '-' , '*','/' : ")
    n2 = int(input("Enter your second number : "))
    dict={}
    dict["+"]=add(n1,n2)
    dict["-"]=sub(n1,n2)
    dict["*"]=mul(n1,n2)
    dict["/"]=div(n1,n2)
    print(dict)

    for op in dict:
        if op==key:
            ans=(dict[op])
    

    print(f" The {key} of {n1} and {n2} is = {ans} ")

    ca=input("Do u want to do any calculatons again type 'y' or 'n' : ")
    if ca=='n':
        calculate_again=False
        
