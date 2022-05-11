print("hello, welcome to the game")
ans= input("Are you ready to play [yes/no]: ")
score = 0
total_q = 5
if ans.lower() =="yes":
    ans= input("does ty own a pair of crocs shoes? ")
    if ans.lower() == "yes":
        score += 1
        print("Correct")
    else:
        print("incorrect")

    ans= input("the avalanche hockey team last won a cup in 2001, however they have been a bottom 20% team for the last 23 years. until recently the avalache are a good hockey team. are the avalanche going to win a cup this year? ")
    if ans.lower() == "yes":
        score += 1
        print("Correct")
    else:
        print("incorrect")
 


    ans= input("what is tys favorite movie ?")
    if ans.lower() == "meet the robinsons":
        score += 1
        print("Correct")
    else:
        print("incorrect")

        

    ans= input("what does ty drink every morning, green tea, coffee, or orange juice ?")
    if ans.lower() == "coffee":
        score += 1
        print("Correct")
    else:
        print("incorrect")


    ans= input("will nikola jokic win MVP this year ?")
    if ans.lower() == "yes":
        score += 1
        print("Correct")
    else:
        print("incorrect")
        
        
print("You have got", score, " question right. thanks for playing ")
mark = (score/total_q) * 100

print("mark: ", str(mark) + '%')
print('goodbye')
