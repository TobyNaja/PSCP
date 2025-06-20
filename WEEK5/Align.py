"""Align"""
def main():
    """Align"""
    size = int(input())
    alignment = input().strip()
    message = input().strip()
    padding = size - len(message)
    if alignment == "left":
        print(message + " " * padding)
    elif alignment == "right":
        print(" " * padding + message)
    elif alignment == "center":
        left_padding = padding // 2
        right_padding = padding - left_padding
        if padding % 2:
            left_padding += 1
        print(" " * right_padding + message + " " * left_padding)
main()
