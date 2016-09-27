#!/usr/bin/env python



separator = ','

# Map for label(result) to factor, easy for find the factors of a result.
result2factor = {}

resultClass = {}

# Map for factot to index.
factorIndex = {}

# Factor val types
factorValType = {}

factorType = []

# Map for index to factor.
index2factor = {}

# Factor count for calculate the probability of a factor.
factorCount = {}

# Evert item is a group value of factor probability, so it is a two-level map.
factorProbability = {}

def makeClassifier(resultMap):
    for result in resultMap:
	for index, factorVal in enumerate(resultMap[result]):
	    factor = index2factor[index]
	    if factor not in factorCount:
		factorCount[factor]['sum'] = 0
		for c in resultClass:
		    factorCount[factor][c] = 0
	    factorCount[factor]['sum'] += 1
	    factorCount[factor][result] += 1

def loadData():
    f = open('test', 'r')
    for line in f:
	fields = line.strip().split(separator)
	result = fields[0]
	factors = fields[1:]
	result2factor[result] = factors
	for index, factorVal in enumerate(factors):
	    factor = index2factor[index]
	    if factorVal not in factorValType[factor]:
		factorValType[factor][factorVal] = 0
	    factorValType[factor][factorVal] += 1
	    factorValType[factor]['sum'] += 1
    return result2factor

def init():
    for factor in factorType:
	factorValType[factor] = {}
	factorValType[factor]['sum'] = 0

if __name__ == '__main__':
    init()
    resultMap = loadData()
    classifier = makeClassifier(resultMap)
    doTest(classifier)
