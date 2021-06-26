# treasure mapping 
row1 = ['💾', '💾', '💾']
row2 = ['💾', '💾', '💾']
row3 = ['💾', '💾', '💾']

mapp = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}".format())
textIn = input("where should be changed :")
listNum = textIn.split(",")
mapp[int(listNum[1])-1][int(listNum[0])-1] = "💿"

print(mapp[0])
print(mapp[1])
print(mapp[2])