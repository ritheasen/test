



inputString = str(input("Enter the string to encode"))

for i in inputString:
    B = ord(i) - 13
    S = ord(i) + 13
    print(f"{i} : {ord(i)}",end=",")
    if ord(i) > 77:
        print(f"{ord(i)-13}")
        print(chr(B),end=" ")
    else:
        print(f"{ord(i)+13}")
        print(chr(S))


    #print(f"{chr(B)}+{chr(S)}")
    # print(ord(i),end=",")
    # print(i,end="")
    # print(f"{chr(ord(i) + 13)}")
    # print(f"{chr(ord(i) - 13)}")




