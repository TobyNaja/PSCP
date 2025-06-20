"""Elo"""
def main(ra,rb,player):
    """Elo"""
    e = 0
    if player == "A":
        e = 1/(1+10**((rb-ra)/400))
    if player == "B":
        e = 1/(1+10**((ra-rb)/400))
    print(f"{e:.2f}")
main(int(input()), int(input()), input())
