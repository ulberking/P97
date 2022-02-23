import random
number = random.randint(1,10)
chances=3
while(chances>0):
    guess=int(input('Guess your number : '))
    if(guess==number):
        print('You get it')
        break
    elif(guess<number):
        print('Yout guess is lesser than the number.')
    elif(guess>number):
        print('Your guess is bigger than the number.')
    chances=chances-1

if(guess!=number):
    print('You losed')