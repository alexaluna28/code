import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1 #13
import matplotlib.pyplot as plt2 #14
import matplotlib.pyplot as plt3 #15
import matplotlib.pyplot as plt4 #16
import matplotlib.pyplot as plt5 #17
import matplotlib.pyplot as plt6 #18
import matplotlib.pyplot as plt7 #19
import matplotlib.pyplot as plt8 #20
import matplotlib.pyplot as plt9 #21
import matplotlib.pyplot as plt10 #22
import matplotlib.pyplot as plt11 #23
import matplotlib.pyplot as plt12 #24
import matplotlib.pyplot as plt13 #25
import matplotlib.pyplot as plt14 #26
import matplotlib.pyplot as plt15 #27
import matplotlib.pyplot as plt16 #28
import matplotlib.pyplot as plt17 #29
import matplotlib.pyplot as plt18 #30
import matplotlib.pyplot as plt19 #31
import matplotlib.pyplot as plt20 #32
import matplotlib.pyplot as plt21 #33
import matplotlib.pyplot as plt22 #34
import matplotlib.pyplot as plt23 #35
import matplotlib.pyplot as plt24 #36
import matplotlib.pyplot as plt25 #37
import matplotlib.pyplot as plt26 #38
import matplotlib.pyplot as plt27 #39
import matplotlib.pyplot as plt28 #40
import matplotlib.pyplot as plt29 #41
import matplotlib.pyplot as plt30 #42
import matplotlib.pyplot as plt31 #43
import matplotlib.pyplot as plt32 #44
import matplotlib.pyplot as plt33 #45
import matplotlib.pyplot as plt34 #46
import matplotlib.pyplot as plt35 #47
import matplotlib.pyplot as plt36 #48
import matplotlib.pyplot as plt37 #49
import matplotlib.pyplot as plt38 #Total Bar 13-18
import matplotlib.pyplot as plt39 #Total Bar 19-29
import matplotlib.pyplot as plt40 #Total Bar 30-39
import matplotlib.pyplot as plt41 #Total Bar 40-49
import matplotlib.pyplot as plt42 #National Graph 13-18
import matplotlib.pyplot as plt43 #National Graph 19-29
import matplotlib.pyplot as plt44 #National Graph 30-39
import matplotlib.pyplot as plt45 #National Graph 40-49
import matplotlib.pyplot as plt46 #County Graph 13-18
import matplotlib.pyplot as plt47 #County Graph 19-29
import matplotlib.pyplot as plt48 #County Graph 30-39
import matplotlib.pyplot as plt49 #County Graph 40-49
import matplotlib.pyplot as plt50 #School Graph
import matplotlib.pyplot as plt51 #total data gathered from personal code Graph

val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23,val24,val25,val26,val27,val28,val29,val30, val31,val32,val33,val34,val35,val36,val37,val38,val39, val40,val41,val42,val43,val44,val45,val46,val47,val48,val49  =  [], [], [], [], [], [],[], [], [],[], [], [],[], [], [], [], [], [],[], [], [], [], [],[], [], [],[], [], [],[], [], [], [], [],[],[],[]

switch = {
    1: "Never got sick with no vaccine",
    2: "Never got sick with vaccine",
    3: "Got sick with no vaccine and no hospitalization",
    4: "Got sick with vaccine and no hospitalization",
    5:"Got sick with no vaccine and hospitalization",
    6: "Got sick with vaccine and hospitalization"
    }


############## getSwitch ###########    
def getSwitch(): # for clean output on list
    for a in switch:
        print(f"\t{a}. {switch[a]}")
    return ""
   

error = "\n\nError!!! Your input was incorrect. Try again!\n\n"
again = "\nPlease re-enter your response.\n"

################ sick ############
def sick ():
    totpeople = 0
    totsick = 0
    thirt = 0
    fourt = 0
    fift = 0
    sixt = 0
    sevent = 0
    eight = 0
    nine = 0
    twenty = 0
    twentyone = 0
    twentytwo = 0
    twentythree = 0
    twentyfour = 0
    twentyfive = 0
    twentysix = 0
    twentyseven = 0
    twentyeight = 0
    twentynine = 0
    thirty = 0
    thirtyone = 0
    thirtytwo = 0
    thirtythree = 0
    thirtyfour = 0
    thirtyfive = 0
    thirtysix = 0
    thirtyseven = 0
    thirtyeight = 0
    thirtynine = 0
    fourty = 0
    fourtyone = 0
    fourtytwo = 0
    fourtythree = 0
    fourtyfour = 0
    fourtyfive = 0
    fourtysix = 0
    fourtyseven = 0
    fourtyeight = 0
    fourtynine = 0
    times = 0 # numerator so user can see which question they are answering


    

    # ******************** AGE(Flu) **************
    while(True): # Age
        while(True):
            age = input("What is your age: ")        
            if(age.isnumeric() == True): break
            else:
                print("\nYour input must be numeric (ex. 12). Try again.\n\n")
       
        nage = int(age) # convert age to int type
        if(nage < 13 or nage > 49):
                print(f"\nYou put {age} as you age and must be between 12 and 50." +
                "Please Re-enter.\n\n")
               
        else:
            while(True): # check with user on age
                ans = input(f"\nYou put {age} as your age. Is this " +
                "correct?\n\t1. Yes\n\t2. No\nChoice: ")
                if(ans == "Yes" or ans == "yes" or ans == "no"or ans == "No" or ans == "1" or ans == "2"): break
                else: print(error) ; os.system('clear')
            if(ans == "1"): # fine with the age they entered
                break
            else: print(again)  # print message and allow change to age
           
    totpeople +=1 # total number people that enter data
    if(nage == 13): thirt+=1 #13 counter
    if(nage == 14): fourt+=1
    if(nage == 15): fift+=1
    if(nage == 16): sixt+=1
    if(nage == 17): sevent+=1
    if(nage == 18): eight+=1
    if(nage == 19): nine+=1
    if(nage == 20): twenty+=1
    if(nage == 21): twentyone+=1
    if(nage == 22): twentytwo+=1
    if(nage == 23): twentythree+=1 
    if(nage == 24): twentyfour+=1
    if(nage == 25): twentyfive+=1
    if(nage == 26): twentysix+=1
    if(nage == 27): twentyseven+=1
    if(nage == 28): twentyeight+=1
    if(nage == 29): twentynine+=1
    if(nage == 30): thirty+=1
    if(nage == 31): thirtyone+=1
    if(nage == 32): thirtytwo+=1
    if(nage == 33): thirtythree+=1 
    if(nage == 34): thirtyfour+=1
    if(nage == 35): thirtyfive+=1
    if(nage == 36): thirtysix+=1
    if(nage == 37): thirtyseven+=1
    if(nage == 38): thirtyeight+=1
    if(nage == 39): thirtynine+=1
    if(nage == 40): fourty+=1
    if(nage == 41): fourtyone+=1
    if(nage == 42): fourtytwo+=1
    if(nage == 43): fourtythree+=1 
    if(nage == 44): fourtyfour+=1
    if(nage == 45): fourtyfive+=1
    if(nage == 46): fourtysix+=1
    if(nage == 47): fourtyseven+=1
    if(nage == 48): fourtyeight+=1
    if(nage == 49): fourtynine+=1
            


    while(True): # ************ SICK(FLU) ******************
        os.system('clear')
        while(True):
            while(True):
                sick = input("How many times have you gotten the Flu? (In total): ") # get number of times sick
                if(sick.isnumeric() == True): break
                else:
                    print("\nYour input must be numeric (ex. 12). Try again.\n\n")
       
            ans = input(f"\nYou put {sick} as the number of times you have gotten the Flu . Is this " +
            "correct?\n\t1. Yes\n\t2. No\nChoice: ")
            if(ans == "Yes" or ans == "yes" or ans == "no" or ans == "No" or ans == "1" or ans == "2"): break
            else: print(error)
        if(ans == "1"):
            break
        else: print(again)
               
    sick = int(sick) # int form of numb sick
    totsick+= sick # running total of  cases
     
           
    if(sick == 0): x = 0
    if (sick > 0): x = 1
    while(x <= sick):
        times+=1
        os.system('clear')
        while(True): ################ choice on how got sick (FLU)********************
            while(True): # for numeric
                choice = input(f"{times}. Choose from the following choices:  {getSwitch()}")
                if(choice.isnumeric() == True): break
                else:
                    print("\nYour input must be numeric (ex. 12). Try again.\n\n")
       
            while(True): # for yes, no etc
                ans = input(f"\n{choice}, was your choice. Is this correct?\n\t1. Yes\n\t2. No\nChoice: ")
                if(ans == "Yes" or ans == "yes" or ans == "no" or ans == "No" or ans == "1" or ans == "2"): break
                else: print(error)
            #####>>>>>>>>>>>>>>>>>>>>    
            if(sick == 0 and int(choice) > 3):  ans = 2; print("\nYou said 0 times sick and your choice must be between 1 and 3.\n")
            if(ans == "1"):
                x+=1
                break
            else: print(again)
       
        choice = int(choice)        
   
        # puts the sick value types in io file
        switchA = {
            13: "Thirteen.txt",
            14: "Fourteen.txt",
            15: "Fifteen.txt",
            16: "Sixteen.txt",
            17: "Seventeen.txt",
            18: "Eightteen.txt",
            19: "Nineteen.txt",
            20: "Twenty.txt",
            21: "Twentyone.txt",
            22: "Twentytwo.txt",
            23: "Twentythree.txt",
            24: "Twentyfour.txt",
            25: "Twentyfive.txt",
            26: "Twentysix.txt",
            27: "Twentyseven.txt",
            28: "Twentyeight.txt",
            29: "Twentynine.txt",
            30: "Thirty.txt",
            31: "Thirtyone.txt",
            32: "Thirtytwo.txt",
            33: "Thirtythree.txt",
            34: "Thirtyfour.txt",
            35: "Thirtyfive.txt",
            36: "Thirtysix.txt",
            37: "Thirtyseven.txt",
            38: "Thirtyeight.txt",
            39: "Thirtynine.txt",
            40: "Fourty.txt",
            41: "Fourtyone.txt",
            42: "Fourtytwo.txt",
            43: "Fourtythree.txt",
            44: "Fourtyfour.txt",
            45: "Fourtyfive.txt",
            46: "Fourtysix.txt",
            47: "Fourtyseven.txt",
            48: "Fourtyeight.txt",
            49: "Fourtynine.txt"
                }
        with open(switchA[nage], "a") as l: # Writes the sick info according to age
            l.write(f"{str(choice)}\n")
           


    # ****************** Vaccinated (FLU)**************
    os.system('clear')    
    while(True):
        vacc = input("Have you been vaccinated? (Flu) (Yes or No): ")
        while(True):
            ans = input(f"\n {vacc} , you recieved the vaccine. Is this" +
            " correct\n\t1. Yes\n\t2. No\nChoice: ")
            if(ans == "Yes" or ans == "yes" or ans == "no"or ans == "No" or ans == "1" or ans == "2"): break
            else: print(error)
        if(ans == "1"or ans == "yes"or ans == "Yes"): break
        else: print(again)

######################## MAIN ##################                  
def main():
    firstCheck()  # call to function to see if it needs to create Totals.txt
    # call getTotals first time read and get totals on program start
    totp, tots, thir, four, fif, six, seven, eigh, nin, twent, twentone, twenttwo, twentthree, twentfour, twentfive, twentsix, twentseven, twenteight, twentnine, thirt, thirtone, thirttwo, thirtthree, thirtfour, thirtfive, thirtsix, thirtseven, thirteight, thirtnine, fourt, fourtone, fourttwo, fourtthree, fourtfour, fourtfive, fourtsix, fourtseven, fourteight, fourtnine = getTotals()

    while(True): # Run the program
        os.system('clear')
        ans = int(input("Select:\n\t1. Record Data\n\t2. Print Output\n\t3. Make Graphs\n\t\n\t4. View lists\n\t5. Quit\nChoice: ")) # run the program again
        if(ans == 1):
            os.system('clear')
            totpeople, totsick, thirt, fourt, fift, sixt, sevent, eight , nine, twenty,twentyone,twentytwo, twentythree, twentyfour, twentyfive, twentysix, twentyseven, twentyeight, twentynine, thirty, thirtyone, thirtytwo, thirtythree, thirtyfour, thirtyfive, thirtysix, thirtyseven, thirtyeight, thirtynine, fourty, fourtyone, fourtytwo, fourtythree, fourtyfour, fourtyfive, fourtysix, fourtyseven, fourtyeight, fourtynine=sick() # call to sick
            with open("Totals.txt", "w") as ts:
                ts.write(f"{str(totpeople + totp)}\n{str(totsick + tots)}\n{str(thirt + thir)}\n{str(fourt + four)}\n{str(fift +  fif)}\n{str(sixt + six)}\n{str(sevent +  seven)}\n{str(eight + eigh)}\n{str(nine + nin)}\n{str(twenty + twent)}\n{str(twentyone + twentone)}\n{str(twentytwo + twenttwo)}\n{str(twentythree + twentthree)}\n{str(twentyfour + twentfour)}\n{str(twentyfive +  twentfive)}\n{str(twentysix + twentsix)}\n{str(twentyseven +  twentseven)}\n{str(twentyeight + twenteight)}\n{str(twentynine + twentnine)}\n{str(thirty + thirt)}\n{str(thirtyone + thirtone)}\n{str(thirtytwo + thirttwo)}\n{str(thirtythree + thirtthree)}\n{str(thirtyfour + thirtfour)}\n{str(thirtyfive +  thirtfive)}\n{str(thirtysix + thirtsix)}\n{str(thirtyseven +  thirtseven)}\n{str(thirtyeight + thirteight)}\n{str(thirtynine + thirtnine)}\n{str(fourty + fourt)}\n{str(fourtyone + fourtone)}\n{str(fourtytwo + fourttwo)}\n{str(fourtythree + fourtthree)}\n{str(fourtyfour + fourtfour)}\n{str(fourtyfive +  fourtfive)}\n{str(fourtysix + fourtsix)}\n{str(fourtyseven +  fourtseven)}\n{str(fourtyeight + fourteight)}\n{str(fourtynine + fourtnine)}")
            os.system('clear')
        elif(ans == 2): os.system('clear'); printOutput(); calcValues(ans); answer = input("\n\nHit any key")
        elif(ans == 3): os.system('clear');  makeGraph(ans)
        elif(ans == 4): print(f"Lists\n   {val13}\n{val14}\n{val15}\n{val16}\n{val17}\n{val18}\n{val19}\n{val20}\n{val21}\n{val22}\n{val23}\n{val24}\n{val25}\n{val26}\n{val27}\n{val28}\n{val29}\n{val30}\n{val31}\n{val32}\n{val33}\n{val34}\n{val35}\n{val36}\n{val37}\n{val38}\n{val39}\n{val40}\n{val41}\n{val42}\n{val43}\n{val44}\n{val45}\n{val46}\n{val47}\n{val48}\n{val49}"); an = input("\nHit any key to continue.")
        else: # end running program
            break

########## Get Totals #############
def getTotals(): # read the totals and return as int type
    with open("Totals.txt", "r") as ts:
        data = ts.read()
        totp, tots, thir, four, fif, six, seven, eigh, nin, twent, twentone, twenttwo, twentthree, twentfour, twentfive, twentsix, twentseven, twenteight, twentnine, thirt, thirtone, thirttwo, thirtthree, thirtfour, thirtfive, thirtsix, thirtseven, thirteight, thirtnine, fourt, fourtone, fourttwo, fourtthree, fourtfour, fourtfive, fourtsix, fourtseven, fourteight, fourtnine = data.split()
        totp = int(totp)
        tots = int(tots)
        thir = int(thir)
        four = int(four)
        fif = int(fif)
        six = int(six)
        seven = int(seven)
        eigh = int(eigh)
        nin = int(nin)
        twent = int(twent)
        twentone = int(twentone)
        twenttwo = int(twenttwo)
        twentthree = int(twentthree)
        twentfour = int(twentfour)
        twentfive = int(twentfive)
        twentsix = int(twentsix)
        twentseven = int(twentseven)
        twenteight = int(twenteight)
        twentnine = int(twentnine)
        thirt = int(thirt)
        thirtone = int(thirtone)
        thirttwo = int(thirttwo)
        thirtthree = int(thirtthree)
        thirtfour = int(thirtfour)
        thirtfive = int(thirtfive)
        thirtsix = int(thirtsix)
        thirtseven = int(thirtseven)
        thirteight = int(thirteight)
        thirtnine = int(thirtnine)
        fourt = int(fourt)
        fourtone = int(fourtone)
        fourttwo = int(fourttwo)
        fourtthree = int(fourtthree)
        fourtfour = int(fourtfour)
        fourtfive = int(fourtfive)
        fourtsix = int(fourtsix)
        fourtseven = int(fourtseven)
        fourteight = int(fourteight)
        fourtnine = int(fourtnine)
    return(totp, tots, thir, four, fif, six, seven, eigh, nin, twent, twentone, twenttwo, twentthree, twentfour, twentfive, twentsix, twentseven, twenteight, twentnine, thirt, thirtone, thirttwo, thirtthree, thirtfour, thirtfive, thirtsix, thirtseven, thirteight, thirtnine, fourt, fourtone, fourttwo, fourtthree, fourtfour, fourtfive, fourtsix, fourtseven, fourteight, fourtnine)

################# calcValues #################
val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23,val24,val25,val26,val27,val28,val29,val30, val31,val32,val33,val34,val35,val36,val37,val38,val39, val40,val41,val42,val43,val44,val45,val46,va47,val48,val49  = [], [], [], [], [], [], [], [],[], [], [],[], [], [],[], [], [], [], [], [],[], [], [], [], [],[], [], [],[], [], [],[], [], [], [], [],[]
# calculates the values collected from the people by age group
def calcValues(ans):
    #val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23,val24,val25,val26,val27,val28,val29,val30, val31,val32,val33,val34,val35,val36,val37,val38,val39, val40,val41,val42,val43,val44,val45,val46,val47,val48,val49  = [], [], [], [], [], [], [], [],[], [], [],[], [], [],[], [], [], [], [], [],[], [], [], [], [],[], [], [],[], [], [],[], [], [], [], [],[]
