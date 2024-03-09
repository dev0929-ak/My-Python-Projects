# Entering of Information
info = input("Enter Username: ")
level = int(input("Enter your level: "))
# Notice
print("Before you start, let me tell you the criteria according to the level")
print("""The criteria according to the level is: 
      Level 1 - 15 Beginner
      Level 15 - 30 Advanced
      Level 30 - 50 Veteran
      Level 50 - 75 Super Veteran
      Level 75 - 90 Elite
      Level 90 - 100 God Level""")
# Choice
ch = int(input("Do you want to exit or continue (type 1 for continue or 2 for exit)"))
if ch==1:
    print("Okay here we go!")
if ch==2:
    exit
# Printing of Information
print()
print(info)
print()
print("level", level)
# Main Calculation (Level)
print()
if level>90 and level<=100:
    print("According to your level", level, "Your level is God Level")
elif level>75 and level<=90:
    print("According to your level", level, "Your level is Elite")
elif level>50 and level<=75:
    print("According to your level", level, "Your level is Super Veteran")
elif level>30 and level<=50:
    print("According to your level", level, "Your level is Veteran")
elif level>15 and level<=30:
    print("According to your level", level, "Your level is Advanced")
elif level>1 and level<=15:
    print("According to your level", level, "Your level is Beginner")
else:
    print("Invalid Input")