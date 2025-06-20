"""Easy Histogram No Dict"""
def main():
    """Easy Histogram No Dict"""
    his = str(input())
    words = []
    pure_words = []
    for i in his:
        if i != " ":
            if i not in pure_words:
                pure_words.append(i)
            words.append(i)
    pure_words.sort(key=lambda b: (b.lower(), b.isupper()))
    for i in pure_words:
        print(f"{i} = {words.count(i)}")
main()