# start by reading data into variables
    switchG = {
            1: ["Thirteen.txt", val13],
            2: ["Fourteen.txt", val14],
            3: ["Fifteen.txt", val15],
            4: ["Sixteen.txt", val16],
            5: ["Seventeen.txt", val17],
            6: ["Eighteen.txt", val18],
            7: ["Nineteen.txt", val19],
            8: ["Twenty.txt", val20],
            9: ["Twentyone.txt", val21],
            10: ["Twentytwo.txt", val22],
            11: ["Twentythree.txt", val23],
            12: ["Twentyfour.txt", val24],
            13: ["Twentyfive.txt", val25],
            14: ["Twentysix.txt", val26],
            15: ["Twentyseven.txt", val27],
            16: ["Twentyeight.txt", val28],
            17: ["Twentynine.txt", val29],
            18: ["Thirty.txt", val30],
            19: ["Thirtyone.txt", val31],
            20: ["Thirtytwo.txt", val32],
            21: ["Thirtythree.txt", val33],
            22: ["Thirtyfour.txt", val34],
            23: ["Thirtyfive.txt", val35],
            24: ["Thirtysix.txt", val36],
            25: ["Thirtyseven.txt", val37],
            26: ["Thirtyeight.txt", val38],
            27: ["Thirtynine.txt", val39],
            28: ["Fourty.txt", val40],
            29: ["Fourtyone.txt", val41],
            30: ["Fourtytwo.txt", val42],
            31: ["Fourtythree.txt", val43],
            32: ["Fourtyfour.txt", val44],
            33: ["Fourtyfive.txt", val45],
            34: ["Fourtysix.txt", val46],
            35: ["Fourtyseven.txt", val47],
            36: ["Fourtyeight.txt", val48],
            37: ["Fourtynine.txt", val49]
                    }
    for x in range(37): # reads data for each age group
        with open(switchG[x+1][0], "r") as f:
            switchG[x+1][1] = f.readlines()
   
    val1a = switchG[1][1] # 13
    for a in val1a:   # eliminate the \n
        val13.append(a.replace("\n", ""))  
    val2a = switchG[2][1] # 14
    for a in val2a:   # eliminate the \n
        val14.append(a.replace("\n", ""))
    val3a = switchG[3][1] # 15
    for a in val3a:   # eliminate the \n
        val15.append(a.replace("\n", ""))
   
    val4a = switchG[4][1] # 16
    for a in val4a:   # eliminate the \n
        val16.append(a.replace("\n", "")) 
    val5a = switchG[5][1] # 17
    for a in val5a:   # eliminate the \n
        val17.append(a.replace("\n", ""))
       
    val6a = switchG[6][1] # 18
    for a in val6a:   # eliminate the \n
        val18.append(a.replace("\n", ""))

    val7a = switchG[7][1] # 19
    for a in val7a:   # eliminate the \n
        val19.append(a.replace("\n", ""))

    val8a = switchG[8][1] # 20
    for a in val8a:   # eliminate the \n
        val20.append(a.replace("\n", ""))

    val9a = switchG[9][1] # 21
    for a in val9a:   # eliminate the \n
        val21.append(a.replace("\n", ""))
    val10a = switchG[10][1] # 22
    for a in val10a:   # eliminate the \n
        val22.append(a.replace("\n", ""))

    val11a = switchG[11][1] # 23
    for a in val11a:   # eliminate the \n
        val23.append(a.replace("\n", ""))

    val12a = switchG[12][1] # 24
    for a in val12a:   # eliminate the \n
        val24.append(a.replace("\n", ""))

    val13a = switchG[13][1] # 25
    for a in val13a:   # eliminate the \n
        val25.append(a.replace("\n", ""))

    val14a = switchG[14][1] # 26
    for a in val14a:   # eliminate the \n
        val26.append(a.replace("\n", ""))

    val15a = switchG[15][1] # 27
    for a in val15a:   # eliminate the \n
        val27.append(a.replace("\n", ""))
    val16a = switchG[16][1] # 28
    for a in val16a:   # eliminate the \n
        val28.append(a.replace("\n", ""))

    val17a = switchG[17][1] # 29
    for a in val17a:   # eliminate the \n
        val29.append(a.replace("\n", ""))

    val18a = switchG[18][1] # 30
    for a in val18a:   # eliminate the \n
        val30.append(a.replace("\n", ""))

    val19a = switchG[19][1] # 31
    for a in val9a:   # eliminate the \n
        val31.append(a.replace("\n", ""))

    val20a = switchG[20][1] # 32
    for a in val20a:   # eliminate the \n
        val32.append(a.replace("\n", ""))

    val21a = switchG[21][1] # 33
    for a in val21a:   # eliminate the \n
        val33.append(a.replace("\n", ""))

    val22a = switchG[22][1] # 34
    for a in val22a:   # eliminate the \n
        val34.append(a.replace("\n", ""))

    val23a = switchG[23][1] # 35
    for a in val23a:   # eliminate the \n
        val35.append(a.replace("\n", ""))

    val24a = switchG[24][1] # 36
    for a in val24a:   # eliminate the \n
        val36.append(a.replace("\n", ""))

    val25a = switchG[25][1] # 37
    for a in val25a:   # eliminate the \n
        val37.append(a.replace("\n", ""))

    val26a = switchG[26][1] # 38
    for a in val26a:   # eliminate the \n
        val38.append(a.replace("\n", ""))

    val27a = switchG[27][1] # 39
    for a in val27a:   # eliminate the \n
        val39.append(a.replace("\n", ""))

    val28a = switchG[28][1] # 40
    for a in val28a:   # eliminate the \n
        val40.append(a.replace("\n", ""))
    val29a = switchG[29][1] # 41
    for a in val29a:   # eliminate the \n
        val41.append(a.replace("\n", ""))

    val30a = switchG[30][1] # 42
    for a in val30a:   # eliminate the \n
        val42.append(a.replace("\n", ""))

    val31a = switchG[31][1] # 43
    for a in val31a:   # eliminate the \n
        val43.append(a.replace("\n", ""))

    val32a = switchG[32][1] # 44
    for a in val32a:   # eliminate the \n
        val44.append(a.replace("\n", ""))

    val33a = switchG[33][1] # 45
    for a in val33a:   # eliminate the \n
        val45.append(a.replace("\n", ""))

    val34a = switchG[34][1] # 46
    for a in val34a:   # eliminate the \n
        val46.append(a.replace("\n", ""))

    val35a = switchG[35][1] # 47
    for a in val35a:   # eliminate the \n
        val47.append(a.replace("\n", ""))

    val36a = switchG[36][1] # 48
    for a in val36a:   # eliminate the \n
        val48.append(a.replace("\n", ""))

    val37a = switchG[37][1] # 49
    for a in val37a:   # eliminate the \n
        val49.append(a.replace("\n", ""))

       
   
    #val13len = len(val13) # length of the list
    # counters for age groups by type of 
    n1_13, n2_13, n3_13, n4_13, n5_13, n6_13 = 0, 0, 0, 0, 0, 0
    for b in val13:
        if b == "1": n1_13 += 1
        elif b == "2": n2_13 += 1
        elif b == "3": n3_13 += 1
        elif b == "4": n4_13 += 1
        elif b == "5": n5_13 += 1
        elif b == "6": n6_13 += 1
       
    n1_14, n2_14, n3_14, n4_14, n5_14, n6_14 = 0, 0, 0, 0, 0, 0
    for b in val14:
        if b == "1": n1_14 += 1
        elif b == "2": n2_14 += 1
        elif b == "3": n3_14 += 1
        elif b == "4": n4_14 += 1
        elif b == "5": n5_14 += 1
        elif b == "6": n6_14 += 1
        
    n1_15, n2_15, n3_15, n4_15, n5_15, n6_15 = 0, 0, 0, 0, 0, 0
    for b in val15:
        if b == "1": n1_15 += 1
        elif b == "2": n2_15 += 1
        elif b == "3": n3_15 += 1
        elif b == "4": n4_15 += 1
        elif b == "5": n5_15 += 1
        elif b == "6": n6_15 += 1

    n1_16, n2_16, n3_16, n4_16, n5_16, n6_16 = 0, 0, 0, 0, 0, 0
    for b in val16:
        if b == "1": n1_16 += 1
        elif b == "2": n2_16 += 1
        elif b == "3": n3_16 += 1
        elif b == "4": n4_16 += 1
        elif b == "5": n5_16 += 1
        elif b == "6": n6_16 += 1
    
    n1_17, n2_17, n3_17, n4_17, n5_17, n6_17 = 0, 0, 0, 0, 0, 0
    for b in val17:
        if b == "1": n1_17 += 1
        elif b == "2": n2_17 += 1
        elif b == "3": n3_17 += 1
        elif b == "4": n4_17 += 1
        elif b == "5": n5_17 += 1
        elif b == "6": n6_17 += 1

    n1_18, n2_18, n3_18, n4_18, n5_18, n6_18 = 0, 0, 0, 0, 0, 0
    for b in val18:
        if b == "1": n1_18 += 1
        elif b == "2": n2_18 += 1
        elif b == "3": n3_18 += 1
        elif b == "4": n4_18 += 1
        elif b == "5": n5_18 += 1
        elif b == "6": n6_18 += 1

    n1_19, n2_19, n3_19, n4_19, n5_19, n6_19 = 0, 0, 0, 0, 0, 0
    for b in val19:
        if b == "1": n1_19 += 1
        elif b == "2": n2_19 += 1
        elif b == "3": n3_19 += 1
        elif b == "4": n4_19 += 1
        elif b == "5": n5_19 += 1
        elif b == "6": n6_19 += 1

    n1_20, n2_20, n3_20, n4_20, n5_20, n6_20 = 0, 0, 0, 0, 0, 0
    for b in val20:
        if b == "1": n1_20 += 1
        elif b == "2": n2_20 += 1
        elif b == "3": n3_20 += 1
        elif b == "4": n4_20 += 1
        elif b == "5": n5_20 += 1
        elif b == "6": n6_20 += 1

    n1_21, n2_21, n3_21, n4_21, n5_21, n6_21 = 0, 0, 0, 0, 0, 0
    for b in val21:
        if b == "1": n1_21 += 1
        elif b == "2": n2_21 += 1
        elif b == "3": n3_21 += 1
        elif b == "4": n4_21 += 1
        elif b == "5": n5_21 += 1
        elif b == "6": n6_21 += 1
        
    n1_22, n2_22, n3_22, n4_22, n5_22, n6_22 = 0, 0, 0, 0, 0, 0
    for b in val22:
        if b == "1": n1_22 += 1
        elif b == "2": n2_22 += 1
        elif b == "3": n3_22 += 1
        elif b == "4": n4_22 += 1
        elif b == "5": n5_22 += 1
        elif b == "6": n6_22 += 1

    n1_23, n2_23, n3_23, n4_23, n5_23, n6_23 = 0, 0, 0, 0, 0, 0
    for b in val23:
        if b == "1": n1_23 += 1
        elif b == "2": n2_23 += 1
        elif b == "3": n3_23 += 1
        elif b == "4": n4_23 += 1
        elif b == "5": n5_23 += 1
        elif b == "6": n6_23 += 1
    
    n1_24, n2_24, n3_24, n4_24, n5_24, n6_24 = 0, 0, 0, 0, 0, 0
    for b in val24:
        if b == "1": n1_24 += 1
        elif b == "2": n2_24 += 1
        elif b == "3": n3_24 += 1
        elif b == "4": n4_24 += 1
        elif b == "5": n5_24 += 1
        elif b == "6": n6_24 += 1

    n1_25, n2_25, n3_25, n4_25, n5_25, n6_25 = 0, 0, 0, 0, 0, 0
    for b in val25:
        if b == "1": n1_25 += 1
        elif b == "2": n2_25 += 1
        elif b == "3": n3_25 += 1
        elif b == "4": n4_25 += 1
        elif b == "5": n5_25 += 1
        elif b == "6": n6_25 += 1

    n1_26, n2_26, n3_26, n4_26, n5_26, n6_26 = 0, 0, 0, 0, 0, 0
    for b in val26:
        if b == "1": n1_26 += 1
        elif b == "2": n2_26 += 1
        elif b == "3": n3_26 += 1
        elif b == "4": n4_26 += 1
        elif b == "5": n5_26 += 1
        elif b == "6": n6_26 += 1

    n1_27, n2_27, n3_27, n4_27, n5_27, n6_27 = 0, 0, 0, 0, 0, 0
    for b in val27:
        if b == "1": n1_27 += 1
        elif b == "2": n2_27 += 1
        elif b == "3": n3_27 += 1
        elif b == "4": n4_27 += 1
        elif b == "5": n5_27 += 1
        elif b == "6": n6_27 += 1

    n1_28, n2_28, n3_28, n4_28, n5_28, n6_28 = 0, 0, 0, 0, 0, 0
    for b in val28:
        if b == "1": n1_28 += 1
        elif b == "2": n2_28 += 1
        elif b == "3": n3_28 += 1
        elif b == "4": n4_28 += 1
        elif b == "5": n5_28 += 1
        elif b == "6": n6_28 += 1

    n1_29, n2_29, n3_29, n4_29, n5_29, n6_29 = 0, 0, 0, 0, 0, 0
    for b in val29:
        if b == "1": n1_29 += 1
        elif b == "2": n2_29 += 1
        elif b == "3": n3_29 += 1
        elif b == "4": n4_29 += 1
        elif b == "5": n5_29 += 1
        elif b == "6": n6_29 += 1

    n1_30, n2_30, n3_30, n4_30, n5_30, n6_30 = 0, 0, 0, 0, 0, 0
    for b in val30:
        if b == "1": n1_30 += 1
        elif b == "2": n2_30 += 1
        elif b == "3": n3_30 += 1
        elif b == "4": n4_30 += 1
        elif b == "5": n5_30 += 1
        elif b == "6": n6_30 += 1

    n1_31, n2_31, n3_31, n4_31, n5_31, n6_31 = 0, 0, 0, 0, 0, 0
    for b in val31:
        if b == "1": n1_31 += 1
        elif b == "2": n2_31 += 1
        elif b == "3": n3_31 += 1
        elif b == "4": n4_31 += 1
        elif b == "5": n5_31 += 1
        elif b == "6": n6_31 += 1

    n1_32, n2_32, n3_32, n4_32, n5_32, n6_32 = 0, 0, 0, 0, 0, 0
    for b in val32:
        if b == "1": n1_32 += 1
        elif b == "2": n2_32 += 1
        elif b == "3": n3_32 += 1
        elif b == "4": n4_32 += 1
        elif b == "5": n5_32 += 1
        elif b == "6": n6_32 += 1

    n1_33, n2_33, n3_33, n4_33, n5_33, n6_33 = 0, 0, 0, 0, 0, 0
    for b in val33:
        if b == "1": n1_33 += 1
        elif b == "2": n2_33 += 1
        elif b == "3": n3_33 += 1
        elif b == "4": n4_33 += 1
        elif b == "5": n5_33 += 1
        elif b == "6": n6_33 += 1

    n1_34, n2_34, n3_34, n4_34, n5_34, n6_34 = 0, 0, 0, 0, 0, 0
    for b in val34:
        if b == "1": n1_34 += 1
        elif b == "2": n2_34 += 1
        elif b == "3": n3_34 += 1
        elif b == "4": n4_34 += 1
        elif b == "5": n5_34 += 1
        elif b == "6": n6_34 += 1

    n1_35, n2_35, n3_35, n4_35, n5_35, n6_35 = 0, 0, 0, 0, 0, 0
    for b in val35:
        if b == "1": n1_35 += 1
        elif b == "2": n2_35 += 1
        elif b == "3": n3_35 += 1
        elif b == "4": n4_35 += 1
        elif b == "5": n5_35 += 1
        elif b == "6": n6_35 += 1

    n1_36, n2_36, n3_36, n4_36, n5_36, n6_36 = 0, 0, 0, 0, 0, 0
    for b in val36:
        if b == "1": n1_36 += 1
        elif b == "2": n2_36 += 1
        elif b == "3": n3_36 += 1
        elif b == "4": n4_36 += 1
        elif b == "5": n5_36 += 1
        elif b == "6": n6_36 += 1

    n1_37, n2_37, n3_37, n4_37, n5_37, n6_37 = 0, 0, 0, 0, 0, 0
    for b in val37:
        if b == "1": n1_37 += 1
        elif b == "2": n2_37 += 1
        elif b == "3": n3_37 += 1
        elif b == "4": n4_37 += 1
        elif b == "5": n5_37 += 1
        elif b == "6": n6_37 += 1

    n1_38, n2_38, n3_38, n4_38, n5_38, n6_38 = 0, 0, 0, 0, 0, 0
    for b in val38:
        if b == "1": n1_38 += 1
        elif b == "2": n2_38 += 1
        elif b == "3": n3_38 += 1
        elif b == "4": n4_38 += 1
        elif b == "5": n5_38 += 1
        elif b == "6": n6_38 += 1

    n1_39, n2_39, n3_39, n4_39, n5_39, n6_39 = 0, 0, 0, 0, 0, 0
    for b in val39:
        if b == "1": n1_39 += 1
        elif b == "2": n2_39 += 1
        elif b == "3": n3_39 += 1
        elif b == "4": n4_39 += 1
        elif b == "5": n5_39 += 1
        elif b == "6": n6_39 += 1

    n1_40, n2_40, n3_40, n4_40, n5_40, n6_40 = 0, 0, 0, 0, 0, 0
    for b in val40:
        if b == "1": n1_40 += 1
        elif b == "2": n2_40 += 1
        elif b == "3": n3_40 += 1
        elif b == "4": n4_40 += 1
        elif b == "5": n5_40 += 1
        elif b == "6": n6_40 += 1


    n1_41, n2_41, n3_41, n4_41, n5_41, n6_41 = 0, 0, 0, 0, 0, 0
    for b in val41:
        if b == "1": n1_41 += 1
        elif b == "2": n2_41 += 1
        elif b == "3": n3_41 += 1
        elif b == "4": n4_41 += 1
        elif b == "5": n5_41 += 1
        elif b == "6": n6_41 += 1

    n1_42, n2_42, n3_42, n4_42, n5_42, n6_42 = 0, 0, 0, 0, 0, 0
    for b in val42:
        if b == "1": n1_42 += 1
        elif b == "2": n2_42 += 1
        elif b == "3": n3_42 += 1
        elif b == "4": n4_42 += 1
        elif b == "5": n5_42 += 1
        elif b == "6": n6_42 += 1

    n1_43, n2_43, n3_43, n4_43, n5_43, n6_43 = 0, 0, 0, 0, 0, 0
    for b in val43:
        if b == "1": n1_43 += 1
        elif b == "2": n2_43 += 1
        elif b == "3": n3_43 += 1
        elif b == "4": n4_43 += 1
        elif b == "5": n5_43 += 1
        elif b == "6": n6_43 += 1

    n1_44, n2_44, n3_44, n4_44, n5_44, n6_44 = 0, 0, 0, 0, 0, 0
    for b in val44:
        if b == "1": n1_44 += 1
        elif b == "2": n2_44 += 1
        elif b == "3": n3_44 += 1
        elif b == "4": n4_44 += 1
        elif b == "5": n5_44 += 1
        elif b == "6": n6_44 += 1

    n1_45, n2_45, n3_45, n4_45, n5_45, n6_45 = 0, 0, 0, 0, 0, 0
    for b in val45:
        if b == "1": n1_45 += 1
        elif b == "2": n2_45 += 1
        elif b == "3": n3_45 += 1
        elif b == "4": n4_45 += 1
        elif b == "5": n5_45 += 1
        elif b == "6": n6_45 += 1

    n1_46, n2_46, n3_46, n4_46, n5_46, n6_46 = 0, 0, 0, 0, 0, 0
    for b in val46:
        if b == "1": n1_46 += 1
        elif b == "2": n2_46 += 1
        elif b == "3": n3_46 += 1
        elif b == "4": n4_46 += 1
        elif b == "5": n5_46 += 1
        elif b == "6": n6_46 += 1

    n1_47, n2_47, n3_47, n4_47, n5_47, n6_47 = 0, 0, 0, 0, 0, 0
    for b in val47:
        if b == "1": n1_47 += 1
        elif b == "2": n2_47 += 1
        elif b == "3": n3_47 += 1
        elif b == "4": n4_47 += 1
        elif b == "5": n5_47 += 1
        elif b == "6": n6_47 += 1

    n1_48, n2_48, n3_48, n4_48, n5_48, n6_48 = 0, 0, 0, 0, 0, 0
    for b in val48:
        if b == "1": n1_48 += 1
        elif b == "2": n2_48 += 1
        elif b == "3": n3_48 += 1
        elif b == "4": n4_48 += 1
        elif b == "5": n5_48 += 1
        elif b == "6": n6_48 += 1

    n1_49, n2_49, n3_49, n4_49, n5_49, n6_49 = 0, 0, 0, 0, 0, 0
    for b in val49:
        if b == "1": n1_49 += 1
        elif b == "2": n2_49 += 1
        elif b == "3": n3_49 += 1
        elif b == "4": n4_49 += 1
        elif b == "5": n5_49 += 1
        elif b == "6": n6_49 += 1


 
    if(ans==2): printValues(n1_13, n2_13, n3_13, n4_13, n5_13, n6_13, n1_14, n2_14, n3_14, n4_14, n5_14, n6_14, n1_15, n2_15, n3_15, n4_15, n5_15, n6_15, n1_16, n2_16, n3_16, n4_16, n5_16, n6_16, n1_17, n2_17, n3_17, n4_17, n5_17, n6_17, n1_18, n2_18, n3_18, n4_18, n5_18, n6_18, n1_19, n2_19, n3_19, n4_19, n5_19, n6_19, n1_20, n2_20, n3_20, n4_20, n5_20, n6_20, n1_21, n2_21, n3_21, n4_21, n5_21, n6_21, n1_22, n2_22, n3_22, n4_22, n5_22, n6_22, n1_23, n2_23, n3_23, n4_23, n5_23, n6_23, n1_24, n2_24, n3_24, n4_24, n5_24, n6_24, n1_25, n2_25, n3_25, n4_25, n5_25, n6_25, n1_26, n2_26, n3_26, n4_26, n5_26, n6_26, n1_27, n2_27, n3_27, n4_27, n5_27, n6_27, n1_28, n2_28, n3_28, n4_28, n5_28, n6_28, n1_29, n2_29, n3_29, n4_29, n5_29, n6_29, n1_30, n2_30, n3_30, n4_30, n5_30, n6_30, n1_31, n2_31, n3_31, n4_31, n5_31, n6_31, n1_32, n2_32, n3_32, n4_32, n5_32, n6_32, n1_33, n2_33, n3_33, n4_33, n5_33, n6_33, n1_34, n2_34, n3_34, n4_34, n5_34, n6_34, n1_35, n2_35, n3_35, n4_35, n5_35, n6_35, n1_36, n2_36, n3_36, n4_36, n5_36, n6_36, n1_37, n2_37, n3_37, n4_37, n5_37, n6_37, n1_38, n2_38, n3_38, n4_38, n5_38, n6_38, n1_39, n2_39, n3_39, n4_39, n5_39, n6_39, n1_40, n2_40, n3_40, n4_40, n5_40, n6_40, n1_41, n2_41, n3_41, n4_41, n5_41, n6_41, n1_42, n2_42, n3_42, n4_42, n5_42, n6_42, n1_43, n2_43, n3_43, n4_43, n5_43, n6_43, n1_44, n2_44, n3_44, n4_44, n5_44, n6_44, n1_45, n2_45, n3_45, n4_45, n5_45, n6_45, n1_46, n2_46, n3_46, n4_46, n5_46, n6_46, n1_47, n2_47, n3_47, n4_47, n5_47, n6_47, n1_48, n2_48, n3_48, n4_48, n5_48, n6_48, n1_49, n2_49, n3_49, n4_49, n5_49, n6_49)
    
    if(ans==3): return(n1_13, n2_13, n3_13, n4_13, n5_13, n6_13, n1_14, n2_14, n3_14, n4_14, n5_14, n6_14, n1_15, n2_15, n3_15, n4_15, n5_15, n6_15, n1_16, n2_16, n3_16, n4_16, n5_16, n6_16, n1_17, n2_17, n3_17, n4_17, n5_17, n6_17, n1_18, n2_18, n3_18, n4_18, n5_18, n6_18, n1_19, n2_19, n3_19, n4_19, n5_19, n6_19, n1_20, n2_20, n3_20, n4_20, n5_20, n6_20, n1_21, n2_21, n3_21, n4_21, n5_21, n6_21, n1_22, n2_22, n3_22, n4_22, n5_22, n6_22, n1_23, n2_23, n3_23, n4_23, n5_23, n6_23, n1_24, n2_24, n3_24, n4_24, n5_24, n6_24, n1_25, n2_25, n3_25, n4_25, n5_25, n6_25, n1_26, n2_26, n3_26, n4_26, n5_26, n6_26, n1_27, n2_27, n3_27, n4_27, n5_27, n6_27, n1_28, n2_28, n3_28, n4_28, n5_28, n6_28, n1_29, n2_29, n3_29, n4_29, n5_29, n6_29, n1_30, n2_30, n3_30, n4_30, n5_30, n6_30, n1_31, n2_31, n3_31, n4_31, n5_31, n6_31, n1_32, n2_32, n3_32, n4_32, n5_32, n6_32, n1_33, n2_33, n3_33, n4_33, n5_33, n6_33, n1_34, n2_34, n3_34, n4_34, n5_34, n6_34, n1_35, n2_35, n3_35, n4_35, n5_35, n6_35, n1_36, n2_36, n3_36, n4_36, n5_36, n6_36, n1_37, n2_37, n3_37, n4_37, n5_37, n6_37, n1_38, n2_38, n3_38, n4_38, n5_38, n6_38, n1_39, n2_39, n3_39, n4_39, n5_39, n6_39, n1_40, n2_40, n3_40, n4_40, n5_40, n6_40, n1_41, n2_41, n3_41, n4_41, n5_41, n6_41, n1_42, n2_42, n3_42, n4_42, n5_42, n6_42, n1_43, n2_43, n3_43, n4_43, n5_43, n6_43, n1_44, n2_44, n3_44, n4_44, n5_44, n6_44, n1_45, n2_45, n3_45, n4_45, n5_45, n6_45, n1_46, n2_46, n3_46, n4_46, n5_46, n6_46, n1_47, n2_47, n3_47, n4_47, n5_47, n6_47, n1_48, n2_48, n3_48, n4_48, n5_48, n6_48, n1_49, n2_49, n3_49, n4_49, n5_49, n6_49)
    ################3
