#imports

import time
import os

#var and def

results = "You scored {:.0%}"
score = 0
def clear():
    os.system( 'cls' )
    
#unicode vars
quiz = """quiz"""

made_by = """
Made by Daniel and Ales"""

enter = """Press ENTER"""

q1 = """I ... (be) at home last year."""

q2 = """... (be) at home last year."""

q3 = """Carol ... (not be) in slovakia last summer."""

q4 = """... (be) Michael and Ryan good friends?"""

q5 = """I ... (be) playing pc games yesterday."""

q6 = """I ... (be) hungry."""

q7 = """
█░░ █ █▀ ▄▀█   ▄▀█ █▄░█ █▀▄   ░░█ ▄▀█ █▀▄▀█ █▀▀ █▀           ▄▀ █▄▄ █▀▀ ▀▄   ▄▀█ ▀█▀   █░█ █▀█ █▀▄▀█ █▀▀ 
█▄▄ █ ▄█ █▀█   █▀█ █░▀█ █▄▀   █▄█ █▀█ █░▀░█ ██▄ ▄█   ▄ ▄ ▄   ▀▄ █▄█ ██▄ ▄▀   █▀█ ░█░   █▀█ █▄█ █░▀░█ ██▄ ▄"""

q8 = """
█           ▄▀ █▄░█ █▀█ ▀█▀   █▄▄ █▀▀ ▀▄   ▀█▀ █░█ █ █▄░█ █▄▀ █ █▄░█ █▀▀   ▄▀█ █▄▄ █▀█ █░█ ▀█▀   █ ▀█▀ 
█   ▄ ▄ ▄   ▀▄ █░▀█ █▄█ ░█░   █▄█ ██▄ ▄▀   ░█░ █▀█ █ █░▀█ █░█ █ █░▀█ █▄█   █▀█ █▄█ █▄█ █▄█ ░█░   █ ░█░ ▄ """

q9 = """

█░█░█ █░█ █▀▀ █▀█ █▀▀           ▄▀ █▄▄ █▀▀ ▀▄   █▄█ █▀█ █░█   █▄█ █▀▀ █▀ ▀█▀ █▀▀ █▀█ █▀▄ ▄▀█ █▄█ ▀█
▀▄▀▄▀ █▀█ ██▄ █▀▄ ██▄   ▄ ▄ ▄   ▀▄ █▄█ ██▄ ▄▀   ░█░ █▄█ █▄█   ░█░ ██▄ ▄█ ░█░ ██▄ █▀▄ █▄▀ █▀█ ░█░ ░▄"""

q10 = """
█░█░█ █▀▀           ▄▀ █▄░█ █▀█ ▀█▀   █▄▄ █▀▀ ▀▄   █ █▄░█   ▀█▀ █░█ █▀▀   █▀█ ▄▀█ █▀█ █▄▀
▀▄▀▄▀ ██▄   ▄ ▄ ▄   ▀▄ █░▀█ █▄█ ░█░   █▄█ ██▄ ▄▀   █ █░▀█   ░█░ █▀█ ██▄   █▀▀ █▀█ █▀▄ █░█ ▄"""

wrong = """
██╗░░██╗
╚██╗██╔╝
░╚███╔╝░
░██╔██╗░
██╔╝╚██╗
╚═╝░░╚═╝"""

correct = """
░░░░░░██░
░░░░░██║░
░░░░██║░░
██░██║░░░
╚███╔╝░░░
░╚══╝░░░░"""

resoults = """

██████╗░███████╗░██████╗██╗░░░██╗██╗░░░░░████████╗░██████╗  ██╗
██╔══██╗██╔════╝██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔════╝  ╚═╝
██████╔╝█████╗░░╚█████╗░██║░░░██║██║░░░░░░░░██║░░░╚█████╗░  ░░░
██╔══██╗██╔══╝░░░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░░╚═══██╗  ░░░
██║░░██║███████╗██████╔╝╚██████╔╝███████╗░░░██║░░░██████╔╝  ██╗
╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═════╝░  ╚═╝"""

