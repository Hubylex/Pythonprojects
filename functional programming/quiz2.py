def spell(txt):
    if len(txt)==0:
        print(txt)
    else:
        print(txt[-1])
        spell(txt[:-1])


txt = input()
spell(txt)