def printValues(n1_13, n2_13, n3_13, n4_13, n5_13, n6_13, n1_14, n2_14, n3_14, n4_14, n5_14, n6_14, n1_15, n2_15, n3_15, n4_15, n5_15, n6_15, n1_16, n2_16, n3_16, n4_16, n5_16, n6_16, n1_17, n2_17, n3_17, n4_17, n5_17, n6_17, n1_18, n2_18, n3_18, n4_18, n5_18, n6_18, n1_19, n2_19, n3_19, n4_19, n5_19, n6_19, n1_20, n2_20, n3_20, n4_20, n5_20, n6_20, n1_21, n2_21, n3_21, n4_21, n5_21, n6_21, n1_22, n2_22, n3_22, n4_22, n5_22, n6_22, n1_23, n2_23, n3_23, n4_23, n5_23, n6_23, n1_24, n2_24, n3_24, n4_24, n5_24, n6_24, n1_25, n2_25, n3_25, n4_25, n5_25, n6_25, n1_26, n2_26, n3_26, n4_26, n5_26, n6_26, n1_27, n2_27, n3_27, n4_27, n5_27, n6_27, n1_28, n2_28, n3_28, n4_28, n5_28, n6_28, n1_29, n2_29, n3_29, n4_29, n5_29, n6_29, n1_30, n2_30, n3_30, n4_30, n5_30, n6_30, n1_31, n2_31, n3_31, n4_31, n5_31, n6_31, n1_32, n2_32, n3_32, n4_32, n5_32, n6_32, n1_33, n2_33, n3_33, n4_33, n5_33, n6_33, n1_34, n2_34, n3_34, n4_34, n5_34, n6_34, n1_35, n2_35, n3_35, n4_35, n5_35, n6_35, n1_36, n2_36, n3_36, n4_36, n5_36, n6_36, n1_37, n2_37, n3_37, n4_37, n5_37, n6_37, n1_38, n2_38, n3_38, n4_38, n5_38, n6_38, n1_39, n2_39, n3_39, n4_39, n5_39, n6_39, n1_40, n2_40, n3_40, n4_40, n5_40, n6_40, n1_41, n2_41, n3_41, n4_41, n5_41, n6_41, n1_42, n2_42, n3_42, n4_42, n5_42, n6_42, n1_43, n2_43, n3_43, n4_43, n5_43, n6_43, n1_44, n2_44, n3_44, n4_44, n5_44, n6_44, n1_45, n2_45, n3_45, n4_45, n5_45, n6_45, n1_46, n2_46, n3_46, n4_46, n5_46, n6_46, n1_47, n2_47, n3_47, n4_47, n5_47, n6_47, n1_48, n2_48, n3_48, n4_48, n5_48, n6_48, n1_49, n2_49, n3_49, n4_49, n5_49, n6_49):
    print("\n\nFlu Results By Age Group\n")
    print(f"Thirteen Year Olds:\n1. {switch[1]} - {n1_13}\n2. {switch[2]} - {n2_13}\n3. {switch[3]} - {n3_13}\n4. {switch[4]} - {n4_13}\n5. {switch[5]} - {n5_13}\n6. {switch[6]} - {n6_13}\n")#7. {switch[7]} - {n7_13}\n8. {switch[8]} - {n8_13}\n9. {switch[9]} - {n9_13}\n")#10. {switch[10]} - {n10_13}\n11. {switch[11]} - {n11_13}\n12. {switch[12]} - {n12_13}\n13. {switch[13]} - {n13_13}\n14. {switch[14]} - {n14_13}\n15. {switch[15]} - {n15_13}\n16. {switch[16]} - {n16_13}\n17. {switch[17]} - {n17_13}\n18. {switch[18]} - {n18_13}\n19. {switch[19]} - {n19_13}\n20. {switch[20]} - {n20_13}\n21. {switch[21]} - {n21_13}\n22. {switch[22]} - {n22_13}\n23. {switch[23]} - {n23_13}\n24. {switch[24]} - {n24_13}\n25. {switch[25]} - {n25_13}\n26. {switch[26]} - {n26_13}\n27. {switch[27]} - {n27_13}\n28. {switch[28]} - {n28_13}\n29. {switch[29]} - {n29_13}\n30. {switch[30]} - {n30_13}\n31. {switch[31]} - {n31_13}\n32. {switch[32]} - {n32_13}\n33. {switch[33]} - {n33_13}\n34. {switch[34]} - {n34_13}\n35. {switch[35]} - {n35_13}\n36. {switch[36]} - {n36_13}\n37. {switch[37]} - {n37_13}")
    print(f"Fourteen Year Olds:\n1. {switch[1]} - {n1_14}\n2. {switch[2]} - {n2_14}\n3. {switch[3]} - {n3_14}\n4. {switch[4]} - {n4_14}\n5. {switch[5]} - {n5_14}\n6. {switch[6]} - {n6_14}\n")#7. {switch[7]} - {n7_14}\n8. {switch[8]} - {n8_14}\n9. {switch[9]} - {n9_14}\n")#10. {switch[10]} - {n10_14}\n11. {switch[11]} - {n11_14}\n12. {switch[12]} - {n12_14}\n13. {switch[13]} - {n13_14}\n14. {switch[14]} - {n14_14}\n15. {switch[15]} - {n15_14}\n16. {switch[16]} - {n16_14}\n17. {switch[17]} - {n17_14}\n18. {switch[18]} - {n18_14}\n19. {switch[19]} - {n19_14}\n20. {switch[20]} - {n20_14}\n21. {switch[21]} - {n21_14}\n22. {switch[22]} - {n22_14}\n23. {switch[23]} - {n23_14}\n24. {switch[24]} - {n24_14}\n25. {switch[25]} - {n25_14}\n26. {switch[26]} - {n26_14}\n27. {switch[27]} - {n27_14}\n28. {switch[28]} - {n28_14}\n29. {switch[29]} - {n29_14}\n30. {switch[30]} - {n30_14}\n31. {switch[31]} - {n31_14}\n32. {switch[32]} - {n32_14}\n33. {switch[33]} - {n33_14}\n34. {switch[34]} - {n34_14}\n35. {switch[35]} - {n35_14}\n36. {switch[36]} - {n36_14}\n37. {switch[37]} - {n37_14}")
    print(f"Fifteen Year Olds:\n1. {switch[1]} - {n1_15}\n2. {switch[2]} - {n2_15}\n3. {switch[3]} - {n3_15}\n4. {switch[4]} - {n4_15}\n5. {switch[5]} - {n5_15}\n6. {switch[6]} - {n6_15}\n")#7. {switch[7]} - {n7_15}\n8. {switch[8]} - {n8_15}\n9. {switch[9]} - {n9_15}\n")#10.{switch[10]} - {n10_15}\n11. {switch[11]} - {n11_15}\n12. {switch[12]} - {n12_15}\n13. {switch[13]} - {n13_15}\n14. {switch[14]} - {n14_15}\n15. {switch[15]} - {n15_15}\n16. {switch[16]} - {n16_15}\n17. {switch[17]} - {n17_15}\n18. {switch[18]} - {n18_15}\n19. {switch[19]} - {n19_15}\n20. {switch[20]} - {n20_15}\n21. {switch[21]} - {n21_15}\n22. {switch[22]} - {n22_15}\n23. {switch[23]} - {n23_15}\n24. {switch[24]} - {n24_15}\n25. {switch[25]} - {n25_15}\n26. {switch[26]} - {n26_15}\n27. {switch[27]} - {n27_15}\n28. {switch[28]} - {n28_15}\n29. {switch[29]} - {n29_15}\n30. {switch[30]} - {n30_15}\n31. {switch[31]} - {n31_15}\n32. {switch[32]} - {n32_15}\n33. {switch[33]} - {n33_15}\n34. {switch[34]} - {n34_15}\n35. {switch[35]} - {n35_15}\n36. {switch[36]} - {n36_15}\n37. {switch[37]} - {n37_15}")
    print(f"Sixteen Year Olds:\n1. {switch[1]} - {n1_16}\n2. {switch[2]} - {n2_16}\n3. {switch[3]} - {n3_16}\n4. {switch[4]} - {n4_16}\n5. {switch[5]} - {n5_16}\n6. {switch[6]} - {n6_16}\n")#7. {switch[7]} - {n7_16}\n8. {switch[8]} - {n8_16}\n9. {switch[9]} - {n9_16}\n")#10.{switch[10]} - {n10_16}\n11. {switch[11]} - {n11_16}\n12. {switch[12]} - {n12_16}\n13. {switch[13]} - {n13_16}\n14. {switch[14]} - {n14_16}\n15. {switch[15]} - {n15_16}\n16. {switch[16]} - {n16_16}\n17. {switch[17]} - {n17_16}\n18. {switch[18]} - {n18_16}\n19. {switch[19]} - {n19_16}\n20. {switch[20]} - {n20_16}\n21. {switch[21]} - {n21_16}\n22. {switch[22]} - {n22_16}\n23. {switch[23]} - {n23_16}\n24. {switch[24]} - {n24_16}\n25. {switch[25]} - {n25_16}\n26. {switch[26]} - {n26_16}\n27. {switch[27]} - {n27_16}\n28. {switch[28]} - {n28_16}\n29. {switch[29]} - {n29_16}\n30. {switch[30]} - {n30_16}\n31. {switch[31]} - {n31_16}\n32. {switch[32]} - {n32_16}\n33. {switch[33]} - {n33_16}\n34. {switch[34]} - {n34_16}\n35. {switch[35]} - {n35_16}\n36. {switch[36]} - {n36_16}\n37. {switch[37]} - {n37_16}")
    print(f"Seventeen Year Olds:\n1. {switch[1]} - {n1_17}\n2. {switch[2]} - {n2_17}\n3. {switch[3]} - {n3_17}\n4. {switch[4]} - {n4_17}\n5. {switch[5]} - {n5_17}\n6. {switch[6]} - {n6_17}\n")#7. {switch[7]} - {n7_17}\n8. {switch[8]} - {n8_17}\n9. {switch[9]} - {n9_17}\n")#10. {switch[10]} - {n10_17}\n11. {switch[11]} - {n11_17}\n12. {switch[12]} - {n12_17}\n13. {switch[13]} - {n13_17}\n14. {switch[14]} - {n14_17}\n15. {switch[15]} - {n15_17}\n16. {switch[16]} - {n16_17}\n17. {switch[17]} - {n17_17}\n18. {switch[18]} - {n18_17}\n19. {switch[19]} - {n19_17}\n20. {switch[20]} - {n20_17}\n21. {switch[21]} - {n21_17}\n22. {switch[22]} - {n22_17}\n23. {switch[23]} - {n23_17}\n24. {switch[24]} - {n24_17}\n25. {switch[25]} - {n25_17}\n26. {switch[26]} - {n26_17}\n27. {switch[27]} - {n27_17}\n28. {switch[28]} - {n28_17}\n29. {switch[29]} - {n29_17}\n30. {switch[30]} - {n30_17}\n31. {switch[31]} - {n31_17}\n32. {switch[32]} - {n32_17}\n33. {switch[33]} - {n33_17}\n34. {switch[34]} - {n34_17}\n35. {switch[35]} - {n35_17}\n36. {switch[36]} - {n36_17}\n37. {switch[37]} - {n37_17}")
    print(f"Eighteen Year Olds:\n1. {switch[1]} - {n1_18}\n2. {switch[2]} - {n2_18}\n3. {switch[3]} - {n3_18}\n4. {switch[4]} - {n4_18}\n5. {switch[5]} - {n5_18}\n6. {switch[6]} - {n6_18}\n")#7. {switch[7]} - {n7_18}\n8. {switch[8]} - {n8_18}\n9. {switch[9]} - {n9_18}\n")#10.{switch[10]} - {n10_18}\n11. {switch[11]} - {n11_18}\n12. {switch[12]} - {n12_18}\n13. {switch[13]} - {n13_18}\n14. {switch[14]} - {n14_18}\n15. {switch[15]} - {n15_18}\n16. {switch[16]} - {n16_18}\n17. {switch[17]} - {n17_18}\n18. {switch[18]} - {n18_18}\n19. {switch[19]} - {n19_18}\n20. {switch[20]} - {n20_18}\n21. {switch[21]} - {n21_18}\n22. {switch[22]} - {n22_18}\n23. {switch[23]} - {n23_18}\n24. {switch[24]} - {n24_18}\n25. {switch[25]} - {n25_18}\n26. {switch[26]} - {n26_18}\n27. {switch[27]} - {n27_18}\n28. {switch[28]} - {n28_18}\n29. {switch[29]} - {n29_18}\n30. {switch[30]} - {n30_18}\n31. {switch[31]} - {n31_18}\n32. {switch[32]} - {n32_18}\n33. {switch[33]} - {n33_18}\n34. {switch[34]} - {n34_18}\n35. {switch[35]} - {n35_18}\n36. {switch[36]} - {n36_18}\n37. {switch[37]} - {n37_18}")
    print(f"Nineteen Year Olds:\n1. {switch[1]} - {n1_19}\n2. {switch[2]} - {n2_19}\n3. {switch[3]} - {n3_19}\n4. {switch[4]} - {n4_19}\n5. {switch[5]} - {n5_19}\n6. {switch[6]} - {n6_19}\n")#7. {switch[7]} - {n7_19}\n8. {switch[8]} - {n8_19}\n9. {switch[9]} - {n9_19}\n")#10.{switch[10]} - {n10_19}\n11. {switch[11]} - {n11_19}\n12. {switch[12]} - {n12_19}\n13. {switch[13]} - {n13_19}\n14. {switch[14]} - {n14_19}\n15. {switch[15]} - {n15_19}\n16. {switch[16]} - {n16_19}\n17. {switch[17]} - {n17_19}\n18. {switch[18]} - {n18_19}\n19. {switch[19]} - {n19_19}\n20. {switch[20]} - {n20_19}\n21. {switch[21]} - {n21_19}\n22. {switch[22]} - {n22_19}\n23. {switch[23]} - {n23_19}\n24. {switch[24]} - {n24_19}\n25. {switch[25]} - {n25_19}\n26. {switch[26]} - {n26_19}\n27. {switch[27]} - {n27_19}\n28. {switch[28]} - {n28_19}\n29. {switch[29]} - {n29_19}\n30. {switch[30]} - {n30_19}\n31. {switch[31]} - {n31_19}\n32. {switch[32]} - {n32_19}\n33. {switch[33]} - {n33_19}\n34. {switch[34]} - {n34_19}\n35. {switch[35]} - {n35_19}\n36. {switch[36]} - {n36_19}\n37. {switch[37]} - {n37_19}")
    print(f"Twenty Year Olds:\n1. {switch[1]} - {n1_20}\n2. {switch[2]} - {n2_20}\n3. {switch[3]} - {n3_20}\n4. {switch[4]} - {n4_20}\n5. {switch[5]} - {n5_20}\n6. {switch[6]} - {n6_20}\n")#7. {switch[7]} - {n7_20}\n8. {switch[8]} - {n8_20}\n9. {switch[9]} - {n9_20}\n")#10.{switch[10]} - {n10_20}\n11. {switch[11]} - {n11_20}\n12. {switch[12]} - {n12_20}\n13. {switch[13]} - {n13_20}\n14. {switch[14]} - {n14_20}\n15. {switch[15]} - {n15_20}\n16. {switch[16]} - {n16_20}\n17. {switch[17]} - {n17_20}\n18. {switch[18]} - {n18_20}\n19. {switch[19]} - {n19_20}\n20. {switch[20]} - {n20_20}\n21. {switch[21]} - {n21_20}\n22. {switch[22]} - {n22_20}\n23. {switch[23]} - {n23_20}\n24. {switch[24]} - {n24_20}\n25. {switch[25]} - {n25_20}\n26. {switch[26]} - {n26_20}\n27. {switch[27]} - {n27_20}\n28. {switch[28]} - {n28_20}\n29. {switch[29]} - {n29_20}\n30. {switch[30]} - {n30_20}\n31. {switch[31]} - {n31_20}\n32. {switch[32]} - {n32_20}\n33. {switch[33]} - {n33_20}\n34. {switch[34]} - {n34_20}\n35. {switch[35]} - {n35_20}\n36. {switch[36]} - {n36_20}\n37. {switch[37]} - {n37_20}")
    print(f"Twenty-one Year Olds:\n1. {switch[1]} - {n1_21}\n2. {switch[2]} - {n2_21}\n3. {switch[3]} - {n3_21}\n4. {switch[4]} - {n4_21}\n5. {switch[5]} - {n5_21}\n6. {switch[6]} - {n6_21}\n")#7. {switch[7]} - {n7_21}\n8. {switch[8]} - {n8_21}\n9. {switch[9]} - {n9_21}\n")#10.{switch[10]} - {n10_21}\n11. {switch[11]} - {n11_21}\n12. {switch[12]} - {n12_21}\n13. {switch[13]} - {n13_21}\n14. {switch[14]} - {n14_21}\n15. {switch[15]} - {n15_21}\n16. {switch[16]} - {n16_21}\n17. {switch[17]} - {n17_21}\n18. {switch[18]} - {n18_21}\n19. {switch[19]} - {n19_21}\n20. {switch[20]} - {n20_21}\n21. {switch[21]} - {n21_21}\n22. {switch[22]} - {n22_21}\n23. {switch[23]} - {n23_21}\n24. {switch[24]} - {n24_21}\n25. {switch[25]} - {n25_21}\n26. {switch[26]} - {n26_21}\n27. {switch[27]} - {n27_21}\n28. {switch[28]} - {n28_21}\n29. {switch[29]} - {n29_21}\n30. {switch[30]} - {n30_21}\n31. {switch[31]} - {n31_21}\n32. {switch[32]} - {n32_21}\n33. {switch[33]} - {n33_21}\n34. {switch[34]} - {n34_21}\n35. {switch[35]} - {n35_21}\n36. {switch[36]} - {n36_21}\n37. {switch[37]} - {n37_21}")
    print(f"Twenty-two  Year Olds:\n1. {switch[1]} - {n1_22}\n2. {switch[2]} - {n2_22}\n3. {switch[3]} - {n3_22}\n4. {switch[4]} - {n4_22}\n5. {switch[5]} - {n5_22}\n6. {switch[6]} - {n6_22}\n")#7. {switch[7]} - {n7_22}\n8. {switch[8]} - {n8_22}\n9. {switch[9]} - {n9_22}\n")#10.{switch[10]} - {n10_22}\n11. {switch[11]} - {n11_22}\n12. {switch[12]} - {n12_22}\n13. {switch[13]} - {n13_22}\n14. {switch[14]} - {n14_22}\n15. {switch[15]} - {n15_22}\n16. {switch[16]} - {n16_22}\n17. {switch[17]} - {n17_22}\n18. {switch[18]} - {n18_22}\n19. {switch[19]} - {n19_22}\n20. {switch[20]} - {n20_22}\n21. {switch[21]} - {n21_22}\n22. {switch[22]} - {n22_22}\n23. {switch[23]} - {n23_22}\n24. {switch[24]} - {n24_22}\n25. {switch[25]} - {n25_22}\n26. {switch[26]} - {n26_22}\n27. {switch[27]} - {n27_22}\n28. {switch[28]} - {n28_22}\n29. {switch[29]} - {n29_22}\n30. {switch[30]} - {n30_22}\n31. {switch[31]} - {n31_22}\n32. {switch[32]} - {n32_22}\n33. {switch[33]} - {n33_22}\n34. {switch[34]} - {n34_22}\n35. {switch[35]} - {n35_22}\n36. {switch[36]} - {n36_22}\n37. {switch[37]} - {n37_22}")
    print(f"Twenty-three Year Olds:\n1. {switch[1]} - {n1_23}\n2. {switch[2]} - {n2_23}\n3. {switch[3]} - {n3_23}\n4. {switch[4]} - {n4_23}\n5. {switch[5]} - {n5_23}\n6. {switch[6]} - {n6_23}\n")#7. {switch[7]} - {n7_23}\n8. {switch[8]} - {n8_23}\n9. {switch[9]} - {n9_23}\n")#10.{switch[10]} - {n10_23}\n11. {switch[11]} - {n11_23}\n12. {switch[12]} - {n12_23}\n13. {switch[13]} - {n13_23}\n14. {switch[14]} - {n14_23}\n15. {switch[15]} - {n15_23}\n16. {switch[16]} - {n16_23}\n17. {switch[17]} - {n17_23}\n18. {switch[18]} - {n18_23}\n19. {switch[19]} - {n19_23}\n20. {switch[20]} - {n20_23}\n21. {switch[21]} - {n21_23}\n22. {switch[22]} - {n22_23}\n23. {switch[23]} - {n23_23}\n24. {switch[24]} - {n24_23}\n25. {switch[25]} - {n25_23}\n26. {switch[26]} - {n26_23}\n27. {switch[27]} - {n27_23}\n28. {switch[28]} - {n28_23}\n29. {switch[29]} - {n29_23}\n30. {switch[30]} - {n30_23}\n31. {switch[31]} - {n31_23}\n32. {switch[32]} - {n32_23}\n33. {switch[33]} - {n33_23}\n34. {switch[34]} - {n34_23}\n35. {switch[35]} - {n35_23}\n36. {switch[36]} - {n36_23}\n37. {switch[37]} - {n37_23}")
    print(f"Twenty-four Year Olds:\n1. {switch[1]} - {n1_24}\n2. {switch[2]} - {n2_24}\n3. {switch[3]} - {n3_24}\n4. {switch[4]} - {n4_24}\n5. {switch[5]} - {n5_24}\n6. {switch[6]} - {n6_24}\n")#7. {switch[7]} - {n7_24}\n8. {switch[8]} - {n8_24}\n9. {switch[9]} - {n9_24}\n")#10.{switch[10]} - {n10_24}\n11. {switch[11]} - {n11_24}\n12. {switch[12]} - {n12_24}\n13. {switch[13]} - {n13_24}\n14. {switch[14]} - {n14_24}\n15. {switch[15]} - {n15_24}\n16. {switch[16]} - {n16_24}\n17. {switch[17]} - {n17_24}\n18. {switch[18]} - {n18_24}\n19. {switch[19]} - {n19_24}\n20. {switch[20]} - {n20_24}\n21. {switch[21]} - {n21_24}\n22. {switch[22]} - {n22_24}\n23. {switch[23]} - {n23_24}\n24. {switch[24]} - {n24_24}\n25. {switch[25]} - {n25_24}\n26. {switch[26]} - {n26_24}\n27. {switch[27]} - {n27_24}\n28. {switch[28]} - {n28_24}\n29. {switch[29]} - {n29_24}\n30. {switch[30]} - {n30_24}\n31. {switch[31]} - {n31_24}\n32. {switch[32]} - {n32_24}\n33. {switch[33]} - {n33_24}\n34. {switch[34]} - {n34_24}\n35. {switch[35]} - {n35_24}\n36. {switch[36]} - {n36_24}\n37. {switch[37]} - {n37_24}")
    print(f"Twenty-five Year Olds:\n1. {switch[1]} - {n1_25}\n2. {switch[2]} - {n2_25}\n3. {switch[3]} - {n3_25}\n4. {switch[4]} - {n4_25}\n5. {switch[5]} - {n5_25}\n6. {switch[6]} - {n6_25}\n")#7. {switch[7]} - {n7_25}\n8. {switch[8]} - {n8_25}\n9. {switch[9]} - {n9_25}\n")#10.{switch[10]} - {n10_25}\n11. {switch[11]} - {n11_25}\n12. {switch[12]} - {n12_25}\n13. {switch[13]} - {n13_25}\n14. {switch[14]} - {n14_25}\n15. {switch[15]} - {n15_25}\n16. {switch[16]} - {n16_25}\n17. {switch[17]} - {n17_25}\n18. {switch[18]} - {n18_25}\n19. {switch[19]} - {n19_25}\n20. {switch[20]} - {n20_25}\n21. {switch[21]} - {n21_25}\n22. {switch[22]} - {n22_25}\n23. {switch[23]} - {n23_25}\n24. {switch[24]} - {n24_25}\n25. {switch[25]} - {n25_25}\n26. {switch[26]} - {n26_25}\n27. {switch[27]} - {n27_25}\n28. {switch[28]} - {n28_25}\n29. {switch[29]} - {n29_25}\n30. {switch[30]} - {n30_25}\n31. {switch[31]} - {n31_25}\n32. {switch[32]} - {n32_25}\n33. {switch[33]} - {n33_25}\n34. {switch[34]} - {n34_25}\n35. {switch[35]} - {n35_25}\n36. {switch[36]} - {n36_25}\n37. {switch[37]} - {n37_25}")
    print(f"Twenty-six Year Olds:\n1. {switch[1]} - {n1_26}\n2. {switch[2]} - {n2_26}\n3. {switch[3]} - {n3_26}\n4. {switch[4]} - {n4_26}\n5. {switch[5]} - {n5_26}\n6. {switch[6]} - {n6_26}\n")#7. {switch[7]} - {n7_26}\n8. {switch[8]} - {n8_26}\n9. {switch[9]} - {n9_26}\n")#10.{switch[10]} - {n10_26}\n11. {switch[11]} - {n11_26}\n12. {switch[12]} - {n12_26}\n13. {switch[13]} - {n13_26}\n14. {switch[14]} - {n14_26}\n15. {switch[15]} - {n15_26}\n16. {switch[16]} - {n16_26}\n17. {switch[17]} - {n17_26}\n18. {switch[18]} - {n18_26}\n19. {switch[19]} - {n19_26}\n20. {switch[20]} - {n20_26}\n21. {switch[21]} - {n21_26}\n22. {switch[22]} - {n22_26}\n23. {switch[23]} - {n23_26}\n24. {switch[24]} - {n24_26}\n25. {switch[25]} - {n25_26}\n26. {switch[26]} - {n26_26}\n27. {switch[27]} - {n27_26}\n28. {switch[28]} - {n28_26}\n29. {switch[29]} - {n29_26}\n30. {switch[30]} - {n30_26}\n31. {switch[31]} - {n31_26}\n32. {switch[32]} - {n32_26}\n33. {switch[33]} - {n33_26}\n34. {switch[34]} - {n34_26}\n35. {switch[35]} - {n35_26}\n36. {switch[36]} - {n36_26}\n37. {switch[37]} - {n37_26}")
    print(f"Twenty-seven Year Olds:\n1. {switch[1]} - {n1_27}\n2. {switch[2]} - {n2_27}\n3. {switch[3]} - {n3_27}\n4. {switch[4]} - {n4_27}\n5. {switch[5]} - {n5_27}\n6. {switch[6]} - {n6_27}\n")#7. {switch[7]} - {n7_27}\n8. {switch[8]} - {n8_27}\n9. {switch[9]} - {n9_27}\n")#10.{switch[10]} - {n10_27}\n11. {switch[11]} - {n11_27}\n12. {switch[12]} - {n12_27}\n13. {switch[13]} - {n13_27}\n14. {switch[14]} - {n14_27}\n15. {switch[15]} - {n15_27}\n16. {switch[16]} - {n16_27}\n17. {switch[17]} - {n17_27}\n18. {switch[18]} - {n18_27}\n19. {switch[19]} - {n19_27}\n20. {switch[20]} - {n20_27}\n21. {switch[21]} - {n21_27}\n22. {switch[22]} - {n22_27}\n23. {switch[23]} - {n23_27}\n24. {switch[24]} - {n24_27}\n25. {switch[25]} - {n25_27}\n26. {switch[26]} - {n26_27}\n27. {switch[27]} - {n27_27}\n28. {switch[28]} - {n28_27}\n29. {switch[29]} - {n29_27}\n30. {switch[30]} - {n30_27}\n31. {switch[31]} - {n31_27}\n32. {switch[32]} - {n32_27}\n33. {switch[33]} - {n33_27}\n34. {switch[34]} - {n34_27}\n35. {switch[35]} - {n35_27}\n36. {switch[36]} - {n36_27}\n37. {switch[37]} - {n37_27}")
    print(f"Twenty-eight Year Olds:\n1. {switch[1]} - {n1_28}\n2. {switch[2]} - {n2_28}\n3. {switch[3]} - {n3_28}\n4. {switch[4]} - {n4_28}\n5. {switch[5]} - {n5_28}\n6. {switch[6]} - {n6_28}\n")#7. {switch[7]} - {n7_28}\n8. {switch[8]} - {n8_28}\n9. {switch[9]} - {n9_28}\n")#10.{switch[10]} - {n10_28}\n11. {switch[11]} - {n11_28}\n12. {switch[12]} - {n12_28}\n13. {switch[13]} - {n13_28}\n14. {switch[14]} - {n14_28}\n15. {switch[15]} - {n15_28}\n16. {switch[16]} - {n16_28}\n17. {switch[17]} - {n17_28}\n18. {switch[18]} - {n18_28}\n19. {switch[19]} - {n19_28}\n20. {switch[20]} - {n20_28}\n21. {switch[21]} - {n21_28}\n22. {switch[22]} - {n22_28}\n23. {switch[23]} - {n23_28}\n24. {switch[24]} - {n24_28}\n25. {switch[25]} - {n25_28}\n26. {switch[26]} - {n26_28}\n27. {switch[27]} - {n27_28}\n28. {switch[28]} - {n28_28}\n29. {switch[29]} - {n29_28}\n30. {switch[30]} - {n30_28}\n31. {switch[31]} - {n31_28}\n32. {switch[32]} - {n32_28}\n33. {switch[33]} - {n33_28}\n34. {switch[34]} - {n34_28}\n35. {switch[35]} - {n35_28}\n36. {switch[36]} - {n36_28}\n37. {switch[37]} - {n37_28}")
    print(f"Twenty-nine Year Olds:\n1. {switch[1]} - {n1_29}\n2. {switch[2]} - {n2_29}\n3. {switch[3]} - {n3_29}\n4. {switch[4]} - {n4_29}\n5. {switch[5]} - {n5_29}\n6. {switch[6]} - {n6_29}\n")#7. {switch[7]} - {n7_29}\n8. {switch[8]} - {n8_29}\n9. {switch[9]} - {n9_29}\n")#10.{switch[10]} - {n10_29}\n11. {switch[11]} - {n11_29}\n12. {switch[12]} - {n12_29}\n13. {switch[13]} - {n13_29}\n14. {switch[14]} - {n14_29}\n15. {switch[15]} - {n15_29}\n16. {switch[16]} - {n16_29}\n17. {switch[17]} - {n17_29}\n18. {switch[18]} - {n18_29}\n19. {switch[19]} - {n19_29}\n20. {switch[20]} - {n20_29}\n21. {switch[21]} - {n21_29}\n22. {switch[22]} - {n22_29}\n23. {switch[23]} - {n23_29}\n24. {switch[24]} - {n24_29}\n25. {switch[25]} - {n25_29}\n26. {switch[26]} - {n26_29}\n27. {switch[27]} - {n27_29}\n28. {switch[28]} - {n28_29}\n29. {switch[29]} - {n29_29}\n30. {switch[30]} - {n30_29}\n31. {switch[31]} - {n31_29}\n32. {switch[32]} - {n32_29}\n33. {switch[33]} - {n33_29}\n34. {switch[34]} - {n34_29}\n35. {switch[35]} - {n35_29}\n36. {switch[36]} - {n36_29}\n37. {switch[37]} - {n37_29}")
    print(f"Thirty Year Olds:\n1. {switch[1]} - {n1_30}\n2. {switch[2]} - {n2_30}\n3. {switch[3]} - {n3_30}\n4. {switch[4]} - {n4_30}\n5. {switch[5]} - {n5_30}\n6. {switch[6]} - {n6_30}\n")#7. {switch[7]} - {n7_30}\n8. {switch[8]} - {n8_30}\n9. {switch[9]} - {n9_30}\n")#10.{switch[10]} - {n10_30}\n11. {switch[11]} - {n11_30}\n12. {switch[12]} - {n12_30}\n13. {switch[13]} - {n13_30}\n14. {switch[14]} - {n14_30}\n15. {switch[15]} - {n15_30}\n16. {switch[16]} - {n16_30}\n17. {switch[17]} - {n17_30}\n18. {switch[18]} - {n18_30}\n19. {switch[19]} - {n19_30}\n20. {switch[20]} - {n20_30}\n21. {switch[21]} - {n21_30}\n22. {switch[22]} - {n22_30}\n23. {switch[23]} - {n23_30}\n24. {switch[24]} - {n24_30}\n25. {switch[25]} - {n25_30}\n26. {switch[26]} - {n26_30}\n27. {switch[27]} - {n27_30}\n28. {switch[28]} - {n28_30}\n29. {switch[29]} - {n29_30}\n30. {switch[30]} - {n30_30}\n31. {switch[31]} - {n31_30}\n32. {switch[32]} - {n32_30}\n33. {switch[33]} - {n33_30}\n34. {switch[34]} - {n34_30}\n35. {switch[35]} - {n35_30}\n36. {switch[36]} - {n36_30}\n37. {switch[37]} - {n37_30}")
    print(f"Thirty-one Year Olds:\n1. {switch[1]} - {n1_31}\n2. {switch[2]} - {n2_31}\n3. {switch[3]} - {n3_31}\n4. {switch[4]} - {n4_31}\n5. {switch[5]} - {n5_31}\n6. {switch[6]} - {n6_31}\n")#7. {switch[7]} - {n7_31}\n8. {switch[8]} - {n8_31}\n9. {switch[9]} - {n9_31}\n")#10.{switch[10]} - {n10_31}\n11. {switch[11]} - {n11_31}\n12. {switch[12]} - {n12_31}\n13. {switch[13]} - {n13_31}\n14. {switch[14]} - {n14_31}\n15. {switch[15]} - {n15_31}\n16. {switch[16]} - {n16_31}\n17. {switch[17]} - {n17_31}\n18. {switch[18]} - {n18_31}\n19. {switch[19]} - {n19_31}\n20. {switch[20]} - {n20_31}\n21. {switch[21]} - {n21_31}\n22. {switch[22]} - {n22_31}\n23. {switch[23]} - {n23_31}\n24. {switch[24]} - {n24_31}\n25. {switch[25]} - {n25_31}\n26. {switch[26]} - {n26_31}\n27. {switch[27]} - {n27_31}\n28. {switch[28]} - {n28_31}\n29. {switch[29]} - {n29_31}\n30. {switch[30]} - {n30_31}\n31. {switch[31]} - {n31_31}\n32. {switch[32]} - {n32_31}\n33. {switch[33]} - {n33_31}\n34. {switch[34]} - {n34_31}\n35. {switch[35]} - {n35_31}\n36. {switch[36]} - {n36_31}\n37. {switch[37]} - {n37_31}")
    print(f"Thirty-two Year Olds:\n1. {switch[1]} - {n1_32}\n2. {switch[2]} - {n2_32}\n3. {switch[3]} - {n3_32}\n4. {switch[4]} - {n4_32}\n5. {switch[5]} - {n5_32}\n6. {switch[6]} - {n6_32}\n")#7. {switch[7]} - {n7_32}\n8. {switch[8]} - {n8_32}\n9. {switch[9]} - {n9_32}\n")#10.{switch[10]} - {n10_32}\n11. {switch[11]} - {n11_32}\n12. {switch[12]} - {n12_32}\n13. {switch[13]} - {n13_32}\n14. {switch[14]} - {n14_32}\n15. {switch[15]} - {n15_32}\n16. {switch[16]} - {n16_32}\n17. {switch[17]} - {n17_32}\n18. {switch[18]} - {n18_32}\n19. {switch[19]} - {n19_32}\n20. {switch[20]} - {n20_32}\n21. {switch[21]} - {n21_32}\n22. {switch[22]} - {n22_32}\n23. {switch[23]} - {n23_32}\n24. {switch[24]} - {n24_32}\n25. {switch[25]} - {n25_32}\n26. {switch[26]} - {n26_32}\n27. {switch[27]} - {n27_32}\n28. {switch[28]} - {n28_32}\n29. {switch[29]} - {n29_32}\n30. {switch[30]} - {n30_32}\n31. {switch[31]} - {n31_32}\n32. {switch[32]} - {n32_32}\n33. {switch[33]} - {n33_32}\n34. {switch[34]} - {n34_32}\n35. {switch[35]} - {n35_32}\n36. {switch[36]} - {n36_32}\n37. {switch[37]} - {n37_32}")
    print(f"Thirty-three Year Olds:\n1. {switch[1]} - {n1_33}\n2. {switch[2]} - {n2_33}\n3. {switch[3]} - {n3_33}\n4. {switch[4]} - {n4_33}\n5. {switch[5]} - {n5_33}\n6. {switch[6]} - {n6_33}\n")#7. {switch[7]} - {n7_33}\n8. {switch[8]} - {n8_33}\n9. {switch[9]} - {n9_33}\n")#10.{switch[10]} - {n10_33}\n11. {switch[11]} - {n11_33}\n12. {switch[12]} - {n12_33}\n13. {switch[13]} - {n13_33}\n14. {switch[14]} - {n14_33}\n15. {switch[15]} - {n15_33}\n16. {switch[16]} - {n16_33}\n17. {switch[17]} - {n17_33}\n18. {switch[18]} - {n18_33}\n19. {switch[19]} - {n19_33}\n20. {switch[20]} - {n20_33}\n21. {switch[21]} - {n21_33}\n22. {switch[22]} - {n22_33}\n23. {switch[23]} - {n23_33}\n24. {switch[24]} - {n24_33}\n25. {switch[25]} - {n25_33}\n26. {switch[26]} - {n26_33}\n27. {switch[27]} - {n27_33}\n28. {switch[28]} - {n28_33}\n29. {switch[29]} - {n29_33}\n30. {switch[30]} - {n30_33}\n31. {switch[31]} - {n31_33}\n32. {switch[32]} - {n32_33}\n33. {switch[33]} - {n33_33}\n34. {switch[34]} - {n34_33}\n35. {switch[35]} - {n35_33}\n36. {switch[36]} - {n36_33}\n37. {switch[37]} - {n37_33}")
    print(f"Thirty-four Year Olds:\n1. {switch[1]} - {n1_34}\n2. {switch[2]} - {n2_34}\n3. {switch[3]} - {n3_34}\n4. {switch[4]} - {n4_34}\n5. {switch[5]} - {n5_34}\n6. {switch[6]} - {n6_34}\n")#7. {switch[7]} - {n7_34}\n8. {switch[8]} - {n8_34}\n9. {switch[9]} - {n9_34}\n")#10.{switch[10]} - {n10_34}\n11. {switch[11]} - {n11_34}\n12. {switch[12]} - {n12_34}\n13. {switch[13]} - {n13_34}\n14. {switch[14]} - {n14_34}\n15. {switch[15]} - {n15_34}\n16. {switch[16]} - {n16_34}\n17. {switch[17]} - {n17_34}\n18. {switch[18]} - {n18_34}\n19. {switch[19]} - {n19_34}\n20. {switch[20]} - {n20_34}\n21. {switch[21]} - {n21_34}\n22. {switch[22]} - {n22_34}\n23. {switch[23]} - {n23_34}\n24. {switch[24]} - {n24_34}\n25. {switch[25]} - {n25_34}\n26. {switch[26]} - {n26_34}\n27. {switch[27]} - {n27_34}\n28. {switch[28]} - {n28_34}\n29. {switch[29]} - {n29_34}\n30. {switch[30]} - {n30_34}\n31. {switch[31]} - {n31_34}\n32. {switch[32]} - {n32_34}\n33. {switch[33]} - {n33_34}\n34. {switch[34]} - {n34_34}\n35. {switch[35]} - {n35_34}\n36. {switch[36]} - {n36_34}\n37. {switch[37]} - {n37_34}")
    print(f"Thirty-five Year Olds:\n1. {switch[1]} - {n1_35}\n2. {switch[2]} - {n2_35}\n3. {switch[3]} - {n3_35}\n4. {switch[4]} - {n4_35}\n5. {switch[5]} - {n5_35}\n6. {switch[6]} - {n6_35}\n")#7. {switch[7]} - {n7_35}\n8. {switch[8]} - {n8_35}\n9. {switch[9]} - {n9_35}\n")#10.{switch[10]} - {n10_35}\n11. {switch[11]} - {n11_35}\n12. {switch[12]} - {n12_35}\n13. {switch[13]} - {n13_35}\n14. {switch[14]} - {n14_35}\n15. {switch[15]} - {n15_35}\n16. {switch[16]} - {n16_35}\n17. {switch[17]} - {n17_35}\n18. {switch[18]} - {n18_35}\n19. {switch[19]} - {n19_35}\n20. {switch[20]} - {n20_35}\n21. {switch[21]} - {n21_35}\n22. {switch[22]} - {n22_35}\n23. {switch[23]} - {n23_35}\n24. {switch[24]} - {n24_35}\n25. {switch[25]} - {n25_35}\n26. {switch[26]} - {n26_35}\n27. {switch[27]} - {n27_35}\n28. {switch[28]} - {n28_35}\n29. {switch[29]} - {n29_35}\n30. {switch[30]} - {n30_35}\n31. {switch[31]} - {n31_35}\n32. {switch[32]} - {n32_35}\n33. {switch[33]} - {n33_35}\n34. {switch[34]} - {n34_35}\n35. {switch[35]} - {n35_35}\n36. {switch[36]} - {n36_35}\n37. {switch[37]} - {n37_35}")
    print(f"Thirty-six Year Olds:\n1. {switch[1]} - {n1_36}\n2. {switch[2]} - {n2_36}\n3. {switch[3]} - {n3_36}\n4. {switch[4]} - {n4_36}\n5. {switch[5]} - {n5_36}\n6. {switch[6]} - {n6_36}\n")#7. {switch[7]} - {n7_36}\n8. {switch[8]} - {n8_36}\n9. {switch[9]} - {n9_36}\n")#10.{switch[10]} - {n10_36}\n11. {switch[11]} - {n11_36}\n12. {switch[12]} - {n12_36}\n13. {switch[13]} - {n13_36}\n14. {switch[14]} - {n14_36}\n15. {switch[15]} - {n15_36}\n16. {switch[16]} - {n16_36}\n17. {switch[17]} - {n17_36}\n18. {switch[18]} - {n18_36}\n19. {switch[19]} - {n19_36}\n20. {switch[20]} - {n20_36}\n21. {switch[21]} - {n21_36}\n22. {switch[22]} - {n22_36}\n23. {switch[23]} - {n23_36}\n24. {switch[24]} - {n24_36}\n25. {switch[25]} - {n25_36}\n26. {switch[26]} - {n26_36}\n27. {switch[27]} - {n27_36}\n28. {switch[28]} - {n28_36}\n29. {switch[29]} - {n29_36}\n30. {switch[30]} - {n30_36}\n31. {switch[31]} - {n31_36}\n32. {switch[32]} - {n32_36}\n33. {switch[33]} - {n33_36}\n34. {switch[34]} - {n34_36}\n35. {switch[35]} - {n35_36}\n36. {switch[36]} - {n36_36}\n37. {switch[37]} - {n37_36}")
    print(f"Thirty-seven Year Olds:\n1. {switch[1]} - {n1_37}\n2. {switch[2]} - {n2_37}\n3. {switch[3]} - {n3_37}\n4. {switch[4]} - {n4_37}\n5. {switch[5]} - {n5_37}\n6. {switch[6]} - {n6_37}\n")#7. {switch[7]} - {n7_37}\n8. {switch[8]} - {n8_37}\n9. {switch[9]} - {n9_37}\n")#10.{switch[10]} - {n10_37}\n11. {switch[11]} - {n11_37}\n12. {switch[12]} - {n12_37}\n13. {switch[13]} - {n13_37}\n14. {switch[14]} - {n14_37}\n15. {switch[15]} - {n15_37}\n16. {switch[16]} - {n16_37}\n17. {switch[17]} - {n17_37}\n18. {switch[18]} - {n18_37}\n19. {switch[19]} - {n19_37}\n20. {switch[20]} - {n20_37}\n21. {switch[21]} - {n21_37}\n22. {switch[22]} - {n22_37}\n23. {switch[23]} - {n23_37}\n24. {switch[24]} - {n24_37}\n25. {switch[25]} - {n25_37}\n26. {switch[26]} - {n26_37}\n27. {switch[27]} - {n27_37}\n28. {switch[28]} - {n28_37}\n29. {switch[29]} - {n29_37}\n30. {switch[30]} - {n30_37}\n31. {switch[31]} - {n31_37}\n32. {switch[32]} - {n32_37}\n33. {switch[33]} - {n33_37}\n34. {switch[34]} - {n34_37}\n35. {switch[35]} - {n35_37}\n36. {switch[36]} - {n36_37}\n37. {switch[37]} - {n37_37}")
    print(f"Thirty-eight Year Olds:\n1. {switch[1]} - {n1_38}\n2. {switch[2]} - {n2_38}\n3. {switch[3]} - {n3_38}\n4. {switch[4]} - {n4_38}\n5. {switch[5]} - {n5_38}\n6. {switch[6]} - {n6_38}\n")#7. {switch[7]} - {n7_38}\n8. {switch[8]} - {n8_38}\n9. {switch[9]} - {n9_38}\n")#10.{switch[10]} - {n10_38}\n11. {switch[11]} - {n11_38}\n12. {switch[12]} - {n12_38}\n13. {switch[13]} - {n13_38}\n14. {switch[14]} - {n14_38}\n15. {switch[15]} - {n15_38}\n16. {switch[16]} - {n16_38}\n17. {switch[17]} - {n17_38}\n18. {switch[18]} - {n18_38}\n19. {switch[19]} - {n19_38}\n20. {switch[20]} - {n20_38}\n21. {switch[21]} - {n21_38}\n22. {switch[22]} - {n22_38}\n23. {switch[23]} - {n23_38}\n24. {switch[24]} - {n24_38}\n25. {switch[25]} - {n25_38}\n26. {switch[26]} - {n26_38}\n27. {switch[27]} - {n27_38}\n28. {switch[28]} - {n28_38}\n29. {switch[29]} - {n29_38}\n30. {switch[30]} - {n30_38}\n31. {switch[31]} - {n31_38}\n32. {switch[32]} - {n32_38}\n33. {switch[33]} - {n33_38}\n34. {switch[34]} - {n34_38}\n35. {switch[35]} - {n35_38}\n36. {switch[36]} - {n36_38}\n37. {switch[37]} - {n37_38}")
    print(f"Thirty-nine Year Olds:\n1. {switch[1]} - {n1_39}\n2. {switch[2]} - {n2_39}\n3. {switch[3]} - {n3_39}\n4. {switch[4]} - {n4_39}\n5. {switch[5]} - {n5_39}\n6. {switch[6]} - {n6_39}\n")#7. {switch[7]} - {n7_39}\n8. {switch[8]} - {n8_39}\n9. {switch[9]} - {n9_39}\n")#10.{switch[10]} - {n10_39}\n11. {switch[11]} - {n11_39}\n12. {switch[12]} - {n12_39}\n13. {switch[13]} - {n13_39}\n14. {switch[14]} - {n14_39}\n15. {switch[15]} - {n15_39}\n16. {switch[16]} - {n16_39}\n17. {switch[17]} - {n17_39}\n18. {switch[18]} - {n18_39}\n19. {switch[19]} - {n19_39}\n20. {switch[20]} - {n20_39}\n21. {switch[21]} - {n21_39}\n22. {switch[22]} - {n22_39}\n23. {switch[23]} - {n23_39}\n24. {switch[24]} - {n24_39}\n25. {switch[25]} - {n25_39}\n26. {switch[26]} - {n26_39}\n27. {switch[27]} - {n27_39}\n28. {switch[28]} - {n28_39}\n29. {switch[29]} - {n29_39}\n30. {switch[30]} - {n30_39}\n31. {switch[31]} - {n31_39}\n32. {switch[32]} - {n32_39}\n33. {switch[33]} - {n33_39}\n34. {switch[34]} - {n34_39}\n35. {switch[35]} - {n35_39}\n36. {switch[36]} - {n36_39}\n37. {switch[37]} - {n37_39}")
    print(f"Fourty Year Olds:\n1. {switch[1]} - {n1_40}\n2. {switch[2]} - {n2_40}\n3. {switch[3]} - {n3_40}\n4. {switch[4]} - {n4_40}\n5. {switch[5]} - {n5_40}\n6. {switch[6]} - {n6_40}\n")#7. {switch[7]} - {n7_40}\n8. {switch[8]} - {n8_40}\n9. {switch[9]} - {n9_40}\n")#10.{switch[10]} - {n10_40}\n11. {switch[11]} - {n11_40}\n12. {switch[12]} - {n12_40}\n13. {switch[13]} - {n13_40}\n14. {switch[14]} - {n14_40}\n15. {switch[15]} - {n15_40}\n16. {switch[16]} - {n16_40}\n17. {switch[17]} - {n17_40}\n18. {switch[18]} - {n18_40}\n19. {switch[19]} - {n19_40}\n20. {switch[20]} - {n20_40}\n21. {switch[21]} - {n21_40}\n22. {switch[22]} - {n22_40}\n23. {switch[23]} - {n23_40}\n24. {switch[24]} - {n24_40}\n25. {switch[25]} - {n25_40}\n26. {switch[26]} - {n26_40}\n27. {switch[27]} - {n27_40}\n28. {switch[28]} - {n28_40}\n29. {switch[29]} - {n29_40}\n30. {switch[30]} - {n30_40}\n31. {switch[31]} - {n31_40}\n32. {switch[32]} - {n32_40}\n33. {switch[33]} - {n33_40}\n34. {switch[34]} - {n34_40}\n35. {switch[35]} - {n35_40}\n36. {switch[36]} - {n36_40}\n37. {switch[37]} - {n37_40}")
    print(f"Fourty-one Year Olds:\n1. {switch[1]} - {n1_41}\n2. {switch[2]} - {n2_41}\n3. {switch[3]} - {n3_41}\n4. {switch[4]} - {n4_41}\n5. {switch[5]} - {n5_41}\n6. {switch[6]} - {n6_41}\n")#7. {switch[7]} - {n7_41}\n8. {switch[8]} - {n8_41}\n9. {switch[9]} - {n9_41}\n")#10.{switch[10]} - {n10_41}\n11. {switch[11]} - {n11_41}\n12. {switch[12]} - {n12_41}\n13. {switch[13]} - {n13_41}\n14. {switch[14]} - {n14_41}\n15. {switch[15]} - {n15_41}\n16. {switch[16]} - {n16_41}\n17. {switch[17]} - {n17_41}\n18. {switch[18]} - {n18_41}\n19. {switch[19]} - {n19_41}\n20. {switch[20]} - {n20_41}\n21. {switch[21]} - {n21_41}\n22. {switch[22]} - {n22_41}\n23. {switch[23]} - {n23_41}\n24. {switch[24]} - {n24_41}\n25. {switch[25]} - {n25_41}\n26. {switch[26]} - {n26_41}\n27. {switch[27]} - {n27_41}\n28. {switch[28]} - {n28_41}\n29. {switch[29]} - {n29_41}\n30. {switch[30]} - {n30_41}\n31. {switch[31]} - {n31_41}\n32. {switch[32]} - {n32_41}\n33. {switch[33]} - {n33_41}\n34. {switch[34]} - {n34_41}\n35. {switch[35]} - {n35_41}\n36. {switch[36]} - {n36_41}\n37. {switch[37]} - {n37_41}")
    print(f"Fourty-two Year Olds:\n1. {switch[1]} - {n1_42}\n2. {switch[2]} - {n2_42}\n3. {switch[3]} - {n3_42}\n4. {switch[4]} - {n4_42}\n5. {switch[5]} - {n5_42}\n6. {switch[6]} - {n6_42}\n")#7. {switch[7]} - {n7_42}\n8. {switch[8]} - {n8_42}\n9. {switch[9]} - {n9_42}\n")#10.{switch[10]} - {n10_42}\n11. {switch[11]} - {n11_42}\n12. {switch[12]} - {n12_42}\n13. {switch[13]} - {n13_42}\n14. {switch[14]} - {n14_42}\n15. {switch[15]} - {n15_42}\n16. {switch[16]} - {n16_42}\n17. {switch[17]} - {n17_42}\n18. {switch[18]} - {n18_42}\n19. {switch[19]} - {n19_42}\n20. {switch[20]} - {n20_42}\n21. {switch[21]} - {n21_42}\n22. {switch[22]} - {n22_42}\n23. {switch[23]} - {n23_42}\n24. {switch[24]} - {n24_42}\n25. {switch[25]} - {n25_42}\n26. {switch[26]} - {n26_42}\n27. {switch[27]} - {n27_42}\n28. {switch[28]} - {n28_42}\n29. {switch[29]} - {n29_42}\n30. {switch[30]} - {n30_42}\n31. {switch[31]} - {n31_42}\n32. {switch[32]} - {n32_42}\n33. {switch[33]} - {n33_42}\n34. {switch[34]} - {n34_42}\n35. {switch[35]} - {n35_42}\n36. {switch[36]} - {n36_42}\n37. {switch[37]} - {n37_42}")
    print(f"Fourty-three Year Olds:\n1. {switch[1]} - {n1_43}\n2. {switch[2]} - {n2_43}\n3. {switch[3]} - {n3_43}\n4. {switch[4]} - {n4_43}\n5. {switch[5]} - {n5_43}\n6. {switch[6]} - {n6_43}\n")#7. {switch[7]} - {n7_43}\n8. {switch[8]} - {n8_43}\n9. {switch[9]} - {n9_43}\n")#10.{switch[10]} - {n10_43}\n11. {switch[11]} - {n11_43}\n12. {switch[12]} - {n12_43}\n13. {switch[13]} - {n13_43}\n14. {switch[14]} - {n14_43}\n15. {switch[15]} - {n15_43}\n16. {switch[16]} - {n16_43}\n17. {switch[17]} - {n17_43}\n18. {switch[18]} - {n18_43}\n19. {switch[19]} - {n19_43}\n20. {switch[20]} - {n20_43}\n21. {switch[21]} - {n21_43}\n22. {switch[22]} - {n22_43}\n23. {switch[23]} - {n23_43}\n24. {switch[24]} - {n24_43}\n25. {switch[25]} - {n25_43}\n26. {switch[26]} - {n26_43}\n27. {switch[27]} - {n27_43}\n28. {switch[28]} - {n28_43}\n29. {switch[29]} - {n29_43}\n30. {switch[30]} - {n30_43}\n31. {switch[31]} - {n31_43}\n32. {switch[32]} - {n32_43}\n33. {switch[33]} - {n33_43}\n34. {switch[34]} - {n34_43}\n35. {switch[35]} - {n35_43}\n36. {switch[36]} - {n36_43}\n37. {switch[37]} - {n37_43}")
    print(f"Fourty-four Year Olds:\n1. {switch[1]} - {n1_44}\n2. {switch[2]} - {n2_44}\n3. {switch[3]} - {n3_44}\n4. {switch[4]} - {n4_44}\n5. {switch[5]} - {n5_44}\n6. {switch[6]} - {n6_44}\n")#7. {switch[7]} - {n7_44}\n8. {switch[8]} - {n8_44}\n9. {switch[9]} - {n9_44}\n")#10.{switch[10]} - {n10_44}\n11. {switch[11]} - {n11_44}\n12. {switch[12]} - {n12_44}\n13. {switch[13]} - {n13_44}\n14. {switch[14]} - {n14_44}\n15. {switch[15]} - {n15_44}\n16. {switch[16]} - {n16_44}\n17. {switch[17]} - {n17_44}\n18. {switch[18]} - {n18_44}\n19. {switch[19]} - {n19_44}\n20. {switch[20]} - {n20_44}\n21. {switch[21]} - {n21_44}\n22. {switch[22]} - {n22_44}\n23. {switch[23]} - {n23_44}\n24. {switch[24]} - {n24_44}\n25. {switch[25]} - {n25_44}\n26. {switch[26]} - {n26_44}\n27. {switch[27]} - {n27_44}\n28. {switch[28]} - {n28_44}\n29. {switch[29]} - {n29_44}\n30. {switch[30]} - {n30_44}\n31. {switch[31]} - {n31_44}\n32. {switch[32]} - {n32_44}\n33. {switch[33]} - {n33_44}\n34. {switch[34]} - {n34_44}\n35. {switch[35]} - {n35_44}\n36. {switch[36]} - {n36_44}\n37. {switch[37]} - {n37_44}")
    print(f"Fourty-five Year Olds:\n1. {switch[1]} - {n1_45}\n2. {switch[2]} - {n2_45}\n3. {switch[3]} - {n3_45}\n4. {switch[4]} - {n4_45}\n5. {switch[5]} - {n5_45}\n6. {switch[6]} - {n6_45}\n")#7. {switch[7]} - {n7_45}\n8. {switch[8]} - {n8_45}\n9. {switch[9]} - {n9_45}\n")#10.{switch[10]} - {n10_45}\n11. {switch[11]} - {n11_45}\n12. {switch[12]} - {n12_45}\n13. {switch[13]} - {n13_45}\n14. {switch[14]} - {n14_45}\n15. {switch[15]} - {n15_45}\n16. {switch[16]} - {n16_45}\n17. {switch[17]} - {n17_45}\n18. {switch[18]} - {n18_45}\n19. {switch[19]} - {n19_45}\n20. {switch[20]} - {n20_45}\n21. {switch[21]} - {n21_45}\n22. {switch[22]} - {n22_45}\n23. {switch[23]} - {n23_45}\n24. {switch[24]} - {n24_45}\n25. {switch[25]} - {n25_45}\n26. {switch[26]} - {n26_45}\n27. {switch[27]} - {n27_45}\n28. {switch[28]} - {n28_45}\n29. {switch[29]} - {n29_45}\n30. {switch[30]} - {n30_45}\n31. {switch[31]} - {n31_45}\n32. {switch[32]} - {n32_45}\n33. {switch[33]} - {n33_45}\n34. {switch[34]} - {n34_45}\n35. {switch[35]} - {n35_45}\n36. {switch[36]} - {n36_45}\n37. {switch[37]} - {n37_45}")
    print(f"Fourty-six Year Olds:\n1. {switch[1]} - {n1_46}\n2. {switch[2]} - {n2_46}\n3. {switch[3]} - {n3_46}\n4. {switch[4]} - {n4_46}\n5. {switch[5]} - {n5_46}\n6. {switch[6]} - {n6_46}\n")#7. {switch[7]} - {n7_46}\n8. {switch[8]} - {n8_46}\n9. {switch[9]} - {n9_46}\n")#10.{switch[10]} - {n10_46}\n11. {switch[11]} - {n11_46}\n12. {switch[12]} - {n12_46}\n13. {switch[13]} - {n13_46}\n14. {switch[14]} - {n14_46}\n15. {switch[15]} - {n15_46}\n16. {switch[16]} - {n16_46}\n17. {switch[17]} - {n17_46}\n18. {switch[18]} - {n18_46}\n19. {switch[19]} - {n19_46}\n20. {switch[20]} - {n20_46}\n21. {switch[21]} - {n21_46}\n22. {switch[22]} - {n22_46}\n23. {switch[23]} - {n23_46}\n24. {switch[24]} - {n24_46}\n25. {switch[25]} - {n25_46}\n26. {switch[26]} - {n26_46}\n27. {switch[27]} - {n27_46}\n28. {switch[28]} - {n28_46}\n29. {switch[29]} - {n29_46}\n30. {switch[30]} - {n30_46}\n31. {switch[31]} - {n31_46}\n32. {switch[32]} - {n32_46}\n33. {switch[33]} - {n33_46}\n34. {switch[34]} - {n34_46}\n35. {switch[35]} - {n35_46}\n36. {switch[36]} - {n36_46}\n37. {switch[37]} - {n37_46}")
    print(f"Fourty-seven Year Olds:\n1. {switch[1]} - {n1_47}\n2. {switch[2]} - {n2_47}\n3. {switch[3]} - {n3_47}\n4. {switch[4]} - {n4_47}\n5. {switch[5]} - {n5_47}\n6. {switch[6]} - {n6_47}\n")#7. {switch[7]} - {n7_47}\n8. {switch[8]} - {n8_47}\n9. {switch[9]} - {n9_47}\n")#10.{switch[10]} - {n10_47}\n11. {switch[11]} - {n11_47}\n12. {switch[12]} - {n12_47}\n13. {switch[13]} - {n13_47}\n14. {switch[14]} - {n14_47}\n15. {switch[15]} - {n15_47}\n16. {switch[16]} - {n16_47}\n17. {switch[17]} - {n17_47}\n18. {switch[18]} - {n18_47}\n19. {switch[19]} - {n19_47}\n20. {switch[20]} - {n20_47}\n21. {switch[21]} - {n21_47}\n22. {switch[22]} - {n22_47}\n23. {switch[23]} - {n23_47}\n24. {switch[24]} - {n24_47}\n25. {switch[25]} - {n25_47}\n26. {switch[26]} - {n26_47}\n27. {switch[27]} - {n27_47}\n28. {switch[28]} - {n28_47}\n29. {switch[29]} - {n29_47}\n30. {switch[30]} - {n30_47}\n31. {switch[31]} - {n31_47}\n32. {switch[32]} - {n32_47}\n33. {switch[33]} - {n33_47}\n34. {switch[34]} - {n34_47}\n35. {switch[35]} - {n35_47}\n36. {switch[36]} - {n36_47}\n37. {switch[37]} - {n37_47}")
    print(f"Fourty-eight Year Olds:\n1. {switch[1]} - {n1_48}\n2. {switch[2]} - {n2_48}\n3. {switch[3]} - {n3_48}\n4. {switch[4]} - {n4_48}\n5. {switch[5]} - {n5_48}\n6. {switch[6]} - {n6_48}\n")#7. {switch[7]} - {n7_48}\n8. {switch[8]} - {n8_48}\n9. {switch[9]} - {n9_48}\n")#10.{switch[10]} - {n10_48}\n11. {switch[11]} - {n11_48}\n12. {switch[12]} - {n12_48}\n13. {switch[13]} - {n13_48}\n14. {switch[14]} - {n14_48}\n15. {switch[15]} - {n15_48}\n16. {switch[16]} - {n16_48}\n17. {switch[17]} - {n17_48}\n18. {switch[18]} - {n18_48}\n19. {switch[19]} - {n19_48}\n20. {switch[20]} - {n20_48}\n21. {switch[21]} - {n21_48}\n22. {switch[22]} - {n22_48}\n23. {switch[23]} - {n23_48}\n24. {switch[24]} - {n24_48}\n25. {switch[25]} - {n25_48}\n26. {switch[26]} - {n26_48}\n27. {switch[27]} - {n27_48}\n28. {switch[28]} - {n28_48}\n29. {switch[29]} - {n29_48}\n30. {switch[30]} - {n30_48}\n31. {switch[31]} - {n31_48}\n32. {switch[32]} - {n32_48}\n33. {switch[33]} - {n33_48}\n34. {switch[34]} - {n34_48}\n35. {switch[35]} - {n35_48}\n36. {switch[36]} - {n36_48}\n37. {switch[37]} - {n37_48}")
    print(f"Fourty-nine Year Olds:\n1. {switch[1]} - {n1_49}\n2. {switch[2]} - {n2_49}\n3. {switch[3]} - {n3_49}\n4. {switch[4]} - {n4_49}\n5. {switch[5]} - {n5_49}\n6. {switch[6]} - {n6_49}\n")#7. {switch[7]} - {n7_49}\n8. {switch[8]} - {n8_49}\n9. {switch[9]} - {n9_49}\n")#10.{switch[10]} - {n10_49}\n11. {switch[11]} - {n11_49}\n12. {switch[12]} - {n12_49}\n13. {switch[13]} - {n13_49}\n14. {switch[14]} - {n14_49}\n15. {switch[15]} - {n15_49}\n16. {switch[16]} - {n16_49}\n17. {switch[17]} - {n17_49}\n18. {switch[18]} - {n18_49}\n19. {switch[19]} - {n19_49}\n20. {switch[20]} - {n20_49}\n21. {switch[21]} - {n21_49}\n22. {switch[22]} - {n22_49}\n23. {switch[23]} - {n23_49}\n24. {switch[24]} - {n24_49}\n25. {switch[25]} - {n25_49}\n26. {switch[26]} - {n26_49}\n27. {switch[27]} - {n27_49}\n28. {switch[28]} - {n28_49}\n29. {switch[29]} - {n29_49}\n30. {switch[30]} - {n30_49}\n31. {switch[31]} - {n31_49}\n32. {switch[32]} - {n32_49}\n33. {switch[33]} - {n33_49}\n34. {switch[34]} - {n34_49}\n35. {switch[35]} - {n35_49}\n36. {switch[36]} - {n36_49}\n37. {switch[37]} - {n37_49}")


