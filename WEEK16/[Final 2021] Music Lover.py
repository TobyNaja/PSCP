"""[Final 2021] Music Lover"""
def main(num):
    """[Final 2021] Music Lover"""
    mysong = {}
    keysong = mysong.keys()
    for _ in range(num):
        x = input().split("-")
        singer = x[0]
        music = x[1]
        if singer not in keysong:
            mysong[singer] = music
        else:
            mysong[singer] += "\n"+music
    for i,j in mysong.items():
        print(i)
        print(j)
main(int(input()))
