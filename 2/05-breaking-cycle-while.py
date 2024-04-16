i = 1
while i <= 3:
    print(i)
    if i == 2:
        i += 1
        continue
    if i == 3:
        break
    text = input("Enter text: ")
    if text == "Hello":
        print("Got Hello on input")
    elif text == "Bye":
        print("Got Bye on input")
    else:
        print("Did not get Hello or Bye on input")
    i += 1
