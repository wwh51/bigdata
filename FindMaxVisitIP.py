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
    except:
        for i in range(len(smallfiles)):
            smallfiles[i].close()
        big_file_handler.close()
    
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
        IP = sorted(IP.items(), key=lambda d: d[1])
        IPmax=[i for i in IP if i[1] == IP[-1][1] ]
        for i in IPmax:
            Result[i[0]] = i[1]
    Result = sorted(Result.items(), key=lambda d: d[1])    
    Result_Max=[i for i in Result if i[1] == Result[-1][1] ]
    print(Result_Max)    
  
if __name__ == '__main__':  
    print("Start At: " + str(ctime()))
    splitFile("d:\\massiveIP.txt", "d:\\massiveData", 100)
    findIP("d:\\massiveData", 100)
    print("End At: " + str(ctime()))
