# """coke"""
# def main(a, b, c, d):
#     """coke"""
#     if not b or a == c:
#         money = a * d
#     else:
#         far = 0
#         money = 0
#         while d > 0:
#             if far < b:
#                 money += a
#                 far += 1
#             else:
#                 money += c
#                 far = 1
#             d -= 1
#     print(money)

# main(int(input()), int(input()), int(input()), int(input()))

def main(a, b, c, d):
    """coke"""
    money = 0
    caps = 0
    while d > 0:
        if caps < b - 1:
            money += a
            caps += 1
        else:
            money += c
            caps = 0
        d -= 1
    print(money)
main(int(input()), int(input()), int(input()), int(input()))
