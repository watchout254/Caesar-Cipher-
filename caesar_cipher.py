import sys

print("\t\t\t👩‍💻Hey there. Welcome to clown caesar cipher👨🏻‍💻\n")
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
         'u','v','w','x','y','z']

def encryption(plain,shift):
    cipher = ""
    for char in plain:
        if char in alpha:
            pos = alpha.index(char)
            brapos = (pos+shift)%26
            cipher += alpha[brapos]
        else:
            cipher += char
    print(f"\tYowww!! Here's the text after encryption:👉🏻👉🏻 {cipher}\n")

def decryption(cipher,shift):
    plain = ""
    for char in cipher:
        if char in alpha:
            pos = alpha.index(char)
            brapos = (pos-shift)%26
            plain += alpha[brapos]
        else:
            plain += char
    print(f"\tYowww!! Here's the text after decryption:👉🏻👉🏻 {plain}\n")

finish = False
while not finish:
    cryption = input("\tType 'encrypt' for encryption, type 'decrypt' for decryption:  \n")
    message = input("\tType your message: \n").lower()
    shift_no = int(input("\tType the shift number: \n"))

    if cryption=="encrypt":
        encryption(plain= message,shift=shift_no)

    elif cryption=="decrypt":
        decryption(cipher=message,shift=shift_no)

    again = input("Type 'yes' to play again, else 'no' to quit: \n")
    if again=="no":
        finish=True
        print("Byee.!!👋👋👋")
        sys.exit()







