# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:37:53 2018

Markus' Recursive Peano-Hilbert function

it can break down from any d*d square which is not a multiple of a prime number
it has a reverse z-curve for any 2^m * 2^m blocks inside 3^n * 3^n blocks.

This is the Peano-Hilbert version of the Hilbert-Peano function I have implemented before.

Here, we are using a symmetric z-base when breaking from a Peano curve.
Now, we have a completely centered solution for square 2D space-filling curves.

Although 3D versions from other authors using convenient bit representations
do exist.

@author: Markus Meister
"""
# %% -- imports --
import numpy as np

# %% -- helpers --
def prime_factors(n):
    """
    Returns the prime factors of a given number.

    Args:
        n (int): The number to factorize.

    Returns:
        list: A list of prime factors of the input number.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def prime_check(n):
    """
    Checks if a number is a prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the input number is prime, False otherwise.
    """
    primes = prime_factors(n)
    mod = True
    for prime in primes:
        if all(np.mod(prime, [2, 3])):
            mod = False
    return mod

# %% -- main function --
def peano_hilbert(d, verbose=False, sub=False):
    """
    Generate a Peano-Hilbert curve map of size dxd.

    Args:
        d (int): The size of the map (dxd).
        verbose (bool, optional): If True, prints additional information. Defaults to False.
        sub (bool, optional): If True, indicates that it's a submap. Defaults to False.

    Returns:
        numpy.ndarray: A 2D array representing the Peano-Hilbert curve map.
    """
    map = np.zeros([d, d], dtype=int)
    pea = not np.ceil(np.mod(d, 3)) or d == 3
    
    if not pea:
        bas = np.array([[2, 1], [3, 4]], dtype=int).T - 1
    else:
        bas = np.flipud(np.array([[1, 6, 7], [2, 5, 8], [3, 4, 9]]).T.T.T) - 1
    
    sub_peam3 = np.array([
            [3, 4],
            [1, 2],
            ], dtype=int) - 1
    
    diff = d // (2 + pea)
    hm3 = not np.ceil(np.mod(diff, 3))
    
    if not pea and sub:
        bas = sub_peam3
        
    if not np.mod(d, 2 + pea) and diff > 1: 
        for r in bas.flatten():
            m = peano_hilbert(
                    diff or d // (3 - hm3), verbose=verbose,
                    sub=pea and not hm3 or sub
                    )
            if not pea:
                if r == 0:
                    m = np.fliplr(np.fliplr(m).T)
                if r == 3:
                    m = m.T
            else:
                if not np.mod((r + 1), 2):
                    m = np.flipud(m)
                if r + 1 > 3 and r + 1 < 7:
                    m = np.fliplr(np.flipud(m))
            
            ind_x, ind_y = np.where(bas == r)
            ind_y += 1
            ind_y *= diff
            ind_x += 1
            ind_x *= diff
            
            if verbose:
                print(ind_x, ind_y)
                print(diff)
                print(m)
            map[ind_x[0] - diff:ind_x[0], ind_y[0] - diff:ind_y[0]] = m + r * diff ** 2
    else:
        if sub and not pea:
            map = sub_peam3
        else:
            map = bas
    return map

# %% -- main demo --
if __name__ == "__main__":
    
    d = 12
    
    primes = prime_factors(d)
    assert prime_check(d)
    
    map = peano_hilbert(d, verbose=1)
    
    print(map)
    
    import matplotlib.pyplot as plt
    
    plt.imshow(map)
