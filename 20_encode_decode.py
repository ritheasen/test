
userEnter = int(input("Press 1 to encode \nPress 2 to decode"))
newString = ""
if userEnter == 1:
    inputString = str(input("Enter the string to encode"))
    for i in inputString:
        print(f"{i} : {ord(i)}")
        for j in range (0,len(inputString)):
            if inputString[j] == ord(i) > 77:
                newString = inputString[j].ord(i)-13
            else:
                ord(i)+13

        #print(f"{chr(ord(i)+13)}")
#print(f"{chr(ord(i)+13)}",end="")
print(newString)
#elif userEnter == 2:

