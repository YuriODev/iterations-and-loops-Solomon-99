correct_password = input()
password = 0
while password != correct_password:
    password = input()
    print(password)
    if password == correct_password:
        print("Done")
        break
    else:
        print("Error")