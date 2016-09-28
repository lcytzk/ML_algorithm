#!/usr/bin/env python
# --*-- coding=utf-8 --*--

class Classifier(object):

    def __init__():
        pass

    def predict(self, features):
        pass

    def dump():
        pass

class Bayes(object):

    def __init__(self, data = None):
        # The types of the result.
        self.labelType = set()
        # Need smooth or not, set smooth will get rid of the occurance of zeros.
        self.smooth = False
        self.classifier = None
        self.exampleSum = 0

        self.labelProb = {}
        self.labelCount = {}
        # Record the count of feature and label for calculating the probability.
        self.featureLabelCount = {}
        self.featureCount = {}
        # The probability of P(x|y), and used to predict other situations.
        self.featureLabelProb = {}
        if data:
            self.makeClassifier(data)

    '''
        Data must organized like label(value) -> features(list)
    '''
    def makeClassifier(self, data):
        self.exampleSum = len(data)
        for label, item in data:
            self.labelType.add(label)
            if label not in self.labelCount:
                self.labelCount[label] = 0
            self.labelCount[label] += 1
            for index, feature in enumerate(item):
                if index not in self.featureLabelCount:
                    self.featureLabelCount[index] = {}
                    self.featureCount[index] = {}
                flcm = self.featureLabelCount[index]
                key = (feature, label)
                if feature not in self.featureCount[index]:
                    self.featureCount[index][feature] = 0
                self.featureCount[index][feature] += 1
                if key not in flcm:
                    flcm[key] = 0
                flcm[key] += 1

        self.calculateProb()

    def calculateLabelProb(self):
        for label in self.labelCount:
            self.labelProb[label] = self.labelCount[label] * 1.0 / self.exampleSum

    def calculateFeatureLabelProb(self):
        for index in self.featureLabelCount:
            self.featureLabelProb[index] = {}
            for feature, label in self.featureLabelCount[index]:
                # prob(feature, label) = count(feature, label) / count(feature)
                self.featureLabelProb[index][(feature, label)] = self.featureLabelCount[index][(feature, label)] * 1.0 / self.labelCount[label]

    def calculateProb(self):
        self.calculateLabelProb()
        self.calculateFeatureLabelProb()

    def predict(self, features):
        resList = []
        for label in self.labelType:
            res = self.labelProb[label]
            print label, res
            for index, feature in enumerate(features):
                key = (feature, label)
                tmp = 0
                if key not in self.featureLabelProb[index]:
                    tmp = 0.00001
                else:
                    tmp = self.featureLabelProb[index][key]
                print feature, label, tmp
                res *= tmp
            resList.append((label, res))
        return resList

    def updateClassifier(self):
        pass

    def dumpClassifier(self):
        pass

    def loadClassifier(self):
        pass

    def outputFeatureLabelCount(self):
        for index in self.featureLabelCount:
            print index
            for key in self.featureLabelCount[index]:
                print key[0], key[1], self.featureLabelCount[index][key]

    def outputFeatureLabelProb(self):
        pass


separator = ','

def loadData():
    f = open('test', 'r')
    result2factor = []
    for line in f:
	fields = line.strip().split(separator)
	result = fields[-1]
        factors = fields[:-1]
	result2factor.append((result, factors))
    return result2factor

def outputResult(m):
    for label, factors in m:
        print label
        print '\t'.join(factors)

def outputFactorVal():
    for key in factorValType:
        print key
        for key2 in factorValType[key]:
            print key2, factorValType[key][key2]

def outputResList(l):
    for i in l:
        print i[0], i[1]

if __name__ == '__main__':
    rawData = loadData()
#    outputResult(rawData)
    bayes = Bayes(rawData)
    resList = bayes.predict(['打喷嚏','建筑工人'])
    outputResList(resList)
    #classifier = makeClassifier(resultMap)
    #doTest(classifier)

