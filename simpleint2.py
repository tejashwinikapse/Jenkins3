def simInt(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p=int(input("Enter principal amount: "))
    r=int(input("Enter rate of interest: "))    
    t=int(input("Enter time in years: "))
    
    print("Simple Interest is: ", simInt(p, r, t))