################## printOutput ###############
def printOutput():
    os.system('clear')
    totp, tots, thir, four, fif, six, seven, eigh, nin, twent, twentone, twenttwo, twentthree, twentfour, twentfive, twentsix, twentseven, twenteight, twentnine, thirt, thirtone, thirttwo, thirtthree, thirtfour, thirtfive, thirtsix, thirtseven, thirteight, thirtnine, fourt, fourtone, fourttwo, fourtthree, fourtfour, fourtfive, fourtsix, fourtseven, fourteight, fourtnine = getTotals()
    print("The following represents the number of participants and the total amount of times they have gotten sick") # finish
    print(f"Total number of people that participated: {totp}")
    print(f"Total number of people that are sick that participated: {tots}")
    print(f"Number of thirteen year olds that participated: {thir}")
    print(f"Number of fourteen year olds that participated: {four}")
    print(f"Number of fifteen year olds that participated: {fif}")
    print(f"Number of sixteen year olds that participated: {six}")
    print(f"Number of seventeen year olds that participated: {seven}")
    print(f"Number of eighteen year olds that participated: {eigh}")
    print(f"Number of nineteen year olds that participated: {nin}")
    print(f"Number of twenty year olds that participated: {twent}")
    print(f"Number of twenty one year olds that participated: {twentone}")
    print(f"Number of twenty two year olds that participated: {twenttwo}")
    print(f"Number of twenty three year olds that participated: {twentthree}")
    print(f"Number of twenty four year olds that participated: {twentfour}")
    print(f"Number of twenty five year olds that participated: {twentfive}")
    print(f"Number of twenty six year olds that participated: {twentsix}")
    print(f"Number of twenty seven year olds that participated: {twentseven}")
    print(f"Number of twenty eight year olds that participated: {twenteight}")
    print(f"Number of twenty nine year olds that participated: {twentnine}")
    print(f"Number of thirty year olds that participated: {thirt}")  ######
    print(f"Number of thirty one year olds that participated: {thirtone}")
    print(f"Number of thirty two year olds that participated: {thirttwo}")
    print(f"Number of thirty three year olds that participated: {thirtthree}")
    print(f"Number of thirty four year olds that participated: {thirtfour}")
    print(f"Number of thirty five year olds that participated: {thirtfive}")
    print(f"Number of thirty six year olds that participated: {thirtsix}")
    print(f"Number of thirty seven year olds that participated: {thirtseven}")
    print(f"Number of thirty eight seven year olds that participated: {thirteight}")
    print(f"Number of thirty nine year olds that participated: {thirtnine}")
    print(f"Number of fourty year olds that participated: {fourt}") ####
    print(f"Number of fourty one year olds that participated: {fourtone}")
    print(f"Number of fourty two year olds that participated: {fourttwo}")
    print(f"Number of fourty three year olds that participated: {fourtthree}")
    print(f"Number of fourty four year olds that participated: {fourtfour}")
    print(f"Number of fourty five year olds that participated: {fourtfive}")
    print(f"Number of fourty six year olds that participated: {fourtsix}")
    print(f"Number of fourty seven year olds that participated: {fourtseven}")
    print(f"Number of fourty eight year olds that participated: {fourteight}")
    print(f"Number of fourty nine year olds that participated: {fourtnine}")

