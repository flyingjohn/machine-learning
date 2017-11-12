#coding=utf-8
# -*- coding: utf-8 -*-


import KNN
import numpy as np
import operator
from os import listdir

'''
@param 
filename 储存文本图像的文件名
'''
def img2vector(filename):
    fr=open(filename)
    size=(1,1024)
    #产生一行1024列的矩阵
    returnVect=np.zeros(size)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect
    
def handwritingClassTest():
    hwLabels=[]
    trainingFileList=listdir("trainingDigits")
    m=len(trainingFileList)
    trainingMat=np.zeros((m,1024))
    for i in range(m):
        fileNameStr=trainingFileList[i]
        #文件名类似0_3.txt
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:]=img2vector('trainingDigits/%s' % fileNameStr)
    testFileList=listdir('testDigits')
    errorCount=0.0
    mTest=len(testFileList)
    for i in range(mTest):
        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        vectorUnderTest=img2vector('testDigits/%s' % fileNameStr)
        classifyerResult=classify0(vectorUnderTest,trainingMat,hwLabels,1)
        print "the  classfier came back with:%d,the real answer is:%d" % (classifyerResult,classNumStr)
        if(classifyerResult!=classNumStr):
            errorCount+=1.0
            print "error file is %s" % fileNameStr
    print "\nthe totle number of errors is: %d" % errorCount
    print "\nthe totle error rate is: %f" % (errorCount/float(mTest))

def classify0(inx,dataSet,labels,k):
    dataSetSize=dataSet.shape[0] 
    #shape是numpy的属性，shape[0]=n row
    diffMat=np.tile(inx,(dataSetSize,1))-dataSet 
    '''numpy.tile用于重复构造，详见https://docs.scipy.org/doc/numpy/reference/generated/numpy.tile.html
       此处的作用就是构造了一个和dataSet一样大小的矩阵
    '''
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    '''由于axis=1,代表把最里层的元组相加,如果axis=0代表把所有元组对应位置相加
    详见https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.sum.html#numpy.sum'''
    distance=sqDistances**0.5
    sortedDistIndices=distance.argsort()
    
    '''
        argsort对矩阵进行排序，输出的依旧是矩阵，里面的元素是从小到大排序后的坐标
        详见https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.argsort.html#numpy.argsort
    '''
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndices[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1 #dict.get(key, default=None)
    '''classCount就是分类之后的个数，比如说a:1,b:1等'''
    #sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    sortedClassCount=sorted(classCount.iteritems(),key=lambda x:x[1],reverse=True)
    #print sortedClassCount [('B', 2), ('A', 1)]
    '''
        python内置列表排序函数，详见http://www.cnblogs.com/65702708/archive/2010/09/14/1826362.html    
    '''
    return sortedClassCount[0][0]
    
   
if __name__=="__main__":
    #group,labels=KNN.createDateSet()
    #print classify0([0,0],group,labels,3)
    
    handwritingClassTest()