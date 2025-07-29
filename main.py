from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pass = input("Enter a master password: ")
key = load_key() + master_pass.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(pwd.encode()).decode())


def add():
    name = input("Account name: ")
    password = input("Password: ")
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("Do you want to add or view passwords? (type q to quit) ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue