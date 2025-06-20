"""d"""
import json
def main():
    """d"""
    player = {}
    dead = {}
    while True:
        among = input()
        if among == "Start":
            break
        player.update(json.loads(among))
    while True:
        die = input()
        if die == "End":
            break
        dead[die] = player.pop(die)
        