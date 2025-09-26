# Note: n MUST be a power of two
# both digits must be a power of two 

# Karatsuba formula psuedocode: 
# x, y
# if n = 1, return x * y
# x split into ab
# y split into cd
# res = (a * 10^n/2 + b)(c * 10^n/2 + d)
# res = (ac) * 10^n + (ad + bc) * 10^(n/2) + bd 
# 
# prod = (a + b)(c + d) = ac + bc + ad + bd
# ad + bc = prod - ac - bd 
#
# res = (ac) * 10^n + (prod-ac-bd) * 10^(n/2) + bd 
def multiply(x,y,n):
    if n == 1:
        return x * y;

    m = n // 2; 

    a = (x // (10**m))
    b = x - a * 10**m
    c = y // (10**m)
    d = y - c * 10**m

    z0 = multiply(a,c,m)
    z1 = multiply(b,d,m)
    z2 = multiply((a + b),(c + d),m)
    z3 = z2 - z0 - z1

    return z0 * (10**n) + z3 * (10**m) + z1

def main():
    res = multiply(24,36,2)
    print("result of 24 * 36: ", res);

    res = multiply(2423,3699,4)
    print("result of 2423 * 3699: ", res);

if __name__ == "__main__":
    main()