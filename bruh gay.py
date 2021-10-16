#imports

import time

#var

results = "You scored {:.0%}"
score = 0

#Starting text

print("{          QUIZ          }")
print("By Daniel Y., Aleš C.")
input("Press Enter to Start...")
time.sleep(1.5)

#1 Question

status = input('Are you gay? : ')
if status == 'yes':
    score = score + 0.10
    print('Why bro?')
elif status == 'no':
    print('Nice bro')
else:
    print('Only accepting yes and no')

#results

print("Final results : ")
if score > 0.80:
    print("Nice results you got more than 80% ^_^")
    print(results.format(score))
elif score > 0.50:
    print("not the worst but you should train a bit more :)")
    print(results.format(score))
elif score < 0.40:
    print("you should really train more :(")
    print(results.format(score))

