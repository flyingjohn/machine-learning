# -*- coding: utf-8 -*-

import apriori 



if __name__=="__main__":
    dataSet=apriori.loadDataSet()
    L,supportData=apriori.apriori(dataSet)
    print "L: ",L
    #print "supportData: ",supportData
    rules=apriori.generateRules(L,supportData)
    print "关联规则是:  ",rules