def Multip_Rec(x, y):
    if y <= 1:
        return x
    else:
        return x + Multip_Rec(x, y - 1)


print(Multip_Rec(8, 4))
