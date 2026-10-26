password = input("Enter a password: ")

if len(password) < 8:
    print("Invalid Password!")
else:
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        print("Password is Valid")
    else:
        print("Invalid Password!")