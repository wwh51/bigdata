import os
import sys
from time import ctime

def splitFile(big_file_path, targetFoler, filenum):
    big_file_handler = open(big_file_path, 'r')
    smallfiles = []

    try:
        for i in range(filenum):
            f_path = os.path.join(targetFoler,"%d.txt" % i)
            smallfiles.append(open(f_path, 'a+'))

        while True:
            line = big_file_handler.readline()
            if not line:
                break
            hash_v = abs(hash(line)) % filenum
            smallfiles[hash_v].writelines(line)
    except IOError as err:
        print("I/O error: {0}".format(err))
    except:
        pass
    finally:
        for i in range(len(smallfiles)):
            smallfiles[i].close()
        big_file_handler.close()


def findIP(targetFolder,filenum):
    Result = {}
    for i in range(filenum):
        f_path = os.path.join(targetFolder, "%d.txt" % i)
        if not os.path.exists(f_path):
            continue
        f_h = open(f_path, 'r')
        text = f_h.read()
        f_h.close()
        text = text.split('\n')
        IP = {}
        for l in text:
            IP[l] = IP.get(l,0) + 1

        IPmax = max(IP.items(), key = lambda x : x[1] )
        Result[IPmax[0]] = IPmax[1]

    Result_Max = max(Result.items(), key = lambda x : x[1] )
    print(Result_Max)

if __name__ == '__main__':
    print("Start At: " + str(ctime()))
    splitFile("c:\\temp\\massiveIP.txt", "c:\\temp\\massiveData", 100)
    findIP("c:\\temp\\massiveData", 100)
    print("End At: " + str(ctime()))
