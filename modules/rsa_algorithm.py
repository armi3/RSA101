import random

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, x):
        if x % i == 0:
            return False
    return True

def GCD(a, b):
    if b>a:
        while a != 0:
            b,a = a,b % a
        return b
    
    while b != 0:
        a,b = b,a % b
    return a

def multiplicative_inverse(a, mod):
    a0, mod0 = a, mod
    x=lasty=0
    y=lastx=1
    while (mod!=0):
        q = a/mod
        a, mod = mod, a%mod
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y
    if lastx<0:
        lastx = mod0+lastx
    return lastx

def binary_exponentiation(base, power, n):
    result = 1
    while power > 0:
        # If power is even
        if power % 2 == 0:
            # Divide the power by 2
            power = power / 2
            # Multiply base to itself
            base = base * base
        else:
            # Decrement the power by 1 and make it even
            power = power - 1
            # Take care of the extra value that we took out
            # We will store it directly in result
            result = result * base

            # Now power is even, so we can follow our previous procedure
            power = power / 2
            base = base * base
    return result%n

def modulus(p, q):
    # n is the modulus for the public and private keys
    n = p * q
    return n

def totient(p, q):
    # Check p and q are prime
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal.')

    # phi(n) is the totient of the modulus n
    phi = (p-1) * (q-1)
    return phi

def public_key_exponent(phi):
    # Condition 1: 1 < e < phi(n)
    e = random.randrange(1, phi)

    # Contidion 2: e and phi(n) must be coprime
    g = GCD(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = GCD(e, phi) 
    return e

def private_key_exponent(phi, e):
    # Satisfy the congruence relation e*d=1 mod(phi(n))
    d = multiplicative_inverse(e, phi)
    return d

def public_key(p,q):
    # (e, n)
    e = public_key_exponent(totient(p,q))
    n = modulus(p,q)
    return (e,n)

def private_key(p, q, pub):
    # (d, n)
    e, n = pub
    d = private_key_exponent(totient(p,q), e)
    n = modulus(p,q)
    return (d,n)

def keypair(p, q):
    pub = public_key(p,q)
    priv = private_key(p,q, pub)
    return pub, priv

def encrypt(public_key, message):
    # Unpack the key into it's components
    e, n = public_key
    # Apply exponentiation to each ascii value on the list
    cipher = pow(message, e, n)
    return cipher

def decrypt(private_key, cipher):
    # Unpack the key into it's components
    d, n = private_key
    message = pow(cipher, d, n)
    return message