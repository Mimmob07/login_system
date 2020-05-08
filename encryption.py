#!/usr/bin/python
print("""
░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
\n""")

codec = ("Do you want to Encode (E) or Decode (D)?")
inp = ("| => ")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
encoding = ["w", "2", "g", "q", "r", "4", "8", "h", "i", "c", "6", "v", "n", "m", "1", "z", "f", "3", "d", "5", "t", "a",
            "s", "j", "l", "e", " ", ")", "(", "*", "&", "^", "%", "$", "#", "@", "!"]
print(codec)
choice = input(inp)
print("what do you want to encode/decode")
hj = input(inp)
hk = len(hj)
output = ""
oldchar = ""
newchar = ""
if choice == "e" or choice == "E":
    for i in range(0, hk):
        oldchar = hj[i]
        for j in range(0, len(encoding)):
            if oldchar == letters[j]:
                newchar = encoding[j]
        output = output + newchar
elif choice == "d" or choice == "D":
    for i in range(0, hk):
        oldchar = hj[i]
        for j in range (0, len(encoding)):
            if oldchar == encoding[j]:
                newchar = letters[j]
        output = output + newchar
else:
    print("\nanswer not recognized\n")
print(output)