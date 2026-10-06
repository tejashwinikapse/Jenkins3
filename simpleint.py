def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

p = 10000
r = 5
t = 2

result = simple_interest(p, r, t)

if __name__ == "__main__":
    print("Simple Interest:", result)