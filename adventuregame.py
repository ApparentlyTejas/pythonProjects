name = input('type yo name: ')
print('welcome to the game' , name , '.')

answer=input('youre on a dirt road do you wanna go left or right? :').lower()
if answer == 'left':
    answer= input('you come across a river do ya wanna swim or walk? :')
    if answer=='swim':
        print('you loose')
    elif answer=='walk':
        print('you win')
    else:
        print('wrong choice')
elif answer == 'right':
    print('you came across a bridge do you wanna try your luck or go back?: ')
    if answer=='back':
        print('you loose')
    elif answer==('try luck'):
        print('you win')
    else:
        print('wrong choice')
else :
    print('wrong choice you loose')

print('thanks for playing', name)