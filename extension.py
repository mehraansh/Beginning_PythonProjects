import re
fileName = input("Input the Filename: ")
# code to find characters in string
res1 = " ".join(re.split("[.py]*", fileName))
 # printing resultant string
print("The extension of the file is Python" )
