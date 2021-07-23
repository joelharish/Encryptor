print("#########   ------|   ||\\||  (======)   #########")
print("#########   | |       ||\\||  (          #########")
print("#########   | |---|   ||\\||  (          #########")
print("#########   | |       ||\\||  (          #########")
print("#########   ------|   ||\\||  (======)   #########")

i = 0
while i <= 1000:
    def encyript(phrase):
        encryption = ""
        for letter in phrase:
            if letter in "AEIOUaeiou":
                if letter.isupper():
                    encryption = encryption + "G"
                else:
                    encryption = encryption + "g"
            else:
                encryption = encryption + letter
        return encryption


    print(encyript(input("Enter Your Normal Message : ")))

    i += 1