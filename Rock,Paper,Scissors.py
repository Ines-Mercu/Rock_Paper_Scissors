import random
class Game:
    def __init__(self):
        self.computer_pick = self.get_computer_pick()
        self.player_pick = self.get_player_pick()
        self.result = self.get_result()
    def get_computer_pick(self):
        random_pick = random.randint(0, 2)
        picks = {0: 'rock', 1: 'paper', 2: 'scissors'}
        return picks[random_pick]
    def get_player_pick(self):
        while True:
            player_pick = input('Choose one:rock/paper/scissors: ')
            player_pick = player_pick.lower()

            if player_pick in ('rock', 'paper', 'scissors'):
                break
            else:
                print('Wrong input, choose again!')
        return player_pick
    def get_result(self):
        if self.player_pick ==  self.computer_pick:
            return 'You tie!'
        elif self.player_pick == 'scissors' and self.computer_pick == 'paper':
            return "You Win!"
        elif self.player_pick == 'rock' and self.computer_pick == 'scissors':
            return "You Win!"
        elif self.player_pick == 'paper' and self.computer_pick == 'rock':
            return "You Win!"
        else:
            return 'You lose!'

    def show_result(self):
        print(f'Computer pick: {self.computer_pick}')
        print(f'Your pick: {self.player_pick}')
        print(self.result)

start = Game()
start.show_result()