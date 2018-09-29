import os
finname = './input.txt'

try:
    fin = open(finname, 'r')
except IOError, e:
    print "file open error", e
else:
    foutname = './output.txt'

    try:
        fout = open(foutname, 'w')
    except IOError, e:
        print "file open error", e
    else:
        txts = []
        for eachLine in fin:
            print ''.join(eachLine.split(",")[1].split()).__len__(),
            if ''.join(eachLine.split(",")[1].split()) == "Dirty":
                txts.append("Suck")
            elif eachLine.split(",")[0] == "A":
                txts.append("Right")
            elif eachLine.split(",")[0] == "B":
                txts.append("Left")

        fin.close()

        for x in txts:
            fout.writelines(['%s%s' % (x, os.linesep)])
        fout.close()

        f = open("output.txt", "rb+")
        f.seek(-1, os.SEEK_END)
        if f.next() == "\n":
            f.seek(-1, os.SEEK_END)
            f.truncate()
        f.close()

