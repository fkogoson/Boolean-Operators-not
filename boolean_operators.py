statement_one = False

statement_two = True

credits = 120
gpa = 1.8

if not (credits >= 120):
  print("You do not have enough credits to graduate.")
elif not (gpa >= 2.0):
  print("Your GPA is not high enough to graduate.")
elif not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")
