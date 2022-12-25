questions = ["What is the capital of Libya?","Who was the commander-in-chief of US Army from 1930 to 1935?","Who was the 3rd Army chief of India?"]
opt = ["Options: \n A)Tripoli\n B)Sabha" ,"Options: \n A)General.Malin Craig \n B)General.Douglas Macarthur","Options: \n A)General. K.S Thimmaya\n B)General. Maharaja rajendra Singhji Jajeda"]
ans = ["A","B","B"]
pamt = 0
cr  = 0
for i in range(3):
    print(questions[i])
    print(opt[i])
    an = str(input("Enter your choice = "))
    if an==ans[i]:
        print("You are Correct")
        pamt = pamt + 500000
        cr+=1
        print(f"Your Total Prize money has became {pamt}")
    else:
        print("You are Wrong")
        pamt = 0
        print(f"Your Total Prize money has became {pamt}")

print(f"{cr} of your answers were correct and you will take Rs.{pamt} to Home.")