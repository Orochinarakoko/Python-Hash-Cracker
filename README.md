# Python-Hash-Cracker
This is a simple , GUI based python script that utilises the hashlib module in order to run a wordlist attack against a hashed password.


The way it works is :
  1) The user enter the hash itself , the type of algorithm used to generate the hash , and the wordlist they wish to use
  2) The program works through each line of the program , hashing the word on that line , using the specified hashing algorithm
  3) If the inputted hash and the hash generated from the word from the wordlist match , then the original word must have been the word in that line of the wordlist


There may be error in the code , or unessecrary line of code in the code used for debugging - feel free to notify me if you find anything :-)

I may update this in the future , to include other hashes , of particular intrest NTLM , however I may need to look in to this more as it may be a more complicated process.
