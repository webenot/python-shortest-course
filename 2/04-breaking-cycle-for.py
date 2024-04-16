for i in range(3):
    print(i)
    if i == 1:
        continue
    if i == 2:
        break
    text = input("Enter text: ")
    if text == "Hello":
        print("Got Hello on input")
    elif text == "Bye":
        print("Got Bye on input")
    else:
        print("Did not get Hello or Bye on input")