perfect = """
██████╗░███████╗██████╗░███████╗███████╗░█████╗░████████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██████╔╝█████╗░░██████╔╝█████╗░░█████╗░░██║░░╚═╝░░░██║░░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██╔═══╝░██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██║░░██╗░░░██║░░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
██║░░░░░███████╗██║░░██║██║░░░░░███████╗╚█████╔╝░░░██║░░░  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

░█████╗░░█████╗░██╗░██╗
██╔══██╗██╔══██╗╚═╝██╔╝
╚█████╔╝██║░░██║░░██╔╝░
██╔══██╗██║░░██║░██╔╝░░
╚█████╔╝╚█████╔╝██╔╝██╗
░╚════╝░░╚════╝░╚═╝░╚═╝"""

ok = """
░█████╗░██╗░░██╗  ░█████╗░██╗░░░██╗███████╗██████╗░  ███████╗░█████╗░██╗░██╗
██╔══██╗██║░██╔╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗  ██╔════╝██╔══██╗╚═╝██╔╝
██║░░██║█████═╝░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝  ██████╗░██║░░██║░░██╔╝░
██║░░██║██╔═██╗░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗  ╚════██╗██║░░██║░██╔╝░░
╚█████╔╝██║░╚██╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║  ██████╔╝╚█████╔╝██╔╝██╗
░╚════╝░╚═╝░░╚═╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═╝░╚═╝"""

bad = """
██████╗░░█████╗░██████╗░  ██╗░░░██╗███╗░░██╗██████╗░███████╗██████╗░  ░░██╗██╗░█████╗░██╗░██╗
██╔══██╗██╔══██╗██╔══██╗  ██║░░░██║████╗░██║██╔══██╗██╔════╝██╔══██╗  ░██╔╝██║██╔══██╗╚═╝██╔╝
██████╦╝███████║██║░░██║  ██║░░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝  ██╔╝░██║██║░░██║░░██╔╝░
██╔══██╗██╔══██║██║░░██║  ██║░░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗  ███████║██║░░██║░██╔╝░░
██████╦╝██║░░██║██████╔╝  ╚██████╔╝██║░╚███║██████╔╝███████╗██║░░██║  ╚════██║╚█████╔╝██╔╝██╗
╚═════╝░╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝  ░░░░░╚═╝░╚════╝░╚═╝░╚═╝"""

#Starting text

print(quiz)
print(made_by)
input(enter)
clear()
time.sleep(1)

#1 Question
print(q1)
status = (input().lower())
clear()
if status == 'was':
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#2 Question
print(q2)
status = (input().lower())
clear()
if status == 'were':
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#3 Question
print(q3)
status = (input().lower())
clear()
if status == "wasn't":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
elif status == "wasnt":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
elif status == "was not":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#4 Question
print(q4)
status = (input().lower())
clear()
if status == 'were':
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#5 Question
print(q5)
status = (input().lower())
clear()
if status == 'was':
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#6 Question
print(q6)
status = (input().lower())
clear()
if status == 'was':
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#7 Question
print(q7)
status = (input().lower())
clear()
if status == 'were':
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#8 Question
print(q8)
status = (input().lower())
clear()
if status == "wasn't":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
elif status == "wasnt":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
elif status == "was not":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#9 Question
print(q9)
status = (input().lower())
clear()
if status == 'were':
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#10 Question
print(q10)
status = (input().lower())
clear()
if status == "weren't":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
elif status == "werent":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
elif status == "were not":
    print (str(correct))
    score = score + 0.1
    time.sleep(1)
else:
    print(wrong)
    time.sleep(1)
clear()

#results

print(resoults)
if score > 0.80:
    print(perfect)
    print(results.format(score))
elif score > 0.50:
    print(ok)
    print(results.format(score))
elif score < 0.40:
    print(bad)
    print(results.format(score))

