text='лырабв абв вова авбфцл лыфабвлыо абвнцш'
list=text.split(' ')
print(list)
for i in range(len(list)-1,-1,-1):
    if 'абв' in list[i]:
        list.remove(list[i])
print(list)