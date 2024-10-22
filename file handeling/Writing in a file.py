with open("text2.txt" , "w") as f :
    f.write("test")
    f.seek(0)
    f.write("Test") # in this case second Test will overwrite the first one
    f.write('R') # overwrite the first letter only
# when opening a file thats not founded it will automaticlly create one
with open ("text.txt" , "r") as rf :
    with open("text_copy.txt", "w") as wf:
        for line in rf :
            wf.write(line)
#creating another copy of the file with different name
# if u want to deal with a picture u have to switch from text to binary to deal with it
with open ("x.jpeg","rb") as rf:
    with open ("x.jpeg" , "wb") as wf :
        for line in rf :
            wf.write(line)
