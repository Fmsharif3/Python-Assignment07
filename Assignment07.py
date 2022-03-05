# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (FSharif, 2.28.2022, Pickle Demo)
# <Fatima Sharif>,<2.28.2022>,Created Script
# ------------------------------------------------- #

# Exception handling example:

try:
    file = open("AppData.txt", "r")
except IOError:
    print("File not found!")
else:
    print("File found!") 

# Pickling Example:
import pickle     # this imports code from another code file!

int_StudentId = int(input("Enter Your Student Id: "))
str_StudentName = str(input("Enter Your First And Last Name: "))
lstStudents = [int_StudentId, str_StudentName]
print(lstStudents)

# Now we store the data with the pickle.dump method
objFile = open("AppData.dat", "ab")
pickle.dump(lstStudents, objFile)
objFile.close()

# And, we read the data back with the pickle.load method
objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile)   # load() only loads one row of data.
objFile.close()

print(objFileData)
