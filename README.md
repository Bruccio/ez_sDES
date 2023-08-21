# ez_sDES
A short and easy-to-read (and use) version of the simplified Data Encryption Standard

DES is a symmetric-key block cipher used for encryption and decryption of data. This implementation is meant to provide a basic understanding of the DES algorithm and its core components. Please note that this code is for educational purposes and may not be suitable for production use.

Features
Initial permutation (IP) and inverse initial permutation (IP^-1) functions.
Key generation with P10 and P8 permutations, as well as left shift operations (LSHIFT-1 and LSHIFT-2).
Expansion function (E(p)) to expand the input data.
Substitution boxes (S0 and S1) for data transformation.
P4 permutation and XOR functions for data manipulation.
Encryption and decryption functions using a given plaintext and key.
Usage-->
Keyboard Input Mode: You can provide input through the keyboard. Run the script and enter the binary bits for both the plaintext and the key when prompted.

Manual Input Mode: Alternatively, you can manually set the values of the text and key lists in the code to perform encryption and decryption on a predefined input.

Encryption and Decryption: The code supports encryption and decryption using the DES algorithm. You can choose whether to encrypt or decrypt by commenting or uncommenting the appropriate lines in the __main__ block.

How does it work?
The plaintext and key are initially provided as lists of binary bits.
The key goes through permutation (P10) and left shift operations (LSHIFT-1 and LSHIFT-2) to generate two subkeys.
The initial permutation (IP) is applied to the plaintext.
The algorithm proceeds with the Feistel network, where the plaintext is divided into left and right halves.
The expansion function (E(p)) is used to expand the right half of the plaintext.
The expanded right half is XORed with the subkey, and the result goes through substitution boxes (S0 and S1).
The output of the substitution boxes is permutated (P4).
The permutated value is XORed with the original left half of the plaintext.
The left and right halves are swapped, and the process is repeated using the second subkey.
The final output of the Feistel network goes through the inverse initial permutation (IP^-1) to obtain the encrypted/decrypted data.
Important Note
This implementation is for educational purposes only and is not suitable for secure data encryption. DES has been deprecated due to security vulnerabilities, and modern encryption algorithms like AES should be used for any practical applications requiring data security.


This code has been entirely created by bruccio.
