i = 0
while i < 3:
    print(i)
    text = input("Enter text: ")
    if text == "Hello":
        print("Got Hello on input")
    elif text == "Bye":
        print("Got Bye on input")
    else:
        print("Did not get Hello or Bye on input")
    i += 1
