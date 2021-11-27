import time

print('Welcome to this animal quiz!')
time.sleep(2)
points = 0
print('You have 0 points!')
time.sleep(2)
print('You have to type the answers without capital letters!')
time.sleep(3)

#The first question:
question_1 = input('The first question is: what is the fastest land animal?')
if question_1 == 'leopard':
    print('Correct answer!')
    points = points + 10
else:
    print("That's wrong! The correct answer is leopard!")

time.sleep(2)

#The second question:
question_2 = input('The second question is: what is the largest animal in the world?')
if question_2 == 'blue whale':
    print('Correct answer!')
    points = points + 10
else:
    print("That's wrong! The correct answer is blue whale!")

time.sleep(2)

#The third question:
question_3 = input('Does a jellyfish have a brain?')
if question_3 == 'no':
    print('Correct answer!')
    points = points + 10
else:
    print("That's wrong! The correct answer is no!")

time.sleep(2)

#The end:
if points == 30:
    print('You have reached the maximum score! Congrats!')
elif points < 30:
    print('You lost!')

