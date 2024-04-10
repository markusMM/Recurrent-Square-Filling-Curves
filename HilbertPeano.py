# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:37:53 2018

Markus' Recursive Hilbert-Peano Function

it can break down from any dxd square which is not a multiple of a prime number
it has an asymetric 3x3 base in case of a hulbert structure before.

TODO: Peano-Hilbert version using a symetric z-base when breaking from a peano 
curve. -> A completely centered solution for square 2D space fillings.

@author: Markus Meister
"""
#%% -- imports --
import numpy as np
#%% -- helpers --
def prime_factors(n):
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
    primes = prime_factors(n)
    mod = True
    for prime in primes:
        if all(np.mod(prime,[2,3])):
            mod = False
    return mod

#%% -- main fcn --
def HilbertPeano(d,verbose=False,sub=False):
    
    map = np.zeros([d,d],dtype=int)
    hil = not np.ceil(np.mod(d,2)) or d == 2 #not np.ceil(np.mod(np.sqrt(d),2)) or d==2
#    if sub:
#        hil = not hil
    #print(hil)
    if hil:
            bas = np.array([[2,1],[3,4]],dtype=int).T - 1
    else:
            bas = np.flipud(np.array([[1,6,7],[2,5,8],[3,4,9]]).T.T.T) - 1
    sub_hilm3 = np.array([
            [5,6,7],
            [4,3,8],
            [1,2,9]
            ],dtype=int) - 1
    #x,y = crd
    diff = d//(3-hil)
    #print(diff)
    hm3 = not np.ceil(np.mod(diff,2))
    if not hil and sub:
        bas = sub_hilm3
    if not np.mod(d,3-hil) and diff > 1: 
        #hil = not np.ceil(np.mod(d,2)) or d == 2
        #hm3 = not np.ceil(np.mod(diff,2)) or d == 2
        for r in bas.flatten():
            #print(r)
            m = HilbertPeano(
                    diff or d//(2 + hm3),verbose=verbose,
                    sub = hil and not hm3 or sub
                    )
            
            if not hm3 and hil and not np.mod((r+1),2):
                m = np.fliplr(np.max(m)-m)
            
            if hil:
                if r==0:
                    m = np.fliplr(np.fliplr(m).T)
                if r==3:
                    m = m.T
            else:
                if not np.mod((r+1),2):
                    m = np.flipud(m)
                if r+1>3 and r+1<7:
                    m = np.fliplr(np.flipud(m))
            
            #print((bas==r)*int(d))
            #print(map[(bas==r)*int(d):(bas==r)*int(d)+np.ones([diff,diff])*int(d)])
            ind_x,ind_y = np.where(bas==r)
            ind_y += 1
            ind_y *= diff
            ind_x += 1
            ind_x *= diff
            if verbose:
                print(ind_x,ind_y)
                print(diff)
                print(m)
            map[ind_x[0]-diff:ind_x[0],ind_y[0]-diff:ind_y[0]] = m + r*diff**2
    else:
        if sub and hil:
            map = sub_hilm3
            #print('bla')
        else:
            map = bas
    return map

#%% -- main test --

if __name__ == "__main__":
    
    d = 12
    
    primes = prime_factors(d)
    assert prime_check(d)
    
    map = HilbertPeano(d,verbose=0)
    
    print(map)
    
    import matplotlib.pyplot as plt
    
    plt.imshow(map)
    
    
