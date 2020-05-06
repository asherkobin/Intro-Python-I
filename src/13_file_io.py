"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os
cwd = os.getcwd()
print("*CWD* " + cwd)
with open("./src/foo.txt", "r") as f:
  text = f.read()
  print(text)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open("./src/bar.txt", "w") as f:
  f.write("Line One\n")
  f.write("Line Two\n")
  f.write("Line Three\n")

with open ("./src/bar.txt", "r") as f:
  print(f.read())