from random import randint
play = 'y'
while play == 'y' or play == 'yes':
    score = 0
    for p in range (5):
        number = randint (1, 3)
        print ("What is my number?")
        user_input = input ("1,2,or 3... ")
        while user_input not in ['1','2','3']:
            user_input = input ('The number has to be 1, 2,or 3... ')
        user_number = int(user_input)
        if number == user_number:
            print ("Correct it was" , number)
            score = score + 1
        else:
            print ("Wrong it was" , number)
    if score > 2:
        r = "WON"
    else:
        r = "LOST"
    print ("You", r, "and you got" ,score, "correct and" , (5 - score), "wrong")
    play = input ("One more time?.. ")
    play.lower()
print ('   ')
print ('   ')
print ('   ')
print ('   ')
print ('                  It was nice to play with you!')
print ('                  --------->GAME OVER<---------')
print ('                     By Miraslau Kavaliou      ')
