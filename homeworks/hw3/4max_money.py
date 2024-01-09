print("Enter the amount of money you want to change:")
amount=int(input())
thousand=amount//1000
five_hundreds=(amount-thousand*1000)//500
two_hundreds=(amount-thousand*1000-five_hundreds*500)//200
hundred=(amount-thousand*1000-five_hundreds*500-two_hundreds*200)//100
fifty=(amount-thousand*1000-five_hundreds*500-two_hundreds*200-hundred*100)//50
twenty=(amount-thousand*1000-five_hundreds*500-two_hundreds*200-hundred*100-fifty*50)//20
ten=(amount-thousand*1000-five_hundreds*500-two_hundreds*200-hundred*100-fifty*50-twenty*20)//10
we_can_not_give_you=(amount-thousand*1000-five_hundreds*500-two_hundreds*200-hundred*100-fifty*50-twenty*20-ten*10)//1
print(f"""Please take you money:
      banknotes with nominal 1000$: {thousand}
      banknotes with nominal 500$:{five_hundreds}
      banknotes with nominal 200$:{two_hundreds}
      banknotes with nominal 100$: {hundred}
      banknotes with nominal 50$: {fifty}
      banknotes with nominal 20$: {twenty}
      banknotes with nominal 10$: {ten}
""")
if we_can_not_give_you:
    print(f"Sorry, but we can not give you {we_can_not_give_you} dollars")