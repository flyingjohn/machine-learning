#coding=utf-8
# -*- coding: utf-8 -*-


import KNN
from numpy import *
import operator

def classify0(inx,dataSet,labels,k):
    dataSetSize=dataSet.shape[0] 
    #shape是numpy的属性，shape[0]=n row
    diffMat=tile(inx,(dataSetSize,1))-dataSet 
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
        argsort对矩阵进行排序，输出的依旧上司矩阵，里面的元素是从小到大排序后的坐标
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
    group,labels=KNN.createDateSet()
    print classify0([0,0],group,labels,3)