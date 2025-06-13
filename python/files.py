"""



#files : data store in a storage device

types: 1) text files : .txt, .c 
       2) binary files  : .jpg, .dat, .png
       



# How to read file in python
f = open("file.txt","r")
text = f.read()
print(text)

#closing file
f.close()


r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
'rb' will open for read in binary mode.
'rt' will open for read in text mode.


#how to write files
f = open("file.txt", "w")
f.write("Hey! i wanna write something speccific in your file, give me permission.")

f.close()

# with statement
with open("file.txt", "r") as f:
    text = f.read()


print(text)
"""


"""Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’."""

f = open("poem.txt","w")

f.write("twinkle")

f = open("poem.txt","r")
text = f.read()

print(text)
f.close