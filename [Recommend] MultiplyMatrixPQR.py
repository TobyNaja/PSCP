"""[Recommend] MultiplyMatrixPQR"""
def main(p,q,r):
    """[Recommend] MultiplyMatrixPQR"""
    pq = []
    qr = []
    pq1 = []
    for _ in range(p):
        for _ in range(q):
            x = int(input())
            pq1.append(x)
        pq.append(pq1)
        pq1 = []
    for _ in range(q):
        for _ in range(r):
            x = int(input())
            pq1.append(x)
        qr.append(pq1)
        pq1 = []
    for i in range(p):
        for k in range(r):
            total = 0
            for j in range(q):
                total += pq[i][j] * qr[j][k]
            print(total ,end=" ")
        print()
main(int(input()),int(input()),int(input()))