################## makeGraph ################ .......................
def makeGraph(ans):

    totp, tots, thir, four, fif, six, seven, eigh, nin, twent, twentone, twenttwo, twentthree, twentfour, twentfive, twentsix, twentseven, twenteight, twentnine, thirt, thirtone, thirttwo, thirtthree, thirtfour, thirtfive, thirtsix, thirtseven, thirteight, thirtnine, fourt, fourtone, fourttwo, fourtthree, fourtfour, fourtfive, fourtsix, fourtseven, fourteight, fourtnine = getTotals()
    n1_13, n2_13, n3_13, n4_13, n5_13, n6_13, n1_14, n2_14, n3_14, n4_14, n5_14, n6_14, n1_15, n2_15, n3_15, n4_15, n5_15, n6_15, n1_16, n2_16, n3_16, n4_16, n5_16, n6_16, n1_17, n2_17, n3_17, n4_17, n5_17, n6_17, n1_18, n2_18, n3_18, n4_18, n5_18, n6_18, n1_19, n2_19, n3_19, n4_19, n5_19, n6_19, n1_20, n2_20, n3_20, n4_20, n5_20, n6_20, n1_21, n2_21, n3_21, n4_21, n5_21, n6_21, n1_22, n2_22, n3_22, n4_22, n5_22, n6_22, n1_23, n2_23, n3_23, n4_23, n5_23, n6_23, n1_24, n2_24, n3_24, n4_24, n5_24, n6_24, n1_25, n2_25, n3_25, n4_25, n5_25, n6_25, n1_26, n2_26, n3_26, n4_26, n5_26, n6_26, n1_27, n2_27, n3_27, n4_27, n5_27, n6_27, n1_28, n2_28, n3_28, n4_28, n5_28, n6_28, n1_29, n2_29, n3_29, n4_29, n5_29, n6_29, n1_30, n2_30, n3_30, n4_30, n5_30, n6_30, n1_31, n2_31, n3_31, n4_31, n5_31, n6_31, n1_32, n2_32, n3_32, n4_32, n5_32, n6_32, n1_33, n2_33, n3_33, n4_33, n5_33, n6_33, n1_34, n2_34, n3_34, n4_34, n5_34, n6_34, n1_35, n2_35, n3_35, n4_35, n5_35, n6_35, n1_36, n2_36, n3_36, n4_36, n5_36, n6_36, n1_37, n2_37, n3_37, n4_37, n5_37, n6_37, n1_38, n2_38, n3_38, n4_38, n5_38, n6_38, n1_39, n2_39, n3_39, n4_39, n5_39, n6_39, n1_40, n2_40, n3_40, n4_40, n5_40, n6_40, n1_41, n2_41, n3_41, n4_41, n5_41, n6_41, n1_42, n2_42, n3_42, n4_42, n5_42, n6_42, n1_43, n2_43, n3_43, n4_43, n5_43, n6_43, n1_44, n2_44, n3_44, n4_44, n5_44, n6_44, n1_45, n2_45, n3_45, n4_45, n5_45, n6_45, n1_46, n2_46, n3_46, n4_46, n5_46, n6_46, n1_47, n2_47, n3_47, n4_47, n5_47, n6_47, n1_48, n2_48, n3_48, n4_48, n5_48, n6_48, n1_49, n2_49, n3_49, n4_49, n5_49, n6_49 = calcValues(ans)
   

    NSX = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    NSNV = [n1_13, n1_14, n1_15, n1_16, n1_17, n1_18, n1_19, n1_20, n1_21, n1_22, n1_23, n1_24, n1_25, n1_26, n1_27, n1_28, n1_29, n1_30, n1_31, n1_32, n1_33, n1_34, n1_35, n1_36, n1_37, n1_38, n1_39, n1_40, n1_41, n1_42, n1_43, n1_44, n1_45, n1_46, n1_47, n1_48, n1_49]

    NSX2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    NSV =  [n2_13, n2_14, n2_15, n2_16, n2_17, n2_18, n2_19, n2_20, n2_21, n2_22, n2_23, n2_24, n2_25, n2_26, n2_27, n2_28, n2_29, n2_30, n2_31, n2_32, n2_33, n2_34, n2_35, n2_36, n2_37, n2_38, n2_39, n2_40, n2_41, n2_42, n2_43, n2_44, n2_45, n2_46, n2_47, n2_48, n2_49]


