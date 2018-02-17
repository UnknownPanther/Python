# Python program which displays Calendar of given month of the year.
# 17.02.2018 | (2)

# Import module
import calendar

# Ask month(mm) and Year(yy)
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

print("Counting...")
print("Done!")
print("")
# Display Calendar
print(calendar.month(yy, mm))


