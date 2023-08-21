# This code has been entirely created by bruccio

# Initial permutation function
def initial_permutation(p):
    return [p[1], p[5], p[2], p[0], p[3], p[7], p[4], p[6]]

# Inverse initial permutation function
def inverse_initial_permutation(p):
    return [p[3], p[0], p[2], p[4], p[6], p[1], p[7], p[5]]

# P10 permutation function
def permutation_P10(k):
    return [k[2], k[4], k[1], k[6], k[3], k[9], k[0], k[8], k[7], k[5]]

# P8 permutation function
def permutation_P8(k):
    return [k[5], k[2], k[6], k[3], k[7], k[4], k[9], k[8]]

# Left shift function (1 position)
def left_shift(k):
    return [k[1], k[2], k[3], k[4], k[0], k[6], k[7], k[8], k[9], k[5]]

# Left shift function (2 positions)
def left_shift2(k):
    return [k[2], k[3], k[4], k[0], k[1], k[7], k[8], k[9], k[5], k[6]]

# Expansion function E(p)
def expansion_E(p):
    return [p[7], p[4], p[5], p[6], p[5], p[6], p[7], p[4]]

# P4 permutation function
def permutation_P4(p):
    return [p[1], p[3], p[2], p[0]]

# XOR function
def xor(p1, p2):
    p3 = []
    for i in range(len(p1)):
        p3.append(int(p1[i]) ^ int(p2[i]))
    return p3

def substitution_S0(t):
    s0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]
    row = int(str(t[0]) + str(t[3]), 2)
    column = int(str(t[1]) + str(t[2]), 2)
    value = '{0:b}'.format(s0[row][column]).zfill(2)
    return value

def substitution_S1(t):
    s1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]
    row = int(str(t[0]) + str(t[3]), 2)
    column = int(str(t[1]) + str(t[2]), 2)
    value = '{0:b}'.format(s1[row][column]).zfill(2)
    return value

def function_F(p, k):
    p_left = [p[0], p[1], p[2], p[3]]
    p_right = [p[4], p[5], p[6], p[7]]
    p_expanded = expansion_E(p)
    p_xor_k = xor(p_expanded, k)
    p_s0 = substitution_S0(p_xor_k[:4])
    p_s1 = substitution_S1(p_xor_k[4:])
    p_p4 = permutation_P4(p_s0 + p_s1)
    p4_xor_k = xor(p_p4, p_left)
    return p4_xor_k + p_right

def encryption(p, k):
    k_p10 = permutation_P10(k) 
    k_shifted1 = left_shift(k_p10)
    k1 = permutation_P8(k_shifted1)
    k_shifted2 = left_shift2(k_shifted1)
    k2 = permutation_P8(k_shifted2)
    
    p_ip = initial_permutation(p)
    p_ip_f1 = function_F(p_ip, k1)
    p_ip_sw = p_ip_f1[4:] + p_ip_f1[:4]
    p_ip_f2 = function_F(p_ip_sw, k2)
    p_ciphertext = inverse_initial_permutation(p_ip_f2)
    return p_ciphertext

def decryption(p, k):
    k_p10 = permutation_P10(k) 
    k_shifted1 = left_shift(k_p10)
    k1 = permutation_P8(k_shifted1)
    k_shifted2 = left_shift2(k_shifted1)
    k2 = permutation_P8(k_shifted2)
    
    p_ip = initial_permutation(p)
    p_ip_f2 = function_F(p_ip, k2)
    p_ip_sw = p_ip_f2[4:] + p_ip_f2[:4]
    p_ip_f1 = function_F(p_ip_sw, k1)
    p_decrypted = inverse_initial_permutation(p_ip_f1)
    return p_decrypted

if __name__ == '__main__':
    #------------------keyboard input------------------
    text = []
    print("Enter the TEXT:")
    for i in range(8):
        bit = input("Enter bit %d: " % (i+1))
        text.append(bit)
    key = []
    print("Enter the KEY:")
    for i in range(10):
        bit = input("Enter bit %d: " % (i+1))
        key.append(bit)
        
    # Comment out the function part that is not intended to be used
    encrypted_text = encryption(text, key)
    print("The encrypted text is ", encrypted_text)
    # decrypted_text = decryption(encrypted_text, key)
    # print("The decrypted text is ", decrypted_text)
#------------------manual input------------------
    # text = [0, 1, 1, 1, 0, 0, 1, 0]
    # key = [1, 1, 0, 1, 1, 0, 0, 1, 0, 1]

# This code has been entirely created by bruccio
