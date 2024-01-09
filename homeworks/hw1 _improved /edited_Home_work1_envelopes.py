# -*- coding: utf-8 -*-
# initializing empty envelops

necessity_envelop = 0  # NEC, необхідні витрати
freedom_envelop = 0    # FFA, фінансова свобода
education_envelop = 0  # EDU, освіта
long_term_envelop = 0   # LTSS, резерв та на великі покупки
play_envelop = 0       # PLAY, розваги
give_envelop = 0       # GIVE, подарунки

# initializing percent rate
necessity_envelop_rate = 0.55
freedom_envelop_rate = 0.1
education_envelop_rate = 0.1
long_term_envelop_rate = 0.1
play_envelop_rate = 0.1
give_envelop_rate = 0.05
# initializing expected income, expected necessity and other amounts
expected_income = 1000
# invitation, greetings etc.
print ("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results""")
# initializing handler for standard input
sum = 0

while (sum < expected_income):
    line = int(input())
    sum += line

    necessity_envelop += line * necessity_envelop_rate
    freedom_envelop += line * freedom_envelop_rate
    education_envelop += line * education_envelop_rate
    long_term_envelop += line * long_term_envelop_rate
    play_envelop += line * play_envelop_rate
    give_envelop += line * give_envelop_rate
    if sum<expected_income:
      print("\n Enter the amount please:")
necessity_envelop_without_coins=int(necessity_envelop)
freedom_envelop_without_coins=int(freedom_envelop)
education_envelop_without_coins=int(education_envelop)
long_term_envelop_without_coins=int(long_term_envelop)
play_envelop_without_coins=int(play_envelop)
give_envelop_without_coins=int(give_envelop)                    
print("At the end we have:\n")
print(f"Necessity Envelop has: {necessity_envelop_without_coins}\n")
print(f"Financial Freedom Envelop has: {freedom_envelop_without_coins}\n")
print(f"Education Envelop has: {education_envelop_without_coins} \n")
print(f"Long Term Saving for Spending Envelop has: {long_term_envelop_without_coins}\n")
print(f"Play Envelop has: {play_envelop_without_coins}\n")
print(f"Give Envelop has: {give_envelop_without_coins}\n")
print(" Thanks for using our software :)")



