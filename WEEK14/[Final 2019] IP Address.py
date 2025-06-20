"""[Final 2019] IP Address"""
def main():
    """[Final 2019] IP Address"""
    ip = input()
    octets = ip.split(".")
    if len(octets) != 4:
        print("Invalid IPv4 address")
        return
    for i in range(4):
        octet = octets[i]
        if not octet.isdigit():
            print("Invalid IPv4 address")
            return
        num = int(octet)
        if num < 0 or num > 255:
            print("Invalid IPv4 address")
            return
        octets[i] = str(num)
    print(".".join(octets))
main()