#################
    SX3 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    SNVNH = [n3_13, n3_14, n3_15, n3_16, n3_17, n3_18, n3_19, n3_20, n3_21, n3_22, n3_23, n3_24, n3_25, n3_26, n3_27, n3_28, n3_29, n3_30, n3_31, n3_32, n3_33, n3_34, n3_35, n3_36, n3_37, n3_38, n3_39, n3_40, n3_41, n3_42, n3_43, n3_44, n3_45, n3_46, n3_47, n3_48, n3_49]


    SX4 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    SVNH = [n4_13, n4_14, n4_15, n4_16, n4_17, n4_18, n4_19, n4_20, n4_21, n4_22, n4_23, n4_24, n4_25, n4_26, n4_27, n4_28, n4_29, n4_30, n4_31, n4_32, n4_33, n4_34, n4_35, n4_36, n4_37, n4_38, n4_39, n4_40, n4_41, n4_42, n4_43, n4_44, n4_45, n4_46, n4_47, n4_48, n4_49]


    SX5 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    SNVH = [n5_13, n5_14, n5_15, n5_16, n5_17, n5_18, n5_19, n5_20, n5_21, n5_22, n5_23, n5_24, n5_25, n5_26, n5_27, n5_28, n5_29, n5_30, n5_31, n5_32, n5_33, n5_34, n5_35, n5_36, n5_37, n5_38, n5_39, n5_40, n5_41, n5_42, n5_43, n5_44, n5_45, n5_46, n5_47, n5_48, n5_49]


    SX6 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    SVH = [n6_13, n6_14, n6_15, n6_16, n6_17, n6_18, n6_19, n6_20, n6_21, n6_22, n6_23, n6_24, n6_25, n6_26, n6_27, n6_28, n6_29, n6_30, n6_31, n6_32, n6_33, n6_34, n6_35, n6_36, n6_37, n6_38, n6_39, n6_40, n6_41, n6_42, n6_43, n6_44, n6_45, n6_46, n6_47, n6_48, n6_49]

    

    # Gen bar graph use
    n1 = ["not sick no vac", "not sick w vac","sick no vac not hosp", "sick w vac not hosp", "sick no vac & hosp", "sick w vac & hosp",]
   ### 13 year old bar graph
    S13 = [n1_13, n2_13, n3_13, n4_13, n5_13, n6_13]
    fig = plt1.figure(figsize=(15, 5))

    plt1.bar(n1, S13, color="grey", width=0.6)
    plt1.ylabel("No. of participants")
    plt1.xlabel("13 year olds status: sick vs vaccine")
    plt1.suptitle("Data on 13 year olds")
    plt1.show()

    ### 14 year old bar graph
    S14 = [n1_14, n2_14, n3_14, n4_14, n5_14, n6_14]
    fig = plt2.figure(figsize=(15, 5))

    plt2.bar(n1, S14, color="red", width=0.6)
    plt2.ylabel("No. of participants")
    plt2.xlabel("14 year olds status: sick vs vaccine")
    plt2.suptitle("Data on 14 year olds")
    plt2.show()

    ### 15 year old bar graph
    S15 = [n1_15, n2_15, n3_15, n4_15, n5_15, n6_15]
    fig = plt3.figure(figsize=(15, 5))

    plt3.bar(n1, S15, color="purple", width=0.6)
    plt3.ylabel("No. of participants")
    plt3.xlabel("15 year olds status: sick vs vaccine")
    plt3.suptitle("Data on 15 year olds")
    plt3.show()

    ### 16 year old bar graph
    S16 = [n1_16, n2_16, n3_16, n4_16, n5_16, n6_16]
    fig = plt4.figure(figsize=(15, 5))

    plt4.bar(n1, S16, color="blue", width=0.6)
    plt4.ylabel("No. of participants")
    plt4.xlabel("16 year olds status: sick vs vaccine")
    plt4.suptitle("Data on 16 year olds")
    plt4.show()

    ### 17 year old bar graph
    S17 = [n1_17, n2_17, n3_17, n4_17, n5_17, n6_17]
    fig = plt5.figure(figsize=(15, 5))

    plt5.bar(n1, S17, color="pink", width=0.6)
    plt5.ylabel("No. of participants")
    plt5.xlabel("17 year olds status: sick vs vaccine")
    plt5.suptitle("Data on 17 year olds")
    plt5.show()

    ### 18 year old bar graph
    S18 = [n1_18, n2_18, n3_18, n4_18, n5_18, n6_18]
    fig = plt6.figure(figsize=(15, 5))

    plt6.bar(n1, S18, color="yellow", width=0.6)
    plt6.ylabel("No. of participants")
    plt6.xlabel("18 year olds status: sick vs vaccine")
    plt6.suptitle("Data on 18 year olds")
    plt6.show()

    ### 19 year old bar graph
    S19 = [n1_19, n2_19, n3_19, n4_19, n5_19, n6_19]
    fig = plt7.figure(figsize=(15, 5))

    plt7.bar(n1, S19, color="yellow", width=0.6)
    plt7.ylabel("No. of participants")
    plt7.xlabel("19 year olds status: sick vs vaccine")
    plt7.suptitle("Data on 19 year olds")
    plt7.show()

    ### 20 year old bar graph
    S20 = [n1_20, n2_20, n3_20, n4_20, n5_20, n6_20]
    fig = plt8.figure(figsize=(15, 5))

    plt8.bar(n1, S20, color="yellow", width=0.6)
    plt8.ylabel("No. of participants")
    plt8.xlabel("20 year olds status: sick vs vaccine")
    plt8.suptitle("Data on 20 year olds")
    plt8.show()

    ### 21 year old bar graph
    S21 = [n1_21, n2_21, n3_21, n4_21, n5_21, n6_21]
    fig = plt9.figure(figsize=(15, 5))

    plt9.bar(n1, S21, color="yellow", width=0.6)
    plt9.ylabel("No. of participants")
    plt9.xlabel("21 year olds status: sick vs vaccine")
    plt9.suptitle("Data on 21 year olds")
    plt9.show()

    ### 22 year old bar graph
    S22 = [n1_22, n2_22, n3_22, n4_22, n5_22, n6_22]
    fig = plt10.figure(figsize=(15, 5))

    plt10.bar(n1, S22, color="yellow", width=0.6)
    plt10.ylabel("No. of participants")
    plt10.xlabel("22 year olds status: sick vs vaccine")
    plt10.suptitle("Data on 22 year olds")
    plt10.show()

    ### 23 year old bar graph
    S23 = [n1_23, n2_23, n3_23, n4_23, n5_23, n6_23]
    fig = plt11.figure(figsize=(15, 5))

    plt11.bar(n1, S23, color="yellow", width=0.6)
    plt11.ylabel("No. of participants")
    plt11.xlabel("23 year olds status: sick vs vaccine")
    plt11.suptitle("Data on 23 year olds")
    plt11.show()

    ### 24 year old bar graph
    S24 = [n1_24, n2_24, n3_24, n4_24, n5_24, n6_24]
    fig = plt12.figure(figsize=(15, 5))

    plt12.bar(n1, S24, color="yellow", width=0.6)
    plt12.ylabel("No. of participants")
    plt12.xlabel("24 year olds status: sick vs vaccine")
    plt12.suptitle("Data on 24 year olds")
    plt12.show()

    ### 25 year old bar graph
    S25 = [n1_25, n2_25, n3_25, n4_25, n5_25, n6_25]
    fig = plt13.figure(figsize=(15, 5))

    plt13.bar(n1, S25, color="yellow", width=0.6)
    plt13.ylabel("No. of participants")
    plt13.xlabel("25 year olds status: sick vs vaccine")
    plt13.suptitle("Data on 25 year olds")
    plt13.show()

    ### 26 year old bar graph
    S26 = [n1_26, n2_26, n3_26, n4_26, n5_26, n6_26]
    fig = plt14.figure(figsize=(15, 5))

    plt14.bar(n1, S26, color="yellow", width=0.6)
    plt14.ylabel("No. of participants")
    plt14.xlabel("26 year olds status: sick vs vaccine")
    plt14.suptitle("Data on 26 year olds")
    plt14.show()

    ### 27 year old bar graph
    S27 = [n1_27, n2_27, n3_27, n4_27, n5_27, n6_27]
    fig = plt15.figure(figsize=(15, 5))

    plt15.bar(n1, S27, color="yellow", width=0.6)
    plt15.ylabel("No. of participants")
    plt15.xlabel("27 year olds status: sick vs vaccine")
    plt15.suptitle("Data on 27 year olds")
    plt15.show()

    ### 28 year old bar graph
    S28 = [n1_28, n2_28, n3_28, n4_28, n5_28, n6_28]
    fig = plt16.figure(figsize=(15, 5))

    plt16.bar(n1, S28, color="yellow", width=0.6)
    plt16.ylabel("No. of participants")
    plt16.xlabel("28 year olds status: sick vs vaccine")
    plt16.suptitle("Data on 28 year olds")
    plt16.show()

    ### 29 year old bar graph
    S29 = [n1_29, n2_29, n3_29, n4_29, n5_29, n6_29]
    fig = plt17.figure(figsize=(15, 5))

    plt17.bar(n1, S29, color="yellow", width=0.6)
    plt17.ylabel("No. of participants")
    plt17.xlabel("29 year olds status: sick vs vaccine")
    plt17.suptitle("Data on 29 year olds")
    plt17.show()

    ### 30 year old bar graph
    S30 = [n1_30, n2_30, n3_30, n4_30, n5_30, n6_30]
    fig = plt18.figure(figsize=(19, 5))

    plt18.bar(n1, S30, color="yellow", width=0.20)
    plt18.ylabel("No. of participants")
    plt18.xlabel("30 year olds status: sick vs vaccine")
    plt18.suptitle("Data on 30 year olds")
    plt18.show()

    ### 31 year old bar graph
    S31 = [n1_31, n2_31, n3_31, n4_31, n5_31, n6_31]
    fig = plt19.figure(figsize=(19, 5))

    plt19.bar(n1, S31, color="yellow", width=0.20)
    plt19.ylabel("No. of participants")
    plt19.xlabel("31 year olds status: sick vs vaccine")
    plt19.suptitle("Data on 31 year olds")
    plt19.show()

    # 32 year olds
    S32 = [n1_32, n2_32, n3_32, n4_32, n5_32, n6_32]
    fig = plt20.figure(figsize=(19, 5))

    plt20.bar(n1, S32, color="yellow", width=0.20)
    plt20.ylabel("No. of participants")
    plt20.xlabel("32 year olds status: sick vs vaccine")
    plt20.suptitle("Data on 32 year olds")
    plt20.show()

    # 33 year olds
    S33 = [n1_33, n2_33, n3_33, n4_33, n5_33, n6_33]
    fig = plt21.figure(figsize=(19, 5))

    plt21.bar(n1, S33, color="yellow", width=0.20)
    plt21.ylabel("No. of participants")
    plt21.xlabel("33 year olds status: sick vs vaccine")
    plt21.suptitle("Data on 33 year olds")
    plt21.show()

    # 34 year olds
    S34 = [n1_34, n2_34, n3_34, n4_34, n5_34, n6_34]
    fig = plt22.figure(figsize=(19, 5))

    plt22.bar(n1, S34, color="yellow", width=0.20)
    plt22.ylabel("No. of participants")
    plt22.xlabel("34 year olds status: sick vs vaccine")
    plt22.suptitle("Data on 34 year olds")
    plt22.show()

    # 35 year olds
    S35 = [n1_35, n2_35, n3_35, n4_35, n5_35, n6_35]
    fig = plt23.figure(figsize=(19, 5))

    plt23.bar(n1, S35, color="yellow", width=0.20)
    plt23.ylabel("No. of participants")
    plt23.xlabel("35 year olds status: sick vs vaccine")
    plt23.suptitle("Data on 35 year olds")
    plt23.show()

    # 36 year olds
    S36 = [n1_36, n2_36, n3_36, n4_36, n5_36, n6_36]
    fig = plt24.figure(figsize=(19, 5))

    plt24.bar(n1, S36, color="yellow", width=0.20)
    plt24.ylabel("No. of participants")
    plt24.xlabel("36 year olds status: sick vs vaccine")
    plt24.suptitle("Data on 36 year olds")
    plt24.show()

    # 37 year olds
    S37 = [n1_37, n2_37, n3_37, n4_37, n5_37, n6_37]
    fig = plt25.figure(figsize=(19, 5))

    plt25.bar(n1, S37, color="yellow", width=0.20)
    plt25.ylabel("No. of participants")
    plt25.xlabel("37 year olds status: sick vs vaccine")
    plt25.suptitle("Data on 37 year olds")
    plt25.show()

    # 38 year olds
    S38 = [n1_38, n2_38, n3_38, n4_38, n5_38, n6_38]
    fig = plt26.figure(figsize=(19, 5))

    plt26.bar(n1, S38, color="yellow", width=0.20)
    plt26.ylabel("No. of participants")
    plt26.xlabel("38 year olds status: sick vs vaccine")
    plt26.suptitle("Data on 38 year olds")
    plt26.show()

    # 39 year olds
    S39 = [n1_39, n2_39, n3_39, n4_39, n5_39, n6_39]
    fig = plt27.figure(figsize=(19, 5))

    plt27.bar(n1, S39, color="yellow", width=0.20)
    plt27.ylabel("No. of participants")
    plt27.xlabel("39 year olds status: sick vs vaccine")
    plt27.suptitle("Data on 39 year olds")
    plt27.show()

    # 40 year olds
    S40 = [n1_40, n2_40, n3_40, n4_40, n5_40, n6_40]
    fig = plt28.figure(figsize=(19, 5))

    plt28.bar(n1, S40, color="yellow", width=0.20)
    plt28.ylabel("No. of participants")
    plt28.xlabel("40 year olds status: sick vs vaccine")
    plt28.suptitle("Data on 40 year olds")
    plt28.show()

    # 41 year olds
    S41 = [n1_41, n2_41, n3_41, n4_41, n5_41, n6_41]
    fig = plt29.figure(figsize=(19, 5))

    plt29.bar(n1, S41, color="yellow", width=0.20)
    plt29.ylabel("No. of participants")
    plt29.xlabel("41 year olds status: sick vs vaccine")
    plt29.suptitle("Data on 41 year olds")
    plt29.show()

    # 42 year olds
    S42 = [n1_42, n2_42, n3_42, n4_42, n5_42, n6_42]
    fig = plt30.figure(figsize=(19, 5))

    plt30.bar(n1, S42, color="yellow", width=0.20)
    plt30.ylabel("No. of participants")
    plt30.xlabel("42 year olds status: sick vs vaccine")
    plt30.suptitle("Data on 42 year olds")
    plt30.show()

    # 43 year olds
    S43 = [n1_43, n2_43, n3_43, n4_43, n5_43, n6_43]
    fig = plt31.figure(figsize=(19, 5))

    plt31.bar(n1, S43, color="yellow", width=0.20)
    plt31.ylabel("No. of participants")
    plt31.xlabel("43 year olds status: sick vs vaccine")
    plt31.suptitle("Data on 43 year olds")
    plt31.show()

    # 44 year olds
    S44 = [n1_44, n2_44, n3_44, n4_44, n5_44, n6_44]
    fig = plt32.figure(figsize=(19, 5))

    plt32.bar(n1, S44, color="yellow", width=0.20)
    plt32.ylabel("No. of participants")
    plt32.xlabel("44 year olds status: sick vs vaccine")
    plt32.suptitle("Data on 44 year olds")
    plt32.show()

    # 45 year olds
    S45 = [n1_45, n2_45, n3_45, n4_45, n5_45, n6_45]
    fig = plt33.figure(figsize=(19, 5))

    plt33.bar(n1, S45, color="yellow", width=0.20)
    plt33.ylabel("No. of participants")
    plt33.xlabel("45 year olds status: sick vs vaccine")
    plt33.suptitle("Data on 45 year olds")
    plt33.show()

    # 46 year olds
    S46 = [n1_46, n2_46, n3_46, n4_46, n5_46, n6_46]
    fig = plt34.figure(figsize=(19, 5))

    plt34.bar(n1, S46, color="yellow", width=0.20)
    plt34.ylabel("No. of participants")
    plt34.xlabel("46 year olds status: sick vs vaccine")
    plt34.suptitle("Data on 46 year olds")
    plt34.show()

    # 47 year olds
    S47 = [n1_47, n2_47, n3_47, n4_47, n5_47, n6_47]
    fig = plt35.figure(figsize=(19, 5))

    plt35.bar(n1, S47, color="yellow", width=0.20)
    plt35.ylabel("No. of participants")
    plt35.xlabel("47 year olds status: sick vs vaccine")
    plt35.suptitle("Data on 47 year olds")
    plt35.show()

    # 48 year olds
    S48 = [n1_48, n2_48, n3_48, n4_48, n5_48, n6_48]
    fig = plt36.figure(figsize=(19, 5))

    plt36.bar(n1, S48, color="yellow", width=0.20)
    plt36.ylabel("No. of participants")
    plt36.xlabel("48 year olds status: sick vs vaccine")
    plt36.suptitle("Data on 48 year olds")
    plt36.show()

    # 49 year olds
    S49 = [n1_49, n2_49, n3_49, n4_49, n5_49, n6_49]
    fig = plt37.figure(figsize=(19, 5))

    plt37.bar(n1, S49, color="yellow", width=0.20)
    plt37.ylabel("No. of participants")
    plt37.xlabel("49 year olds status: sick vs vaccine")
    plt37.suptitle("Data on 49 year olds")
    plt37.show()




    #########total for personal###########
    
    TNSNV1 = n1_13 + n1_14 + n1_15 + n1_16 + n1_17 + n1_18
  
    TNSV1 = n2_13 + n2_14 + n2_15 + n2_16 + n2_17 + n2_18

    TSNVNH1 = n3_13 + n3_14 + n3_15 + n3_16 + n3_17 + n3_18

    TSVNH1 = n4_13 + n4_14 + n4_15 + n4_16 + n4_17 + n4_18
    
    TSNVH1 = n5_13 + n5_14 + n5_15 + n5_16 + n5_17 + n5_18

    TSVH1 = n6_13 + n6_14 + n6_15 + n6_16 + n6_17 + n6_18
   
    # Totals Bar Graph (teens)
    TNS1 =[TNSNV1, TNSV1, TSNVNH1,TSVNH1,TSNVH1, TSVH1]
    fig = plt7.figure(figsize=(15,5))
   
    plt7.bar(n1, TNS1, color = "aqua", width = 0.6)
    plt7.ylabel("Total: number of students sick")
    plt7.xlabel("By Data Type: Grouped Data (13-18) ")
    plt7.suptitle("School Data by Not sick/sick and by Vac and by not hospitalized/hospitalized(Total)")
    plt7.show()

    TNSNV2 = n1_19 + n1_20 + n1_21 + n1_22 + n1_23 + n1_24 + n1_25 + n1_26 + n1_27 + n1_28 + n1_29

    TSNV2 = n2_19 + n2_20 + n2_21 + n2_22 + n2_23 + n2_24 + n2_25 + n2_26 + n2_27 + n2_28 + n2_29

    TSNVNH2 = n3_19 + n3_20 + n3_21 + n3_22 + n3_23 + n3_24 + n3_25 + n3_26 + n3_27 + n3_28 + n3_29

    TSVNH2 = n4_19 + n4_20 + n4_21 + n4_22 + n4_23 + n4_24 + n4_25 + n4_26 + n4_27 + n4_28 + n4_29

    TSNVH2 = n5_19 + n5_20 + n5_21 + n5_22 + n5_23 + n5_24 + n5_25 + n5_26 + n5_27 + n5_28 + n5_29

    TSVH2 = n6_19 + n6_20 + n6_21 + n6_22 + n6_23 + n6_24 + n6_25 + n6_26 + n6_27 + n6_28 + n6_29


    # Totals Bar Graph (19-29)
    TNS2 =[TNSNV2, TSNV2, TSNVNH2,TSVNH2,TSNVH2, TSVH2]
    fig = plt42.figure(figsize=(15,5))
       
    plt42.bar(n1, TNS2, color = "blue", width = 0.6)
    plt42.ylabel("Total: number of 20yrs age group sick")
    plt42.xlabel("By Data Type: Grouped Data (19-29) ")
    plt42.suptitle("20yrs old Data by Not sick/sick and by Vac and by not hospitalized/hospitalized(Total)")
    plt42.show()

    TNSNV3 = n1_30 + n1_31 + n1_32 + n1_33 + n1_34 + n1_35 + n1_36 + n1_37 + n1_38 + n1_39
    
    TSNV3 = n2_30 + n2_31 + n2_32 + n2_33 + n2_34 + n2_35 + n2_36 + n2_37 + n2_38 + n2_39
    
    TSNVNH3 = n3_30 + n3_31 + n3_32 + n3_33 + n3_34 + n3_35 + n3_36 + n3_37 + n3_38 + n3_39
    
    TSVNH3 = n4_30 + n4_31 + n4_32 + n4_33 + n4_34 + n4_35 + n4_36 + n4_37 + n4_38 + n4_39
    
    TSNVH3 = n5_30 + n5_31 + n5_32 + n5_33 + n5_34 + n5_35 + n5_36 + n5_37 + n5_38 + n5_39

    TSVH3 = n6_30 + n6_31 + n6_32 + n6_33 + n6_34 + n6_35 + n6_36 + n6_37 + n6_38 + n6_39

    # Totals Bar Graph (30-39)
    TNS3 =[TNSNV3, TSNV3, TSNVNH3,TSVNH3,TSNVH3, TSVH3]
    fig = plt43.figure(figsize=(15,5))
       
    plt43.bar(n1, TNS3, color = "red", width = 0.6)
    plt43.ylabel("Total: number of 30yrs age group sick")
    plt43.xlabel("By Data Type: Grouped Data (30-39) ")
    plt43.suptitle("30yrs old Data by Not sick/sick and by Vac and by not hospitalized/hospitalized(Total)")
    plt43.show()

    TNSNV4 = n1_39 + n1_40 + n1_41 + n1_42 + n1_43 + n1_44 + n1_45 + n1_46 + n1_47 + n1_48 + n1_49

    TNV4 = n2_39 + n2_40 + n2_41 + n2_42 + n2_43 + n2_44 + n2_45 + n2_46 + n2_47 + n2_48 + n2_49

    TNVNH4 = n3_39 + n3_40 + n3_41 + n3_42 + n3_43 + n3_44 + n3_45 + n3_46 + n3_47 + n3_48 + n3_49

    TVNH4 = n4_39 + n4_40 + n4_41 + n4_42 + n4_43 + n4_44 + n4_45 + n4_46 + n4_47 + n4_48 + n4_49

    TNVH4 = n5_39 + n5_40 + n5_41 + n5_42 + n5_43 + n5_44 + n5_45 + n5_46 + n5_47 + n5_48 + n5_49

    TVH4 = n6_39 + n6_40 + n6_41 + n6_42 + n6_43 + n6_44 + n6_45 + n6_46 + n6_47 + n6_48 + n6_49

    # Totals Bar Graph (40-49)
    TNS4 =[TNSNV4, TNV4, TNVNH4,TVNH4,TNVH4, TVH4]
    fig = plt44.figure(figsize=(15,5))
       
    plt44.bar(n1, TNS4, color = "green", width = 0.6)
    plt44.ylabel("Total: number of 40yrs age group sick")
    plt44.xlabel("By Data Type: Grouped Data (40-49) ")
    plt44.suptitle("40 yrs old Data by Not sick/sick and by Vac and by not hospitalized/hospitalized(Total)")
    plt44.show()

    TNSNV5 =  n1_13 + n1_14 + n1_15 + n1_16 + n1_17 + n1_18+n1_19 + n1_20 + n1_21 + n1_22 + n1_23 + n1_24 + n1_25 + n1_26 + n1_27 + n1_28 + n1_29 + n1_30 + n1_31 + n1_32 + n1_33 + n1_34 + n1_35 + n1_36 + n1_37 + n1_38 + n1_39 + n1_40 + n1_41 + n1_42 + n1_43 + n1_44 + n1_45 + n1_46 + n1_47 + n1_48 + n1_49# total ages for no vacc

    TNSV5 =   n2_13 + n2_14 + n2_15 + n2_16 + n2_17 + n2_18 +  n2_19 + n2_20 + n2_21 + n2_22 + n2_23 + n2_24 + n2_25 + n2_26 + n2_27 + n2_28 + n2_29 + n2_30 + n2_31 + n2_32 + n2_33 + n2_34 + n2_35 + n2_36 + n2_37 + n2_38 + n2_39 +  n2_40 + n2_41 + n2_42 + n2_43 + n2_44 + n2_45 + n2_46 + n2_47 + n2_48 + n2_49

    TNSB5 =  n3_13+ n3_14+ n3_15+ n3_16+ n3_17+ n3_18 + n3_19 + n3_20 + n3_21 + n3_22 + n3_23 + n3_24 + n3_25 + n3_26 + n3_27 + n3_28 + n3_29 +  n3_30 + n3_31 + n3_32 + n3_33 + n3_34 + n3_35 + n3_36 + n3_37 + n3_38 + n3_39 + n3_40 + n3_41 + n3_42 + n3_43 + n3_44 + n3_45 + n3_46 + n3_47 + n3_48 + n3_49

    TSNVNH5 = n4_13+ n4_14+ n4_15+ n4_16+ n4_17+ n4_18 + n4_19 + n4_20 + n4_21 + n4_22 + n4_23 + n4_24 + n4_25 + n4_26 + n4_27 + n4_28 + n4_29 +  n4_30 + n4_31 + n4_32 + n4_33 + n4_34 + n4_35 + n4_36 + n4_37 + n4_38 + n4_39 + n4_40 + n4_41 + n4_42 + n4_43 + n4_44 + n4_45 + n4_46 + n4_47 + n4_48 + n4_49

    TSVNH5 = n5_13+ n5_14+ n5_15+ n5_16+ n5_17+ n5_18 +  n5_19 + n5_20 + n5_21 + n5_22 + n5_23 + n5_24 + n5_25 + n5_26 + n5_27 + n5_28 + n5_29 +   n5_30 + n5_31 + n5_32 + n5_33 + n5_34 + n5_35 + n5_36 + n5_37 + n5_38 + n5_39 + n5_40 + n5_41 + n5_42 + n5_43 + n5_44 + n5_45 + n5_46 + n5_47 + n5_48 + n5_49

    TSBNH5 = n6_13+ n6_14+ n6_15+ n6_16+ n6_17+ n6_18 +  n6_19 + n6_20 + n6_21 + n6_22 + n6_23 + n6_24 + n6_25 + n6_26 + n6_27 + n6_28 + n6_29 +   n6_30 + n6_31 + n6_32 + n6_33 + n6_34 + n6_35 + n6_36 + n6_37 + n6_38 + n6_39 +  n6_40 + n6_41 + n6_42 + n6_43 + n6_44 + n6_45 + n6_46 + n6_47 + n6_48 + n6_49

	# Totals Bar Graph (40-49)
    TNS5 =[TNSNV5, TNSV5, TNSB5, TSNVNH5, TSVNH5, TSBNH5]

    fig = plt51.figure(figsize=(20,5))
       
    plt51.bar(n1, TNS5, color = "green", width = 0.20)
    plt51.ylabel("Total: number of 13-49 age group sick")
    plt51.xlabel("By Data Type: Grouped Data (13-49) ")
    plt51.suptitle("13-49 yrs old Data by Not sick/sick and by Vac and by not hospitalized/hospitalized(Total)")
    plt51.show()


