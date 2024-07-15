
#判斷
def pandon(text):
    kind = ""
    pandon1 = len(text)
    if text[pandon1-2:] == "ru":
        if text[pandon1-3] == "a"or"u"or"o":
            kind = "5"
        if text[pandon1-3] == "i":
            kind ="last"
        if text[pandon1-3] == "e":
            kind="next"
    if text[pandon1-4:] =="suru":
        kind = "ts"
    if text[pandon1-4:] =="kuru":
        kind = "li"
    if text[pandon1-2:]!= "ru":
        kind = "5"
    return kind


    


#修改

def sugay(la,text):
    len1 = len(text)
    ans = ""

    if la == "5":
        ans = text[:len1-1]+"i"+"masu"


    if la == "last":
        ans = text[:len1-2]+"masu"


    if la == "next":
        ans = text[:len1-2]+"masu"


    if la == "ts":
        ans = text[:len1-4]+"simasu"
    

    if la == "il":
        ans = text[:len1-4]+"kimasu"
    return ans



x1 = 0
x = []
t = int(input())
for _ in range(t):
    x.append(input())

for i in range(t):
    y =pandon(x[x1])
    g = x[x1]
    print(sugay(y,g))
    x1+=1

