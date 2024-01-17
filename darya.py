class Soldier:
    def __init__(self, soldier_id, soldier_type, health, x, y):
        self.soldier_id = soldier_id
        self.soldier_type = soldier_type
        self.health = health
        self.x = x
        self.y = y

    def move(self, direction, n):
        if direction == 'right':
            if self.x == n:
                print("out of bounds")
                return False
            else:
                self.x += 1
                return True

        elif direction == 'left':
            if self.x == 0:
                print("out of bounds")
                return False
            else:
                self.x -= 1
                return True

        elif direction == 'down':
            if self.y == n:
                print("out of bounds")
                return False
            else:
                self.y += 1
                return True

        elif direction == 'up':
            if self.y == 0:
                print("out of bounds")
                return False
            else:
                self.y -= 1
                return True

    def get_info(self):
        return f"health:  {self.health}\nlocation:  {self.x}   {self.y}"


class GameBoard:
    def __init__(self, size):
        self.size = size
        self.soldiers = [{}, {}]
        self.player = 0

    def create_soldier(self, soldier_id, soldier_type, health, x, y):
        if soldier_id in self.soldiers[self.player]:
            print("duplicate tag")
        else:
            self.soldiers[self.player][soldier_id] = Soldier(soldier_id, soldier_type, health, x, y)
            self.player = 0 if self.player else 1

    def move_soldier(self, soldier_id, direction, n):
        if self.soldiers[self.player][soldier_id].move(direction, n):
            self.player = 0 if self.player else 1

    def attack_soldier(self, attacker_id, target_id):
        distance = self.calculate_distance(self.soldiers[self.player][attacker_id],
                                           self.soldiers[1 - self.player][target_id])
        if self.soldiers[self.player][attacker_id].soldier_type == "archer":
            if distance > 2:
                print("the target is too far")
            else:
                self.soldiers[1 - self.player][target_id].health -= 10
                if self.soldiers[1 - self.player][target_id].health <= 0:
                    del self.soldiers[1 - self.player][target_id]
                    print('target eliminated')

                self.player = 0 if self.player else 1

        elif self.soldiers[self.player][attacker_id].soldier_type == "melee":
            if distance > 1:
                print("the target is too far")
            else:
                self.soldiers[1 - self.player][target_id].health -= 20
                if self.soldiers[1 - self.player][target_id].health <= 0:
                    del self.soldiers[1 - self.player][target_id]
                    print('target eliminated')

                self.player = 0 if self.player else 1

    def calculate_distance(self, soldier1, soldier2):
        distance = abs(soldier1.x - soldier2.x) + abs(soldier1.y - soldier2.y)
        return distance

    def who_is_in_lead(self):
        healths = [0, 0]

        for i in range(len(self.soldiers)):
            for soldier in self.soldiers[i].values():
                healths[i] += soldier.health

        if healths[0] > healths[1]:
            print('player  1')
        elif healths[0] < healths[1]:
            print('player  2')
        else:
            print('draw')

    def get_soldier_info(self, soldier_id):
        if soldier_id in self.soldiers[self.player]:
            info = self.soldiers[self.player][soldier_id].get_info()
            self.player = 0 if self.player else 1
            return info
        else:
            return "soldier does not exist"


n = int(input())
game_board = GameBoard(n)

while True:
    command = input().split()

    if command[0] == "new":
        soldier_type = command[1]
        soldier_id = int(command[2])
        health = 100
        x = int(command[3])
        y = int(command[4])
        game_board.create_soldier(soldier_id, soldier_type, health, x, y)
    elif command[0] == "move":
        soldier_id = int(command[1])
        direction = command[2]
        game_board.move_soldier(soldier_id, direction, n)
    elif command[0] == "attack":
        attacker_id = int(command[1])
        target_id = int(command[2])
        game_board.attack_soldier(attacker_id, target_id)
    elif command[0] == "info":
        soldier_id = int(command[1])
        print(game_board.get_soldier_info(soldier_id))
    elif command[0] == "who":
        game_board.who_is_in_lead()
    elif command[0] == "end":
        break