#############media################
    ### National Graph 
    TN = [333.3, 158.1,175.2,323.3,10,110000]
    n2 = ["Nat Tot(333.3m)","Nat Tot No Vac(158.1m)", "Nat Tot Vac(175.2m)", "Nat Tot Not Sick(323.3m)", "Nat Tot Sick(10m)", "Nat Tot hospitalized(110000)"]
    fig = plt42.figure(figsize=(20,5))
   
    plt42.bar(n2, TN, color = "Brown", width = 0.20)
    plt42.ylabel("No. of participant (13-49)")
    plt42.xlabel("Total/Vacc/nosickness/sickness/hospitalization Data")
    plt42.suptitle("National Media Flu Data(13-49) in the US")
    plt42.show()

     ### County Graph 
    TC = [ 421750, 420063,1687, 421485, 265, 1 ] 

    n3 = ["Cam Tot(421750)","Cam Tot No Vac(420063)", "Cam Tot Vac(1687)", "Cam Tot Not Sick(421485)", "Cam Tot Sick(265)", "Cam Tot hospitalized(1)"] 
    fig = plt46.figure(figsize=(30,5))
   
    plt46.bar(n3, TC, color = "orange", width = 0.20)
    plt46.ylabel("No. of participant (13-49)")
    plt46.xlabel("Total/Vacc/nosickness/sickness/hospitalization Data")
    plt46.suptitle("Cameron County Media Flu Data(13-49)")
    plt46.show()


   
     ### Local High School Graph 
    TH = [2336,1418, 918, 799,1537]
    n4 = ["Loc HS Tot(2336)", "Loc HS Tot No Vac(1418)", "Loc HS Tot Vac(918)","Loc HS Tot No Sick(799)", "Loc HS Tot Sick(1537)"]
    fig = plt50.figure(figsize=(20,5))
   
    plt50.bar(n4, TH, color = "black", width = 0.20)
    plt50.ylabel("No. of students (13-49)")
    plt50.xlabel("Total/Vacc/nosickness/sickness/hospitalization Data")
    plt50.suptitle("Local High School Media Flu Data(13-49)")
    plt50.show()


    
