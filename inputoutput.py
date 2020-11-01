# Coding utf-8
import os.path

def insertText(inputText):
    text = input("Write your note: \n")
    inputText.write(text)
    inputText.close()

def files(fileName):
    if os.path.exists(fileName + ".txt"):
        while os.path.exists(fileName + ".txt"):
            print("The file is already exists. Please, rename it.")
            fname = input("Please insert a new name of the file you want to create: ")
            rfile = fname + ".txt"
            if os.path.isfile(rfile):
                continue
            else:
                filer = open(rfile, "w")
                insertText(filer)
                break
    else:
        cfile = fileName + ".txt"
        filen = open(cfile, "w")
        insertText(filen)

def main():
    print("Welcome to a note-taking program")
    # Asking for the filename
    fileName = input("Please insert a name of the file you want to create: ")
    files(fileName)

if __name__ == "__main__":
    main()