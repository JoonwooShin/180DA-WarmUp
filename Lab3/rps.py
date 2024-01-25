import random

user_input = input('Rock Paper Scissors: ').lower()
user = 0
cpu = random.randint(1,3)
# 1 = Rock, 2 = Paper, 3 = Scissors

match user_input:
    case "rock":
        user = 1
    case "paper":
        user = 2
    case "scissors":
        user = 3

match cpu:
    case 1:
        print("CPU: Rock")
    case 2:
        print("CPU: paper")
    case 3:
        print("CPU: Scissors")

diff = user - cpu
if diff == 0:
    print("Tie Game!")
elif (diff % 3) == 1: 
    print("You win!")
else:
    print("CPU Wins!")