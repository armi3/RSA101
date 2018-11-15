import modular_arithmetic as calc
import random

def modulus(p, q):
    # n is the modulus for the public and private keys
    n = p * q
    return n

def totient(p, q):
    # Check p and q are prime
    if not (calc.is_prime(p) and calc.is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # phi(n) is the totient of the modulus n
    phi = (p-1) * (q-1)
    return phi

def public_key_exponent(phi):
    # Condition 1: 1 < e < phi(n)
    e = random.randrange(1, phi)

    # Contidion 2: e and phi(n) must be coprime
    g = calc.GCD(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = calc.GCD(e, phi) 
    return e

def private_key_exponent(phi):
    # Satisfy the congruence relation e*d=1 mod(phi(n))
    e = public_key_exponent(phi)
    d = calc.multiplicative_inverse(e, phi)
    return d

def public_key(p,q):
    # (e, n)
    e = public_key_exponent(totient(p,q))
    n = modulus(p,q)
    return (e,n)

def private_key(p,q):
    # (d, n)
    d = private_key_exponent(totient(p,q))
    n = modulus(p,q)
    return (d,n)

def keypair(p, q):
    pub = public_key(p,q)
    priv = private_key(p,q)
    return pub, priv

def encrypt_txt(public_key, msg):
    # Unpack the key into it's components
    e, n = public_key
    #cipher = calc.binary_exponentiation(msg, e, n)
    cipher = [(ord(char) ** e) % n for char in msg]
    return cipher

def decrypt_txt(private_key, cipher):
    # Unpack the key into it's components
    d, n = private_key
    #msg = calc.binary_exponentiation(cipher, d, n)
    msg = [chr((char ** d) % n) for char in cipher]
    return ''.join(msg)
