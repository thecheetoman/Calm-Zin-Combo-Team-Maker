import random
import time
import os
#read names from the players.txt file
def read_players(filename):
    
    with open(filename, 'r') as file:
        players = [line.strip() for line in file if line.strip()]
    return players
#create the teams by randomly alloting a value to each name and assigning teams.
def create_teams(players, team_size=3):
    random.shuffle(players)
    teams = [players[i:i + team_size] for i in range(0, len(players), team_size)]
    return teams
#do the save thingy
def print_and_save_teams(teams, output_file='teams.txt'):
    with open(output_file, 'w') as file:
        for i, team in enumerate(teams, 1):
            team_str = f"Team {i}: {', '.join(team)}"
            print(team_str)
            file.write(team_str + '\n')

def main():
    print("Calm Zin Combo Team Maker")
    print("Programmed by SirCheetoDust")
    time.sleep(1)
    print("hacking embark servers(definetly)")
    time.sleep(2)
    print("wasting your time =D")
    time.sleep(1)
    print("jks")
    time.sleep(0.6)
    os.system('clear')
    players = read_players('players.txt')
    teams = create_teams(players, team_size=3)
    print_and_save_teams(teams)

if __name__ == '__main__':
    main()
