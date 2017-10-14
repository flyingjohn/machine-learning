# -*- coding: utf-8 -*-
'''
author hahaszj
website hahaszj.top
由于平时都用java,python不是很熟练，所以程序里面包含了大量的函数解释
'''

def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

'''
@desc 创建每项只包含一项的频繁项集

1:map(function,sequence):
map的作用是就是对于sequence里面的所有项进行function(),返回的是list

2:frozenset:
set无序排序且不重复，是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。
基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交集), difference(差集)
和sysmmetric difference(对称差集)等数学运算. sets 支持 x in set, len(set),和 for x in set。
作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, 或其它类序列的操作。
frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。
缺点是一旦创建便不能更改，没有add，remove方法。

3:apriori算法使用了一个原理：频繁项集的子集也是频繁项集，因为{a,b}如果是频繁的，那么a,b单独出现的
概率肯定也大于minsupport
但是，由于不可能知道最大的频繁项集，就算知道了，由于求关联规则需要知道所有的频繁项集，包含1维，2维的，
那么就只能从小到大构造，但是这样的话就不满足上面的原理，如果a,b分别都是频繁的，但是a,b不一定是频繁的，
因为a,b同时出现可能不满足条件
'''
def createC1(dataSet):
    c1=[]
    for transaction in dataSet:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset,c1)
    
'''
@param
D:完整记录
Ck:频繁项集
minSupport:最小支持度
@desc 这里产生的是频繁项集，上面的C1叫做候选频繁项集
用C代表候选集，L代表频繁项集
'''
def scanD(D,Ck,minSupport):
    ssCnt={}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can): ssCnt[can]=1
                else : ssCnt[can]+=1
                
    numItems=float(len(D))
    retList=[]
    supportData={}
    for key in ssCnt:
        support=ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key]=support
    return retList,supportData

'''
@param
Lk 频繁项集
k 需要得到的新的频繁项集的每项的个数
@desc 比较每项的前k-2项，然后求并集，加上每项的最后一项，合成之后就是k项
由于是从1得到2，一次得到k+1,而且循环里面的j取指造成不会重复去12，21所以保证了
前k-2项是想等的
'''
def aprioriGen(Lk,k):
    retList=[]
    lenLk=len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1=list(Lk[i])[:k-2]
            L2=list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1==L2:
                retList.append(Lk[i] | Lk[j])
    return retList
    
'''
@param 
dataSet 初始数据集
minSupport 最小支持度
'''
def apriori(dataSet,minSupport = 0.5):
    C1=createC1(dataSet)
    D=map(set,dataSet)
    L1,supportData=scanD(D,C1,minSupport)
    L=[L1]
    k=2
    while(len(L[k-2])>0):
        #产生候选集
        Ck=aprioriGen(L[k-2],k)
        #根据支持度产生频繁集
        Lk,supK=scanD(D,Ck,minSupport)
        supportData.update(supK)
        L.append(Lk)
        k+=1
    return L,supportData

'''
@param
L 频繁项集
supportData 支持度集
minConf 最小置信度
@desc

'''
def generateRules(L,supportData,minConf=0.7):
    bigRuleList=[]
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1=[frozenset([item]) for item in freqSet]
            print "now h1 is:",H1
            if(i>1):
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList

'''
@param
freqSet 频繁项集 由于需要计算支持度 所以这里需要原始频繁项集
h 可以理解为前件或者后件 
最终计算关联规则都是在这里 诸如[1,2],[[1,2],3]之类的freqSet会输入
'''
def calcConf(freqSet,H,supportData,brl,minConf=0.7):
    print "calcConf"
    prunedH=[]
    for conseq in H:
        conf=supportData[freqSet]/supportData[freqSet-conseq]
        if conf >= minConf:
            print freqSet-conseq,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH
    
def rulesFromConseq(freqSet,H,supportData,brl,minConf=0.7):
    print "rulesFromConseq"
    m=len(H[0])
    print "m=",m," freqSet=",len(freqSet)
    #len(H[0])=1
    '''
        m在函数第一次调用的时候一定是1，然后由于存在递归，所以m逐渐增大，此时判断的意思就是
        增大后添加的规则不能大于原始的，也就是[2,3,5]可以产生23->5,所以需要产生23,但是不能
        产生235，这样就会死循环
    '''
    if(len(freqSet)>(m+1)):
        Hmpl=aprioriGen(H,m+1)
        print "hmpl:",Hmpl
        Hmpl=calcConf(freqSet,Hmpl,supportData,brl,minConf)
        if(len(Hmpl)>1):
            rulesFromConseq(freqSet,Hmpl,supportData,brl,minConf)