file = open("test.txt","r")
arrA = []
arrAB = []
arrAA_AAB = []
arrABC = []
arrAAstarAA = []

#The value of the flag indicates what came before the character being read
#A positive flag indicates that the substring "aa" has not occured before the current character
#A negative flag indicates that the substring "aa" has occured before the current character
#For a character x and wildcard *:
#   flag = (+/-) 1 indicates we don't have *ax*, *aax*, *abx*. Default state
#   flag = (+/-) 2 indicates we have *ax* but not *aax*
#   flag = (+/-) 4 indicates we have *aax*
#   flag = (+/-) 8 indicates we have *abx*
flag = 1

def resetFlag(flag):
    """function re-sets the absolute value of the flag to 1, while preserving the 
    flag's sign"""
    return flag / abs(flag)

def parse(flag):
    #firstAA and aaFlag needed to avoid the first appearance of a "aaa" string 
    #from being counted as a aa*aa string
    firstAA = False
    aaFlag = -1
    #count = index of current character
    count = 0
    for line in file:
        for char in line:
            if firstAA:# if "aa" substring has been found so far
                aaFlag +=1
            
            if abs(flag) == 1:
                if char == "a" or char == "A": #if "a"
                    #update lists
                    arrA.append(count)
                    #change state to *ax* 
                    flag *=2

            elif abs(flag) == 2:
                if char == "b" or char == "B": #if "ab"
                    arrAB.append(count)
                    #change state to *abx*
                    flag *= 4
                elif char == "a" or char == "A": #if "aa"
                    arrA.append(count)
                    arrAA_AAB.append(count)
                    if flag>0: #if "aa" substring has not appeared before this
                        #change state to *aax* and make flag negative
                        firstAA = True
                        flag *= -2
                    else:
                        arrAAstarAA.append(count)
                        #change state to *aax*
                        flag *=2
                else:
                    #change state to default
                    flag = resetFlag(flag)

            elif flag == -4:
                if char == "a" or char == "A": #if "aaa"
                    arrA.append(count)
                    arrAA_AAB.append(count)
                    if aaFlag>0: #prevents first appearence of "aa" as "aaa" from being counted as "aa*aa"
                        arrAAstarAA.append(count)
                elif char == "b" or char == "B": #if "aab"
                    arrAB.append(count)
                    arrAA_AAB.append(count)
                    #change state to *abx*
                    flag *=2
                else:
                    #change state to default
                    flag = resetFlag(flag)

            elif abs(flag) == 8:
                if char == "a" or char == "A": # if "aba"
                    arrA.append(count)
                    #change state to default
                    flag = resetFlag(flag)
                elif char == "c" or char == "C": # if "abc"
                    arrABC.append(count)
                    #change state to default
                    flag = resetFlag(flag)
                else:
                    #change state to default
                    flag = resetFlag(flag)
            count+=1
          
        
parse(flag)
print("a: " + str(arrA))
print("ab: " + str(arrAB))
print("aa or aab: "+ str(arrAA_AAB))
print("abc: " + str(arrABC))
print("aa*aa " + str(arrAAstarAA))




            