"""Palindrome"""
def main():
    """find Palindrome with time"""
    x = int(input())
    now = input()
    time = find_pali(now)
    ans = ""
    if now != time:
        print(time)
        x -= 1
    for _ in range(x):
        if len(time) == 4:
            if int(time[2])+1 <= 5:
                time = time[:2]+str(int(time[2])+1)+time[3]
            elif time == "0:50":
                time = "1:01"
            elif int(time[0]) < 9:
                time = str(int(time[0])+1)+time[1]+"0"+str(int(time[0])+1)
            else:
                time = str(int(time[0])+1)+time[1]+"01"
            ans = time
        elif len(time) == 5:
            if time[0] == "1" and int(time[3]) < 5:
                time = time[0] + str(int(time[1])+1) + time[2] + str(int(time[1])+1) + time[4]
                ans = time
            elif time[0] == "1" and int(time[3]) >= 5:
                time = "20:02"
                ans = time
            elif time[0] == "2" and int(time[3]) < 3:
                time = time[0] + str(int(time[1])+1) + time[2] + str(int(time[1])+1) + time[4]
                ans = time
            elif time[0] == "2" and int(time[3]) >= 3:
                time = "0:00"
                ans = time
        print(ans)

def find_pali(x):
    """find Palindrome"""
    if len(x) == 4:
        if x[0] > x[3]:
            x = x[:3]+x[0]
        elif x[0] < x[3]:
            if int(x[2]) < 5 :
                x = x[:3]+x[0]
                x = x[:2]+str(int(x[2])+1)+x[3]
            elif int(x[2]) == 5 :
                x = x[:3]+x[0]
                x = str(int(x[0])+1)+x[1:2]+"0"+x[3]
    elif len(x) == 5:
        if x[0] > x[4]:
            x = x[:4]+x[0]
            if x[1] < x[3]:
                x = x[0]+str(int(x[1])+1)+x[2:]
                x = x[:3]+x[1]+x[4]
            x = x[:3]+x[1]+x[4]
        elif x[0] < x[4]:
            x = x[:4]+x[0]
            x = x[:3]+str(int(x[3])+1)+x[4]
            if x[1] < x[3]:
                x = x[0]+str(int(x[1])+1)+x[2:]
                x = x[:3]+x[1]+x[4]
            x = x[:3]+x[1]+x[4]
        if int(x[:2]) >= 24:
            x = "0:00"
    return x
main()
