import string
#recording time of program
import time
#for SHA1 function
import hashlib
#for creating list of words to turn to SHA1 and check
from itertools import product

#minimum and maximum values that the password can be 
minimum = 1
maximum = 6

#list of hashed passwords to crack
hashed_passwords = [
        'c2543fff3bfa6f144c2f06a7de6cd10c0b650cae',
        'b47f363e2b430c0647f14deea3eced9b0ef300ce',
        'e74295bfc2ed0b52d40073e8ebad555100df1380',
        '0f7d0d088b6ea936fb25b477722d734706fe8b40',
        '77cfc481d3e76b543daf39e7f9bf86be2e664959',
        '5cc48a1da13ad8cef1f5fad70ead8362aabc68a1',
        '4bcc3a95bdd9a11b28883290b03086e82af90212',
        '7302ba343c5ef19004df7489794a0adaee68d285',
        '21e7133508c40bbdf2be8a7bdc35b7de0b618ae4',
        '6ef80072f39071d4118a6e7890e209d4dd07e504',
        '02285af8f969dc5c7b12be72fbce858997afe80a',
        '57864da96344366865dd7cade69467d811a7961b'
    ]


bchlist = ['902608824fae2a1918d54d569d20819a4288a4e4',
           '88d0b34055b79644196fce25f876bc1a5ef654d3',
           '5b8f495b7f02b62eb228c5dbece7c2f81b60b9a3',
           ]
           
           

#take recording of start time

def basicpasswordcrack(passwordlist):
    crackcounter = 0
    starttime = time.perf_counter()
    
    for i in range(minimum, maximum + 1):
        #creates list of passwords to the maximum length of maximum (6)
        passwords = product(string.ascii_lowercase + string.digits, repeat=i)
        for j in passwords:
            #checks if all passwords have been cracked
            if crackcounter == len(hashed_passwords):
                print("All hashes have been cracked")
                return 0

            hashstring = hashlib.sha1(str.encode(''.join(j))).hexdigest()
            
            #checks if the hashed string from the loop is inside the hashed_passwords list
            if hashstring in hashed_passwords:
                #records the current time of program running
                cracktime = time.perf_counter()
                #calculates how long it took to crack the current hash
                calculated_time = (cracktime - starttime)
                print("Time to crack this hash was ", calculated_time, " seconds")
                #add 1 to crack counter as one of the hashes has been cracked
                crackcounter += 1
                print ("Cracked hash: ", hashstring)
                print("String is: ", j)

    print("Error: Not all hashes have been cracked")
    return -1

def bchbruteforce(passwordlist):
    starttime = time.perf_counter()
    bchminimum = 10
    crackcounter = 0
    bchmaximum = 10
    for i in range (bchminimum, bchmaximum + 1):
        passwords = product(string.digits, repeat=i)
        for j in passwords:
            if crackcounter ==len(bchlist):
                print("All hashes have been cracked")
                return 0

            hashstring = hashlib.sha1(str.encode(''.join(j))).hexdigest()

            if hashstring in bchlist:
                cracktime = time.perf_counter()
                calculated_time = (cracktime - starttime)
                crackcounter += 1
                print ("Cracked hash: ", hashstring)
                print("String is ", j)

    print("Error: Not all hashes have been cracked")
    return -1
    


#basicpasswordcrack(hashed_passwords)
bchbruteforce(bchlist)



