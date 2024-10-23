while True :
    try:
        with open("ahmed.txt" , "a+") as f :
            f.write("hello\n    ")
            f.seek(0)
            read = f.read()
            print(read)
        break
    except IOError():
        input("File couldn't open , please press enter to try again")


