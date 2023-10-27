#Check bodytemperature and give whether they are normal, high fever or cold fever

bodytemp = float(input("Enter your Body Temperature: "))
if bodytemp>97 and bodytemp<99:
    print("You are normal")
elif bodytemp<97:
    print("You have Cold fever, if you still alive.")
else:
    print("You have high Fever")