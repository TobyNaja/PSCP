# """Lotto"""
# def main():
#     """Lotto"""
#     win1 = input()
#     win2 = input()
#     win3_1 = input()
#     win3_2 = input()
#     win4_1 = input()
#     win4_2 = input()
#     num = input()
#     count = 0
#     check2 = num[4:]
#     check3 = num[:3]
#     check4 = num[3:]
#     if num == win1:
#         count += 6000000
#     if check2 == win2:
#         count += 2000
#     if check3 == win3_1 or check3 == win3_2:
#         count += 4000
#     if check4 == win4_1 or check4 == win4_2:
#         count += 4000
#     if num != "000000" or num != "999999":
#         if int(num) == int(win1)-1 or int(num) == int(win1)+1:
#             count += 100000
#     else:
#         if win1 == "000000" and num == "000001":
#             count += 100000
#         if win1 == "000000" and num == "999999":
#             count += 100000
#         if win1 == "999999" and num == "999998":
#             count += 100000
#         if win1 == "999999" and num == "000000":
#             count += 100000
#     print(count)
# main()
"""Lotto"""
def main():
    """Lotto"""
    firstprize = input()
    lasttwoprize = input()
    firstthreeprize1 = input()
    firstthreeprize2 = input()
    lastthreeprize1 = input()
    lastthreeprize2 = input()
    mine = input()
    a = int(firstprize)-1
    if a < 0:
        a = "999999"
    else:
        a = f"{int(firstprize)-1:>06}"
    b = f"{int(firstprize)+1:>06}"
    if int(b) > 999999:
        b = "000000"
    ans = 0
    if mine == firstprize:
        ans += 6000000
    if mine[4:] == lasttwoprize:
        ans += 2000
    if mine[:3] == firstthreeprize1:
        ans +=  4000
    if mine[:3] == firstthreeprize2:
        ans += 4000
    if mine[3:] == lastthreeprize1:
        ans += 4000
    if mine[3:] == lastthreeprize2:
        ans += 4000
    if mine in (a,b):
        ans += 100000
    print(ans)
main()
