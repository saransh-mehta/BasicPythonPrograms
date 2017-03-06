#writing a txt file with each sentence in new line

file=open("F:/PYTHON PROGRAMS/writeTest.txt","w+")

def nextLine(content):
    sentence=[]
    string=''
    sentence=content.split(".")
    for line in sentence:
        string=string+line+"\n"
        print(string)
    file.write(string)
    print("writing done")
    file.close()
value=input("add all content : ")
nextLine(value)
