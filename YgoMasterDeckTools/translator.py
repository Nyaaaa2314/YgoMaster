
ydkmap = {}
with open("YgoMasterDeckTools\\yk.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        try:
            line = line.split()
            ydkmap[int(line[0])] = int(line[1])
        except:
            pass



with open("YgoMasterDeckTools\\temp.ydk", "r") as f:
    lines = f.readlines()
    lines2 = lines.copy()
    ind = 0
    for line in lines:
        try:
            line = int(line.strip())
            if line > 99999:
                lines2[ind] = str(ydkmap[line]) + ",\n"
            ind += 1
        except:
            ind += 1
    with open("YgoMasterDeckTools\\temp.ydk", "w") as f2:
        f2.writelines(lines2)