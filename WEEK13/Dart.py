"""Dart"""
def main(num):
    """Dart"""
    score = 0
    for _ in range(num):
        pi = input().split()
        x1,x2 = pi[0],pi[1]
        dis = ((int(x1))**2 + (int(x2))**2)**0.5
        if dis <= 2:
            score += 5
        elif 2 < dis <= 4:
            score += 4
        elif 4 < dis <= 6:
            score += 3
        elif 6 < dis <= 8:
            score += 2
        elif 8 < dis <= 10:
            score += 1
    print(score)
main(int(input()))
