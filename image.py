from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce
from collections import Counter

def createExamples():
    numberArrayexamples = open ('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionWeHave:
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            lineTowrite = str(eachNum)+'::'+str(eiarl)+'\n'
            numberArrayexamples.write(lineTowrite)

def whatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExamp in loadExamps:
        if len(eachExamp)>3:
            splitEx = eachExamp.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x=0
            while x<len(eachPixEx):
                if eachPixEx[x]==eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                
                x+=1


    # print(matchedAr)
    x = Counter(matchedAr)
    print(x)

    GraphX = []
    GraphY = []

    for eachThing in x:
        GraphX.append(eachThing)
        GraphY.append(x[eachThing])
    
    fig = plt.figure()

    ax1  = plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)

    ax1.imshow(iar)
    ax2.bar(GraphX,GraphY,align='center')
    plt.ylim(380)

    plt.show()


def threshold(imgArr):
    balanceAr = []
    newArray = imgArr

    for eachrow in imgArr:
        for eachpix in eachrow:
            avgNum = reduce(lambda x,y:x+y,eachpix[:3])/len(eachpix[:3])
            balanceAr.append(avgNum) 
    balance = reduce(lambda x,y:x+y,balanceAr)/len(balanceAr)

    for eachrow in newArray:
        for eachpix in eachrow:
            if reduce(lambda x,y:x+y,eachpix[:3])/len(eachpix[:3])>balance:
                eachpix[0]=255
                eachpix[1]=255
                eachpix[2]=255
                eachpix[3]=255
            else:
                eachpix[0]=0
                eachpix[1]=0
                eachpix[2]=0
                eachpix[3]=255
    return newArray

whatNumIsThis('images/test4.png')

# i1 = Image.open('images/numbers/0.1.png')
# i1arr = np.array(i1)
# i2 = Image.open('images/numbers/y0.3.png')
# i2arr = np.array(i2)
# i3 = Image.open('images/dot.png')
# i3arr = np.array(i3)
# i4 = Image.open('images/sentdex.png')
# i4arr = np.array(i4)


# threshold(i1arr)
# threshold(i2arr)
# threshold(i3arr)
# threshold(i4arr)

# plt.figure()
# ax1 = plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
# ax2 = plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
# ax3 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
# ax4 = plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)

# ax1.imshow(i1arr)
# ax2.imshow(i2arr)
# ax3.imshow(i3arr)
# ax4.imshow(i4arr)
# plt.show()



