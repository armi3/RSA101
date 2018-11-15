# Verify if integer is prime
def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, x):
        if x % i == 0:
            return False
    return True

# GCD (Greatest Common Divisor) with Euclid's Algorithm
# Coprimes if GCD = 1
def GCD(a, b):
	if b>a:
		c=b
		d=a
		while d != 0:
        	c, d = d, c % d
        return c
	while b != 0:
        a, b = b, a % b
    return a

# Multiplicative inverse with Euclid's Extended Algorithm (Bezout)
# GCD(a, mod) = x*a + y*mod
# 1 = x*a + y*mod 
def multiplicative_inverse(a, mod):
	aO, bO = a, mod

    x=lasty=0
    y=lastx=1
    while (mod!=0):
        q= a/mod
        a, mod = mod, a%mod
        x, lastx = lastx-q*x, x
        y, lasty = lasty-q*y, y

    return lastx

# Exponentiation by Squaring / Binary Exponentiation
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
