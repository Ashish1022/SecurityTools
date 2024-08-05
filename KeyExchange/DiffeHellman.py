# Ashish Jadhav 25 TEIT

G = int(input("Enter value for public key G: "))
P = int(input("Enter value for public key P: "))

a = int(input("Enter value for private key a selected by user1: "))
b = int(input("Enter value for private key b selected by user2: "))

def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

x = power(G, a, P)
y = power(G, b, P)
ka = power(y, a, P)
kb = power(x, b, P)

print(f'Secret key for Alice is : {ka}')
print(f'Secret key for Bob is : {kb}')