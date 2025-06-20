"""CuteCat CuteFox"""
import json
def process(cafe,cat,fox):
    """CuteCat CuteFox"""
    for i,j in cafe.items():
        if i in cat:
            del cat[i]
        elif i in fox:
            del fox[i]
        if "Cat" in j:
            for k in list(cat.keys()):
                if cat[k] == j:
                    del cat[k]
            cat[i] = j
        elif "Fox" in j:
            for k in list(fox.keys()):
                if fox[k] == j:
                    del fox[k]
            fox[i] = j
def main(n):
    """CuteCat CuteFox"""
    cafe={}
    cat={"Garfield":"Cat01"}
    fox={"Fubuki":"Fox01"}
    for _ in range(n):
        speies = input()
        if speies.count("'") == 4:
            speies = speies.replace("'", '"')
        a = json.loads(speies)
        cafe.update(a)
    process(cafe,cat,fox)
    sorted_cats = dict(sorted(cat.items(), key=lambda item: (item[1][:3], int(item[1][3:]))))
    sorted_fox = dict(sorted(fox.items(), key=lambda item: (item[1][:3], int(item[1][3:]))))
    print(f"Cat : {len(cat)}")
    print(f"Fox : {len(fox)}")
    for i,j in sorted_cats.items():
        print(f"{i} : {j}")
    for i,j in sorted_fox.items():
        print(f"{i} : {j}")
main(int(input()))
