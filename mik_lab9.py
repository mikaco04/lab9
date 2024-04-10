#mikaylacohen
def encode():
    pass

def display_menu():
    print("Menu"
          "\n-------------"
          "\n1. Encode"
          "\n2. Decode"
          "\n3. Quit")
def main():
    while True:
    display_menu()
    selection = int(input("Please enter an option:"))
    if selection = 1:
        encoded_pass= input("Please enter your password to encode:")
        encode(encoded_pass)
        print("Your password has been encoded and stored!")
    elif selection = 2:
        pass
    elif selection = 3:
        break

def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        decoded_password += str((int(char) - 3) % 10)
    return decoded_password

if __name__ == '__main__':
    main()
