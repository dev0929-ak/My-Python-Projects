print("Welcome to Age Checker. Where you can enter your age and check the possibilities")
print("Here are some criteria")
# Criteria
print("If your age is above 18 then you are an adult")
print("If your age is above 13 but below 18, you are a teenager and you can use social media")
print("If your age is above than 3 but less than 18, then you are schooling")
print("If your age is above than 3 but less than 13, then you are a child")
print("Else you are a baby")

# Personal Details
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name: " + str(name))
print("Age: " + str(age))

# Main Calculation
if age > 18:
    print("You are an adult")
elif age > 13 < 18:
    print("You are a teenager and you can use social media")
elif age > 3 < 18:
    print("You are in school")
elif age > 3 < 13:
    print("You are a child")
else:
    print("You are a baby")
