"""Impostor"""
import json
def main():
    """Impostor"""
    roles={}
    dead={}
    c=0
    while True:
        amongus=input()
        if amongus.strip()=="Start":
            break
        player=json.loads(amongus)
        roles.update(player)
    while True:
        vote=input()
        if vote=="End":
            break
        dead[vote] = roles.pop(vote)
    for i in roles.values():
        if i == "Impostor":
            c +=1
    print(f"{c} Impostor Remains")
    print("***Alive***")
    for i,j in sorted(roles.items()):
        print(f"{i} : {j}")
    print("***Dead***")
    for i,j in sorted(dead.items()):
        print(f"{i} : {j}")
main()