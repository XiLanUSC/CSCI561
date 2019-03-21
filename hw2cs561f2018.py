import os
class Combine(object):
    sTotal = 0
    lTotal = 0


def schoose(rest, start, count1, count2, found):
    #print start
    rs = Combine()
    rs.lTotal = 0
    rs.sTotal = 0
    sfound = False

    for j in range(0, a):
        if SPLA[j] == 1 and j+1 in rest:
            if As[j][13] == 1 and splace[0] <= 0:
                continue
            if As[j][14] == 1 and splace[1] <= 0:
                continue
            if As[j][15] == 1 and splace[2] <= 0:
                continue
            if As[j][16] == 1 and splace[3] <= 0:
                continue
            if As[j][17] == 1 and splace[4] <= 0:
                continue
            if As[j][18] == 1 and splace[5] <= 0:
                continue
            if As[j][19] == 1 and splace[6] <= 0:
                continue
            days = 0
            for ss in As[j][13:20]:
                if ss == "1":
                    days += 1
            count1 += days
            rest.remove(j+1)
            sfound = True
            temp = lchoose(rest, start, count1, count2, True)
            if temp.sTotal > rs.sTotal:
                rs.sTotal = temp.sTotal
                rs.lTotal = temp.lTotal
            count1 -= days
            rest.add(j+1)
    if not sfound and not found:
        rs = Combine()
        rs.sTotal = count1
        rs.lTotal = count2
        return rs
    if not sfound:
        return lchoose(rest, start, count1, count2, False)
    return rs


def lchoose(rest, start, count1, count2, found):
    rs = Combine()
    rs.lTotal = 0
    rs.sTotal = 0
    ffound = False
    for j in range(0, a):
        if LAHSA[j] == 1 and j+1 in rest:
            if As[j][13] == 1 and lplace[0] <= 0:
                continue
            if As[j][14] == 1 and lplace[1] <= 0:
                continue
            if As[j][15] == 1 and lplace[2] <= 0:
                continue
            if As[j][16] == 1 and lplace[3] <= 0:
                continue
            if As[j][17] == 1 and lplace[4] <= 0:
                continue
            if As[j][18] == 1 and lplace[5] <= 0:
                continue
            if As[j][19] == 1 and lplace[6] <= 0:
                continue
            days = 0
            for ss in As[j][13:20]:
                if ss == "1":
                    days += 1
            count2 += days
            rest.remove(j+1)
            ffound = True
            temp = schoose(rest, start, count1, count2, True)
            if temp.lTotal > rs.lTotal:
                rs.lTotal = temp.lTotal
                rs.sTotal = temp.sTotal
            rest.add(j+1)
            count2 -= days
    if not ffound and not found:
        rs = Combine()
        rs.sTotal = count1
        rs.lTotal = count2
        return rs
    if not ffound:
        return schoose(rest, start, count1, count2, False)
    return rs


finname = './input.txt'
try:
    fin = open(finname, 'r')
except IOError, e:
    print "file open error", e
maxNum = 0
maxi = -1
count = 0
b = 0
p = 0
l = 0
s = 0
a = 0
restPlace = set([])
b = int(fin.readline())
p = int(fin.readline())
l = int(fin.readline())
Ls = ["" for i in range(0,l)]
for i in range(0, l):
    Ls[i] = fin.readline()
s = int(fin.readline())
Ss = ["" for i in range(0,s)]
for i in range(0, s):
    Ss[i] = fin.readline()
a = int(fin.readline())
As = ["" for i in range(0,a)]
for i in range(0, a):
    As[i] = fin.readline()
    restPlace.add(int(As[i][0:5]))


SPLA = [0 for j in range(0,a)]
LAHSA = [0 for j in range(0,a)]
splace = [p for j in range(0,7)]
lplace = [b for j in range(0,7)]

for j in range(0,a):
    if As[j][10] == "N" and As[j][11] == "Y" and As[j][12] == "Y":
        SPLA[j] = 1
    if As[j][5] == "F" and int(As[j][6:9]) > 17 and As[j][9] == "N":
        LAHSA[j] = 1
used1 = 0
for s in Ss:
    id1 = int(s)
    restPlace.remove(id1)

    for day in range(0,7):
        if As[id1-1][13+day] == "1":
            splace[day] -= 1
            used1 += 1

used2 = 0
for l in Ls:
    id1 = int(l)
    restPlace.remove(id1)

    for day in range(0,7):
        if As[id1-1][13+day] == "1":
            lplace[day] -= 1
            used2 += 1


for i in range(0, a):
    if SPLA[i] == 1 and LAHSA[i] == 1 and i + 1 in restPlace:
        if As[i][13] == 1 and splace[0] <= 0:
            continue
        if As[i][14] == 1 and splace[1] <= 0:
            continue
        if As[i][15] == 1 and splace[2] <= 0:
            continue
        if As[i][16] == 1 and splace[3] <= 0:
            continue
        if As[i][17] == 1 and splace[4] <= 0:
            continue
        if As[i][18] == 1 and splace[5] <= 0:
            continue
        if As[i][19] == 1 and splace[6] <= 0:
            continue
        days = 0
        for ss in As[i][13:20]:
            if ss == "1":
                days += 1
        used1 += days
        restPlace.remove(i + 1)

        print i
        temp = lchoose(restPlace, i, used1, used2, True)
        print temp.sTotal,temp.lTotal
        if temp.sTotal>maxNum:
            maxi = i
            maxNum = temp.sTotal

        restPlace.add(i+1)
        used1 -= days
if maxi == -1:
    for i in range(0, a):
        if SPLA[i] == 1 and i + 1 in restPlace:
            if As[i][13] == 1 and splace[0] <= 0:
                continue
            if As[i][14] == 1 and splace[1] <= 0:
                continue
            if As[i][15] == 1 and splace[2] <= 0:
                continue
            if As[i][16] == 1 and splace[3] <= 0:
                continue
            if As[i][17] == 1 and splace[4] <= 0:
                continue
            if As[i][18] == 1 and splace[5] <= 0:
                continue
            if As[i][19] == 1 and splace[6] <= 0:
                continue
            days = 0
            for ss in As[i][13:20]:
                if ss == "1":
                    days += 1
            used1 += days
            restPlace.remove(i + 1)

            print i
            temp = lchoose(restPlace, i, used1, used2, True)
            print temp.sTotal, temp.lTotal
            if temp.sTotal > maxNum:
                maxi = i
                maxNum = temp.sTotal

            restPlace.add(i + 1)
            used1 -= days
print As[maxi][0:5]


foutname = './output.txt'
try:
    fout = open(foutname, 'w')
except IOError, e:
    print "file open error", e
fout.writelines(['%s%s' % (As[maxi][0:5], os.linesep)])
fout.close()

f = open("output.txt", "rb+")
f.seek(-1, os.SEEK_END)
if f.next() == "\n":
    f.seek(-1, os.SEEK_END)
    f.truncate()
f.close()
