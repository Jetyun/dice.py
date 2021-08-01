import random
dice=[1,2,3,4,5,6]

print("""dice competition vs com, 3 rounds (bigger or smaller)"""

)

attempt=0
win_count=0
lose_count=0



while attempt<3:
			big_or_small=input('big or small= ').lower()
			if big_or_small=="big":
				player=random.choice(dice)
				com=random.choice(dice)
				print("player=" +str(player))
				print("com=" + str(com))
				attempt=attempt+1
				if player<com:
				    print('you lose')
				    lose_count=lose_count+1
				elif player>com:
					print('you win')
					win_count=win_count+1
				elif player==com:
					print('try again')
					attempt=attempt-1
			elif big_or_small=="small":
				player=random.choice(dice)
				com=random.choice(dice)
				print("player=" +str(player))
				print("com=" + str(com))
				attempt=attempt+1
				if player>com:
					print('you lose')
					lose_count=lose_count+1
				elif player<com:
					print('you win')
					win_count=win_count+1
				elif player==com:
					print('try again')
					attempt=attempt-1
			else:
				print('please insert the right command')
else:
	print('game ended')
	print('win=' +str(win_count))
	print('lose=' +str(lose_count))




	
