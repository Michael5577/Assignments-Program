month = int(input("Input your month as a number"))

match month:
  case 1:
    print("You have entered January")
  case 2:
    print("You have entered February")
  case 3:
    print("You have entered March")
  case 4:
    print("You have entered April")
  case _:
    print("Inavalid nimber")
