"""d"""
def main():
    """d"""
    num = int(input())
    score = 0
    count = 0
    for _ in range(num):
        card = input()
        if card in("J", "K", "Q"):
            score += 10
        elif card == "A":
            count += 1
        else:
            b = int(card)
            score += b
    for _ in range(count):
        if score <= 10:
            score += 11
        else:
            score += 1
    if score > 21 and count >= 1:
        score -= 10
    print(score)
main()
