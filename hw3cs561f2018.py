import numpy
import sys
import os


dirc = [[0, -1], [1, 0], [0, 1], [-1, 0]]


def next_best1():
    de = 0
    for ii in range(0, size):
        for jj in range(0, size):
            if ii == x and jj == y:
                continue
            maxvalue = -sys.maxint-1
            for dd in range(0, 4):
                value = values[ii][jj]
                if (ii+dirc[dd][0]<0) or (ii+dirc[dd][0] >= size) or (jj+dirc[dd][1] < 0) or(jj+dirc[dd][1]) >= size:
                    value += 0.9*(0.7 * values1[ii][jj])
                else:
                    value += 0.9*(0.7 * values1[ii+dirc[dd][0]][jj+dirc[dd][1]])
                for d in range(0, 4):
                    if d == dd:
                        continue
                    if (ii + dirc[d][0] < 0) or (ii + dirc[d][0] >= size) or (jj + dirc[d][1] < 0) or (jj + dirc[d][1]) >= size:
                        value += 0.9*(0.1 * values1[ii][jj])
                    else:
                        value += 0.9*(0.1 * values1[ii + dirc[d][0]][jj + dirc[d][1]])
                if value > maxvalue:
                    maxvalue = value
            values2[ii][jj] = maxvalue
            de = max(delta, abs(values2[ii][jj] - values1[ii][jj]))
    return de


def next_best2():
    de = 0
    for ii in range(0, size):
        for jj in range(0, size):
            if ii == x and jj == y:
                continue
            maxvalue = -sys.maxint-1
            for dd in range(0, 4):
                value = values[ii][jj]
                if (ii+dirc[dd][0]<0) or (ii+dirc[dd][0]>=size) or (jj+dirc[dd][1] < 0) or(jj+dirc[dd][1]) >= size:
                    value += 0.9*(0.7 * values2[ii][jj])
                else:
                    value += 0.9*(0.7 * values2[ii+dirc[dd][0]][jj+dirc[dd][1]])
                for d in range(0, 4):
                    if d == dd:
                        continue
                    if (ii + dirc[d][0] < 0) or (ii + dirc[d][0] >= size) or (jj + dirc[d][1] < 0) or (jj + dirc[d][1]) >= size:
                        value += 0.9*(0.1 * values2[ii][jj])
                    else:
                        value += 0.9*(0.1 * values2[ii + dirc[d][0]][jj + dirc[d][1]])
                if value > maxvalue:
                    maxvalue = value
            values1[ii][jj] = maxvalue
            de = max(delta, abs(values1[ii][jj]-values2[ii][jj]))
    return de

for m in range(0,47):
    finname = './input'+str(m)+'.txt'
    print "********************************"
    print finname
    try:
        fin = open(finname, 'r')
    except IOError, e:
        print "file open error", e
    size = int(fin.readline())
    carNums = int(fin.readline())
    obNums = int(fin.readline())
    obs = ["" for i in range(0, obNums)]
    for i in range(0, obNums):
        obs[i] = fin.readline()
    starts = ["" for i in range(0, carNums)]
    for i in range(0, carNums):
        starts[i] = fin.readline()
    ends = ["" for i in range(0, carNums)]
    for i in range(0, carNums):
        ends[i] = fin.readline()
    values = [[-1 for k in range(0, size)] for j in range(0, size)]
    values1 = [[-1 for k in range(0, size)] for j in range(0, size)]
    values2 = [[-1 for k in range(0, size)] for j in range(0, size)]
    foutname = './output.txt'
    try:
        fout = open(foutname, 'w')
    except IOError, e:
        print "file open error", e

    for i in range(0, carNums):
        theta = 0.0001
        values = [[-1 for k in range(0, size)] for j in range(0, size)]
        values1 = [[-1 for k in range(0, size)] for j in range(0, size)]
        values2 = [[-1 for k in range(0, size)] for j in range(0, size)]
        for s in obs:
            x = int(s.split(",")[0])
            y = int(s.split(",")[1])
            values[x][y] = -101
            values1[x][y] = -101
            values2[x][y] = -101
        x = int(ends[i].split(",")[0])
        y = int(ends[i].split(",")[1])
        values[x][y] = 99
        values1[x][y] = 99
        values2[x][y] = 99
        delta = float("inf")
        round_num = 0
        while delta > theta:
            delta = 0
            if round_num % 2 == 0:
                delta = next_best1()
            #print values2
            else:
                delta = next_best2()
            #print values1
        #print delta
            round_num += 1
        #if round_num%2 == 0:
         #   print values1
        #else:
        #    print values2
        sum = 0
        for j in range(0, 10):
            count = 0
            posx = int(starts[i].split(",")[0])
            posy = int(starts[i].split(",")[1])
            numpy.random.seed(j)
            swerve = numpy.random.random_sample(1000000)
            kk = 0
            ties = [3,1,2,0]
            #if i == 3:
                #print "round", j
            while not (posx == x and posy == y):
                #
                    #print k,posx,posy
                move = 0
                if round_num % 2 == 0:
                    maxNum = -sys.maxint-1
                    for k in range(0, 4):
                        if (posx + dirc[ties[k]][0] < 0) or (posx + dirc[ties[k]][0] >= size) or (posy + dirc[ties[k]][1] < 0) or (
                                posy + dirc[ties[k]][1]) >= size:
                            continue
                        if values1[posx+dirc[ties[k]][0]][posy+dirc[ties[k]][1]] > maxNum:
                            maxNum = values1[posx+dirc[ties[k]][0]][posy+dirc[ties[k]][1]]
                            move = ties[k]
                else:
                    maxNum = -sys.maxint - 1
                    for k in range(0, 4):
                        if (posx + dirc[ties[k]][0] < 0) or (posx + dirc[ties[k]][0] >= size) or (posy + dirc[ties[k]][1] < 0) or (
                                posy + dirc[ties[k]][1]) >= size:
                            continue
                        if values2[posx + dirc[ties[k]][0]][posy + dirc[ties[k]][1]] > maxNum:
                            maxNum = values2[posx + dirc[ties[k]][0]][posy + dirc[ties[k]][1]]
                            move = ties[k]

                if swerve[kk] > 0.7:
                    if swerve[kk] > 0.8:
                        if swerve[kk] > 0.9:
                            move = (move+2) % 4
                        else:
                            move = (move+1) % 4
                    else:
                        move = (move+3) % 4
                #if i == 3:
                    #print move, swerve[kk]
                if (posx + dirc[move][0] < 0) or (posx + dirc[move][0] >= size) or (posy + dirc[move][1] < 0) or (
                        posy + dirc[move][1]) >= size:
                    posx = posx
                    posy = posy
                else:
                    posx += dirc[move][0]
                    posy += dirc[move][1]
                count += values[posx][posy]
                kk += 1
            #if i == 4:
                #print count
            sum += count
        #print sum
        print sum//10
        fout.writelines(['%s%s' % (sum//10, os.linesep)])
    fout.close()

    f = open("output.txt", "rb+")
    f.seek(-1, os.SEEK_END)
    if f.next() == "\n":
        f.seek(-1, os.SEEK_END)
        f.truncate()
    f.close()



