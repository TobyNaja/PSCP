"""BloodDonation"""
def main():
    """BloodDonation"""
    age = int(input())
    wight = int(input())
    num = int(input())
    if age == 17 or 60 <= age <= 70:
        cer = input()
        if cer == "True" and wight >= 45:
            if age > 55 and num <= 0:
                print("No")
            else:
                print("Yes")
        else:
            print("No")
    elif 17 < age < 60 and wight >= 45:
        if age > 55 and num <= 0:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
main()
