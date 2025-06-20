"""W"""
def main():
    """W"""
    x = input()
    none = input()
    none = str(none)
    ping = input()
    if ping.find("[") >= 0:
        ping = ping[(ping.find("[")+1):ping.find("]")]
    else:
        ping = (x[x.find("ping")+5:]).strip()
    reply,time = check()
    rec = reply
    lost = 4 - rec
    percent = int(100 - (rec * 100 / 4))
    try:
        timeMax,timeMin = max(time),min(time)
    except ValueError:
        timeMax,timeMin = 0,0
    if rec:
        average = sum(time) // rec
    else:
        average = 0
    print("Ping statistics for",str(ping)+":")
    print(f"    Packets: Sent = 4, Received = {rec}, Lost = {lost} ({percent}\
% loss),")
    if lost < 4:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {timeMin}ms, Maximum = {timeMax}ms, Average = {average}ms")
def check():
    """W"""
    reply = 0
    time1 = ()
    for _ in range(4):
        para = input()
        for i in para:
            if i.isdigit() is True:
                reply += 1
                break
        try:
            if para.find("time<1") >= 0:
                time1 += (0,)
            elif para.find("time=") >= 0:
                time1 += (int(para[para.find("time=")+5:para.find("ms")]),)
        except ValueError:
            pass
    return reply,time1
main()
