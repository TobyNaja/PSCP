"""[Final 2019] T-score"""
def main():
    """[Final 2019] T-score"""
    n = int(input())
    maxscore = int(input())
    mylist = []
    powerlist = []
    for _ in range(n):
        score = int(input())
        if score > maxscore:
            score = maxscore
        mylist.append(score)
        powerlist.append(score**2)
    sumscore = sum(mylist)
    powersum = sum(powerlist)
    average = sumscore/n
    sd = (((n*powersum) - (sumscore**2))/(n*(n-1)))**0.5
    for i in mylist:
        z = (i-average)/sd
        tscore = 50 + (10*z)
        print(f"{tscore:.2f}")
main()
