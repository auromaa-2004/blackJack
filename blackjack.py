import random
import os


print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/      ''')


def blackjack():
    # next_game=input("Do you want to play the game? y or n").lower()
    # if next_game=="y":
    #     os.system('cls')
    # elif next_game=="n":
    #     print("Thank you")    
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    user_card1=cards[random.randint(0,12)]
    user_card2=cards[random.randint(0,12)]
    me=[]
    me.append(user_card1)
    me.append(user_card2)
    user_current_score=me[0]+me[1]
    print(f"Your cards:{me}, current score={user_current_score}")
    comp_card1=cards[random.randint(0,12)]
    comp=[]
    comp.append(comp_card1)
    comp_score=comp[0]
    comp_str=""
    user_str=""
    print(f"Computer's first card={' '.join([str(elem) for elem in comp])}")


    if user_current_score!=21:
        next_input=input("Type 'y' to get another card, type n to pass")
        total_score=0
        total_comp=0
        next=[]
        if next_input== "y":
            next=[]
            
            while (next_input!= "n") and (total_score<21):
                current_score=0
                next.append(cards[random.randint(0,12)])
                x=len(next)
                for i in range(0,x):
                    current_score=current_score+next[i]
                    total_score=current_score+user_current_score        
                print(f"Your cards:{[','.join([str(elem) for elem in me])+','+','.join([str(elem) for elem in next])]}, current score={total_score}")
                print(f"Computer's first card={' '.join([str(elem) for elem in comp])}")
                if total_score>21:
                    user_str=user_str+"you lose"
                    print("you lose")
                    break
                elif total_score==21:
                    user_str=user_str+"you win"
                    print("you win")
                    break    
                next_input=input("Type 'y' to get another card, type n to pass\n")
            
            if user_str!="you lose" and user_str!="you win":
                next_comp=[]
                total_comp=0
                y=len(next_comp)
                while total_comp<17 and y<4:
                    current_comp_score=0
                    next_comp.append(cards[random.randint(0,12)])
                    y=len(next_comp)
                    for j in range(0,y):
                        current_comp_score=current_comp_score+next_comp[j]
                        total_comp=comp_score+current_comp_score
                print(f"Your final hand:{[','.join([str(elem) for elem in me])+','+','.join([str(elem) for elem in next])]}, final score={total_score}")
                print(f"Computer's final hand={','.join([str(elem) for elem in comp])+','+','.join([str(elem) for elem in next_comp])}, final score={total_comp}")    

                if total_comp<=21 and total_comp>total_score:
                    print("You Lose")
                elif total_comp>21:
                    print("You Win")   
                elif total_score>21:
                    print("You Lose")
                elif total_score<=21 and total_score>total_comp:   
                    print("You Win") 
                elif total_score==total_comp:
                    print("Draw")
                


        elif next_input=="n":
            next_comp=[]
            total_comp=0
            y=len(next_comp)
            while total_comp<17 and y<4:
                current_comp_score=0
                next_comp.append(cards[random.randint(0,12)])
                y=len(next_comp)
                for j in range(0,y):
                    current_comp_score=current_comp_score+next_comp[j]
                    total_comp=comp_score+current_comp_score

            print(f"Your final hand:{[','.join([str(elem) for elem in me])]}, final score={user_current_score}")
            print(f"Computer's final hand={','.join([str(elem) for elem in comp])+','+','.join([str(elem) for elem in next_comp])}, final score={total_comp}")    

            if total_comp<=21 and total_comp>user_current_score:
                print("You lose")
            elif total_comp>21:
                print("you win")   
            elif user_current_score>total_comp:
                print("you win") 
            elif user_current_score==total_comp:
                print("Draw")    

    if user_current_score==21:
        print("You won")

    # next_game=input("Do you want to play the game again? y or n").lower()
    # if next_game=="n":
    #     print("Thank you!")
    # elif next_game=="y":
    #     os.system('cls')
    # blackjack()

blackjack()