# BruteForce-PasswordCracker

This repository contains a Python implementation of a brute force password cracker for hashed passwords. The script uses the SHA-1 cryptographic hash function to hash generated passwords and compare them to a list of hashed passwords to crack.

This was completed as part of my Cryptography module during my time at university.

## Features

The script contains two functions:

- `basicpasswordcrack`: This function generates all possible combinations of lowercase letters and digits up to a certain length (6 by default), hashes each combination using SHA-1, and checks if the hashed combination is in a list of hashed passwords. If it finds a match, it prints the cracked hash and the corresponding password.

- `bchbruteforce`: This function does the same as `basicpasswordcrack`, but it only generates combinations of digits and it's intended to crack a different list of hashed passwords.

Both functions also keep track of the time it takes to crack each password.

## Usage

To use the script, call the `basicpasswordcrack` or `bchbruteforce` function with a list of hashed passwords as argument.

