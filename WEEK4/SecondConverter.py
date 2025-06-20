"""SecondConverter"""
def main():
    """SecondConverter"""
    second = int(input())
    sec = int(input())
    mint = int(input())
    hous = int(input())
    new_sec = second % sec
    sec = second// sec
    new_mint = sec % mint
    mint = sec // mint
    new_hous = mint % hous
    print(f"{new_hous}:{new_mint}:{new_sec}")
main()