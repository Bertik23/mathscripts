from fractions import Fraction


def load_matice(file):
    data = open(file, "r").readlines()
    data = [[int(y) for y in x.replace("\\n", '').split()] for x in data]
    return data


def print_matice(d):
    for i in d:
        out = ""
        for j in i:
            out += str(j) + " "*(10-len(str(j)))
        print(out)
    print("-"*50)


def troj_matice(data):
    '''
        vypočítá trojůhelníkovou matici
    '''
    for sloupec in range(len(data[0])-1):
        pocet_nul = len(data) - 1 - sloupec
        for radek in range(pocet_nul):
            # číslo které vynásobíme n a přičteme k nulaku
            nasobitel = data[sloupec][sloupec]
            pos = len(data) - radek - 1
            nulak = data[pos][sloupec]  # číslo které chceme dát na 0

            try:
                nasobek = Fraction(-nulak, nasobitel)  # - nulak / nasobitel
            except ZeroDivisionError:
                nasobek = 0

            for i in range(len(data[pos])):
                data[pos][i] += data[sloupec][i] * nasobek
    return data


def solve(data):
    '''
        vyřeší trojúhelníkovou matici
    '''
    nezname = [None for i in range(len(data[0]) - 1)]

    for line in data[::-1]:
        # print(line)
        s = 0
        for i, num in enumerate(line[:-1][::-1]):
            if num != 0:
                index = line.index(num)
                # print(index,num, line[-1])
                if nezname[index] is None:
                    nezname[index] = Fraction(
                        line[-1] - s, num)  # (line[-1] - s) / num
                    # print("neznama")
                else:
                    s += num * nezname[index]
    return nezname


def get_hodnost(data):
    '''
        vypočítá hodnost matice
    '''
    hodnost = 0
    for i in data:
        if i != [0 for j in range(len(i))]:
            hodnost += 1
    return hodnost


def get_hodnosti(data):
    '''
        vypočítá hodnosti A a A|b a n
    '''
    Ab = data
    A = []
    for i in data:
        A.append(i[:-1])
    hA = get_hodnost(A)
    hAb = get_hodnost(Ab)
    n = len(data[0])-1
    return hA, hAb, n


def check_hodnosti(A, Ab, n):
    '''
        zkontroluje kolik má matice řešení a vyprintuje info
    '''
    if A < Ab:
        print("SLR nemá řešení")
        return -1
    elif A == Ab == n:
        print("SLR má právě jedno řešení")
        return 0
    elif A == Ab and A < n:
        print("SLR má nekonečně mnoho řešení")
        return n-A


def solve_parametry(matice, pocet_parametru):
    '''
        vyřeší matici pomocí parametrů
    '''
    data = matice
    par = 0
    # odstranění nulových řádků
    parametry = [None for i in range(len(data[0])-1)]
    for line in data[::-1]:
        if line != [0 for i in range(len(line))]:
            for j, num in enumerate(line[:-1]):
                if num != 0 and par < pocet_parametru and parametry[j] is None:
                    parametry[j] = chr(97 + par)
                    par += 1
                elif parametry[j] is None and num != 0:
                    # vyjádření neznámých pomocí parametrů
                    val = str(line[-1])
                    for x in range(len(line[:-1])):
                        if x != j and parametry[x] is not None:
                            # val += str("-" + str(line[x]) + "*"
                            #  +str(parametry[x]))
                            val += f"-{str(line[x])}*({str(parametry[x])})"
                    parametry[j] = val
    return parametry


def magic(s, nasobek=1, check=False):
    global promenne

    pos = 0
    nasobitel = ""
    while pos < len(s):
        char = s[pos]
        if char not in "()*":
            nasobitel += char
        elif char == "(":
            start = pos
            pocet_zavorek = 1
            while pocet_zavorek > 0:
                pos += 1
                char = s[pos]
                if char == "(":
                    pocet_zavorek += 1
                if char == ")":
                    pocet_zavorek -= 1
            end = pos
            sub = s[start+1:end]
            if "(" in sub:
                magic(sub, nasobek=nasobitel)
            else:
                # print(nasobek, nasobitel, sub)
                n = eval(f"{nasobek}*({nasobitel})")
                # print(sub, n)
                promenne[sub] += n
            nasobitel = ""
        pos += 1
    return promenne


def zhezci(d):
    out = ""
    for i in d.keys():
        nas = d[i]
        if nas > 0:
            nas = "+" + str(nas)
        out += f"{nas}{i}"
    return out.replace("1", "")


data = load_matice("data.txt")
data = troj_matice(data)
state = check_hodnosti(*get_hodnosti(data))
if state == 0:
    reseni = solve(data)
    print([str(i) for i in reseni])
elif state == -1:
    pass
else:
    # state = počet parametrů
    print(f"parametryyyyyyyyyyyyyyyyyyyyyyyy ({state})")
    p = solve_parametry(data, state)
    for j, vyraz in enumerate(p):
        if len(vyraz) > 1:
            promenne = {}

            for i in vyraz:
                if 97 <= ord(i) <= 122:
                    if i not in promenne:
                        promenne[i] = 0
            vyraz = vyraz.replace("--", "+")

            wow = magic(vyraz)
            p[j] = zhezci(wow)

    print(p)
