while True:
    out = r"""\left(
    \begin{array}{"""

    line = input("Layout? ")
    out += line + "}"

    line = input("Line? ")
    while line != "":
        out += "\n        "
        line = line.split(" ")
        for i in line:
            if len(i.split("/")) == 2:
                a = i.split("/")
                out += "\\frac{"+a[0]+"}{"+a[1]+"}"
            else:
                out += i
            out += " & "
        out = out[:-3]
        out += r"\\"
        line = input("Line? ")
        
    out += r"""
    \end{array}
\right)\\"""
            
    print(out)
