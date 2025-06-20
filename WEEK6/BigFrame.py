"""BigFrame"""
def main():
    """BigFrame"""
    txt1 = input().strip()
    txt2 = input().strip()
    txt3 = input().strip()
    txt4 = input().strip()
    txt5 = input().strip()
    txt_max = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    print("**"+("*"*txt_max)+"**")
    print(f"* {txt1:<{txt_max}} *")
    print(f"* {txt2:<{txt_max}} *")
    print(f"* {txt3:<{txt_max}} *")
    print(f"* {txt4:<{txt_max}} *")
    print(f"* {txt5:<{txt_max}} *")
    print("**"+("*"*txt_max)+"**")
main()
