import colorama
from colorama import Fore, Back, Style
from rsa import encrypt
from util import *
import numpy as np

def caesar_cipher():
    print("Caesar Cipher")  
    
def monoalphebatic_cipher():
    print("Monoalphebatic Cipher") 
  
def hill_cipher():
    K = []
    def get_key(m):
        for i in range(m):
            line = input()
            row = line.split()
            row = [int(e) for e in row]
            K.append(row)
        return K
    
    def encrypt(K, P):
        C = []
        m = len(K)
        
        for row in K:
            sum = 0
            for i in range(m):
                sum += row[i] * P[i]
            
            C.append(sum % 26)
        # print(C)
        return C
            
    def block(K, P):
        BC = []
        K = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
        
        for x in range(0, len(P), 3):
            block = P[x: x + 3]
            # print(block)
            c = encrypt(K, block)
            BC.append(c)
        
        C = ""
        for row in BC:
            L = [decoding(e) for e in row]
            B = "".join(L)
            C += B
            
        return C
            
        

            
        
            
    starprint(Fore.MAGENTA, 10, 2, "Hill Cipher")
    
    P = get_P()
    print(P)
    m = int(input("Size of the matrix: "))
    # K = get_key(m)
    
    block(K, P)
    
def get_P():
    plain_text = input("Plain text: ").lower()
    P = [encoding(letter) for letter in plain_text]
    return P

def encoding(letter):
    return ord(letter) - ord("a")

def decoding(n):
    n += ord("A")
    return chr(n)