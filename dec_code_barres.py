#T=("3141728704713")     test
#J=("1")                 Jambon
#B=("2")                 beure
#S=("3")                 Saucisson
#P=("4")                 pain
#F=("5")                 fanta



code=["3141728704713" , "1" , "2" ,"3" , "4" , "5"]
elem=["Test" , "Jambon" , "Beurre" , "Saucisson" , "Pain" , "Fanta"]
           
Wil=1
x=0
b=0

while Wil==1:
    code_input =input ("Scan")
    try:
       val = str(code_input)
    except ValueError:
       print("ValueError")

    while x<=6:
        if x!=6 and code_input == code[x]:
            print( elem[x])
            if b==1:
                cursor.execute("""INSERT INTO aliment (aliment) VALUES(%s(element))""", elem[x])


            
            break
        if x==6:
            print ("non définie")
        x=x+1
    x=0
