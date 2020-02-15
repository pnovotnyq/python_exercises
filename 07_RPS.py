#! /usr/bin/env python3
'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the wp, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

# If I had a second player, I could just play RPS with them. Let's play against the computer.

player = str(input("What's your name? ").capitalize())
rps = ('rock','paper','scissors')
score = {player:0,'cpu':0}

def get_plays():
    import random
    playerplay = input('\nWhat do you play? (rock/paper/scissors) ').lower()
    if playerplay not in rps:
        print ('You cannot play ' + str(playerplay))
        cpuplay = 0
    else:
        cpuplay = str(random.sample(rps,1)[0])
    return {player:playerplay,'cpu':cpuplay}

def evaluate(plays_dict):
    wp = None
    plays = plays_dict.values()
    if 'rock' in plays and 'paper' in plays:
        wp = 'paper'
    elif 'rock' in plays and 'scissors' in plays:
        wp = 'rock'
    elif 'scissors' in plays and 'paper' in plays:
        wp = 'scissors'
    if plays_dict[player] == wp:
        return 1
    elif plays_dict['cpu'] == wp:
        return 2
    else:
        return 3

def counter(winner):
    newscore = score
    if winner == 1:
        newscore[player] = newscore[player] + 1
    elif winner == 2:
        newscore['cpu'] = newscore['cpu'] + 1
    return newscore

def main():
    while True:
        plays_dict = get_plays()
        if plays_dict['cpu'] == 0:
            continue
        print (f'\n{player} played {plays_dict[player]}\nCpu played {plays_dict["cpu"]}.')
        winner = (evaluate(plays_dict))
        if winner == 1:
            print(f'{player} wins!')	
        elif winner == 2:
            print(f'Cpu wins!')
        else:
            print("It's a tie!")
        newscore = counter(winner)
        print("The score is: ")
        print(newscore)
        replay = str(input('Would you like to play again? ')).lower()[0]
        if replay == 'y':
            continue
        else:
            print("The final score is: \n " + str(newscore))
            break
if __name__ == '__main__':
    main()
