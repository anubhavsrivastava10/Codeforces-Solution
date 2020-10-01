s = input()
f = input()
x = ord(s[0])-ord(f[0])
y = ord(s[1])-ord(f[1])
print(max(x,y,-x,-y))
while x != 0 or y != 0:
    st = ""
    if x < 0:
      st += "R"
      x = x + 1
    if x > 0:
        st = st + "L"
        x = x - 1
    if y < 0:
        st = st + "U"
        y = y + 1
    if y > 0:
        st = st + "D"
        y = y - 1
    print(st)