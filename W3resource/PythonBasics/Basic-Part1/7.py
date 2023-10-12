'''Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java'''

fileName=input("Enter file name: ")
fileName=fileName.split('.')
print(f"Your file extension is : {fileName[1]}")
