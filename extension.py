filename=input("Input the Filename: ")
ext_dict={"py":"python","txt":"text","ppt":"powerpoint presentation","docx":"word document"}
index=0
for i in range(len(filename)):
    if filename[i]==".":
        index=i
for item in ext_dict:
    if filename[index+1: ]==item:
        print("The extension of the file is: '"+ext_dict[item]+"'")
