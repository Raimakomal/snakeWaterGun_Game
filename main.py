import random
lst=['snake','water','gun']
attempts=1
scr_of_cont=0
scr_of_cpo=0
print("lets start the game.....are you ready..you must be!!")
while attempts<=10:
    
    print("Welcome RAIMA KOMAL! Let's start the game.")
    cont=input("Enter your choice: Gun OR snake OR water?  ")
    cpo=random.choice(lst)
    print("my choice:",cpo)
    if cont=='snake' and cpo=='water':
        print("cont:win")
        scr_of_cont+=1
    elif cpo=='snake' and cont=='water':
        print("cpo:win")
        scr_of_cpo+=1

    if cont=='snake' and cpo=='gun':
        print("cpo:win")
        scr_of_cpo+=1
    elif cpo=='snake' and cont=='gun':
        print("cont:win")
        scr_of_cont+=1 

    if cont=='gun' and cpo=='water':
        print("cpo:win")
        scr_of_cpo+=1 
    elif cpo=='gun' and cont=='water':
        print("cont:win")
        scr_of_cont+=1
        
    if cont==cpo:
        print("no point")

    print(f"{10-attempts} is left out of 10 ")
    attempts+=1

print("Game over....")  
if scr_of_cont>scr_of_cpo:
    print('Raima wins........') 
elif scr_of_cont==scr_of_cpo:
    print("it becomes a tie........")    
else:
    print('cpo wins..........')     
print(f"Final score of cpo:{scr_of_cpo}")        
print(f"Final score of cont:{scr_of_cont}")        