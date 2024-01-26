import string # this is use to enter your password can be string is added 
import getpass # this use to enter your password but not be visible

def check_pwd():
    password = getpass.getpass("Enter Password:")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_cont = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_cont += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_cont >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    # remarks section
    if strength == 1:
        remarks = "very bad password!!! "
    elif strength == 2:
        remarks = "not a good password!!!"
    elif strength == 3:
        remarks = "It is a weak password, change to a new one"
    elif strength == 4:
        remarks = "It's a weak password, try a better one"
    elif strength == 5:
        remarks = "very strong password!!!"

    print('your password has:')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_cont} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"password strength: {strength}")
    print(f"Hint: {remarks}")

def ask_for_password(another_pwd=False):
    valid = False
    if another_pwd:
        choice = input(' Do you want to enter another password (y/n):')
    else:
        choice = input(' Do you want to change password (y/n):')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid choice, Try Again')

if __name__ == '__main__':
    print('----Welcome To Password Checker----')
    ask_password = ask_for_password()
    while ask_password:
        check_pwd()
        ask_password = ask_for_password(True)
