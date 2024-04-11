def encoder(s):
    new = ""
    for letter in s:
        num = int(letter)
        if num == 7:
            new += "0"
        elif num == 8:
           new += "1"
        elif num == 9:
            new += "2"
        else:
            num += 3
            new += str(num)
    return new
def decoder(s):
    new = ""
    for letter in s:
        num = int(letter)
        if num == 2:
            new += "9"
        elif num == 1:
            new += "8"
        elif num == 0:
            new+= "7"
        else:
            num -= 3
            new += str(num)
    return new
menu = """Menu
-------------
1. Encode
2. Decode
3. Quit"""
print(menu)

sel = int(input("Please enter an option: "))
while sel != 3:
    if sel == 1:
        number = input("Please enter your password to encode: ")
        encode = encoder(number)
        print("Your password has been encoded and stored!")
    if sel == 2:
        decode = decoder(encode)
        print(f"The encoded password is {encode}, and the original password is {decode}.")
    print(menu)
    sel = int(input("Please enter an option: "))



