import random
import time
import sys

#state the delay between actions
delay_between_actions = 1
max_value = 100
dice_face = 6

# these lists store snake bite positions and and corresponding result 
# positions after sanke bite
snake_bite_positions = [8, 18, 26, 39, 51, 54, 56, 60, 75, 83, 85, 90, 92, 97, 99]
snake_bite_results = [4, 1, 10, 5, 6, 36, 1, 23, 28, 45, 59, 48, 25, 87, 63]


# these lists store ladder postions abd corresponding result
# positions after climbing ladder
ladder_positions = [3, 6, 11, 15, 17, 22, 38, 49, 57, 61, 73, 81, 88]
ladder_results = [20, 14, 28, 34, 74, 37, 59, 67, 76, 78, 86, 98, 91]


player_turn = [
	"It's your turn now.",
	"Go.",
	"You can win this",
	"Are you ready?",
	"",
]


snake_bite = [
	"boohoo",
	"what a bummer!",
	"You got a snake bite",
	"oh no",
]


ladder_jump = [
	"woohoo",
	"WOW!",
	"NAILED IT!",
	"CONGRATS!",
	"yaayyy"
]




def welcome_message():
	message = """
	Welcome to the Snakes and Ladders Game.
	Rules:
		1. At the start of the game, the players are at the starting position, which is 0
		The players will take turns to roll the dice.
		and move forward the number of spaces shown on the dice.
		
		2. If you end up at the bottom of a ladder, you can move up to the top of the ladder.
		
		3. If you land on the head of a snake, you must slide down to the bottom of the snake.
		
		4. The first player to get to the FINAL position, which is 100, is the winner.
		
		5. Hit enter to roll the dice.
	"""
	print(message)


def get_player_name():
	player1_name = None
	while not player1_name:
		player1_name = input("Please enter a valid name for first player: ").strip()
	player2_name = None
	while not player2_name:
		player2_name = input("Please enter a valid name for second player: ").strip()
	print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
	return player1_name, player2_name


def get_dice_value():
	time.sleep(delay_between_actions)
	dice_value = random.randint(1, dice_face)
	print("Its a " + str(dice_value))
	return dice_value


def got_snake_bite(old_value, current_value, player_name):
	print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
	print("\n" + player_name + " just got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
	print("\n" + random.choice(ladder_jump).upper() + " ########")
	print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
	time.sleep(delay_between_actions)
	old_value = current_value
	current_value = current_value + dice_value
	
	if current_value > max_value:
		print("You need " + str(max_value - old_value) + " to win this game. Keep trying.")
		final_value = old_value
	else:
		print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
		
		if current_value in snake_bite_positions:
			final_value = snake_bite_results[snake_bite_positions.index(current_value)]
			got_snake_bite(current_value, final_value, player_name)
		elif current_value in ladder_positions:
			final_value = ladder_results[ladder_positions.index(current_value)]
			got_ladder_jump(current_value, final_value, player_name)
		else:
			final_value = current_value
	return final_value



def win(player_name, position):
	time.sleep(delay_between_actions)
	if max_value == position:
		print("\n\n\nThats it.\n\n" + player_name + " won the game.")
		print("Congratulations " + player_name)
		print("\nThank you for playing the game")
		sys.exit(1)



def start():
	welcome_message()
	time.sleep(delay_between_actions)
	player1_name, player2_name = get_player_name()
	time.sleep(delay_between_actions)
	
	player1_current_position = 0
	player2_current_position = 0
	
	while True:
		time.sleep(delay_between_actions)
		input_1 = input("\n" + player1_name + ": " + random.choice(player_turn) + " Hit enter to roll dice: ")
		print("\nRolling dice...")
		dice_value = get_dice_value()
		time.sleep(delay_between_actions)
		print(player1_name + " moving....")
		player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)
		
		win(player1_name, player1_current_position)
		
		input_2 = input("\n" + player2_name + ": " + random.choice(player_turn) + " Hit enter to roll dice: ")
		print("\nRolling dice...")
		dice_value = get_dice_value()
		time.sleep(delay_between_actions)
		print(player2_name + " moving....")
		player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)
		win(player2_name, player2_current_position)

start()

