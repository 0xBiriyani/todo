
import os
file= open("mydairy1.txt", "w")
file.write("Today I worked late night, I Learned new things ")

file= open("mydairy1.txt", "r")
print(file.read())
#os.remove("mydairy1.txt")

#if os.path.exists("mydairy1.txt"):
  #  os.remove("mydairy.txt")