def compData():
    vacc1 =175200000
    novacc1 = 158100000
    sick1 = 10000000
    totnatpeople1 = vacc1 + novacc1 # total sample of people
    pernatsick1 = float((sick1/totnatpeople1)*100) # percent national sick out of total
    totp, tots, thir, four, fif, six, seven, eigh, nin, twent, twentone, twenttwo, twentthree, twentfour, twentfive, twentsix, twentseven, twenteight, twentnine, thirt, thirtone, thirttwo, thirtthree, thirtfour, thirtfive, thirtsix, thirtseven, thirteight, thirtnine, fourt, fourtone, fourttwo, fourtthree, fourtfour, fourtfive, fourtsix, fourtseven, fourteight, fourtnine = getTotals()
    permysampsick1 = float((tots/totp)*100) #tot percent my sample sick out of total sample people
    print(f"\n\nNational data on 13-49 vaccinated: {vacc}")
    print(f"\n\nNational data on 13-49 not vaccinated: {novacc}")
    print(f"\n\nTotal number of 13-49 with collected data (vaccinated, no vaccine) : {totnatpeople}")
    print(f"\n\nNational data on 13-49 that got Flu: {sick}")
    a = 60
    plt3.scatter(NSX, NSNV, a, c='red', marker='*',)
    plt3.scatter(NSX2, NSV, a, c='blue', marker='*')
    plt3.scatter(NSX3, NSVB, a, c='purple', marker='*',)


    plt3.xlim(12,19)
    plt3.ylim(0,7)

    plt2.title('National data of High School Student\nred-no vaccine, blue-vaccine')

    plt3.xlabel('Age')
    plt3.ylabel('Vaccination status')

    plt3.show()




 
   

   
################## firstCheck ###############
# Creates a Totals io file if it doesn't exist.
def firstCheck():
    empty = "0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0"
    try:   # checks to see if the file is empty, if not empty then does nothing
        with open("Totals.txt", "r+") as f:
            one_char = f.read(1)
            if not one_char:
                print("")
    except: # creates the file if empty and populates with 0's
        with open("Totals.txt", "w") as f:
            f.write(empty)


main()

