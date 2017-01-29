#-*- coding: utf-8 -*-

from random import randint, paretovariate
from time import time

def generateSentence(partsNb, maxPartsNb, minPartsNb, paretoDist, onlyOnce, addVoyels, wordsNb):
    global deltatime
    global totalPartsNb
    global totalRolls
    deltatime = time()
    totalPartsNb = 0
    totalRolls = 0

    #parts = ["xwe", "in", "an", "ber", "xo", "ser", "şe", "şî", "çî"] # TODO : Add a lang selector in the UI
    #voyParts = ["û", "e", "a", "i"]
    parts = ["nar", "buk", "vir", "ad", "al", "der", "ser", "ia", "tu", "dem", "thry", "gua", "thir", "ya", "min", "as", "ti", "rith"]
    voyParts = ["a", "e", "i", "o", "u", "y"] # TODO : Move parts in the DB

    if addVoyels == True:
        parts += voyParts

    sentence = []
    for i in range(0, wordsNb):
        sentence.append(generateName(parts, voyParts, partsNb, minPartsNb, maxPartsNb, onlyOnce, paretoDist))

    deltatime = (time()-deltatime)*1000

    return sentence, deltatime, totalPartsNb, totalRolls

def generateName(parts, voyParts, partsNb, minPartsNb, maxPartsNb, onlyOnce, paretoDist): # TODO : Generate with dict ponderation
    global totalPartsNb
    global totalRolls
    global deltatime
    wordPartsNb = partsNb
    name = ""
    takenParts = [];

    if onlyOnce == True and partsNb > 0 and partsNb > len(parts): # TODO: Use Django form validation
        print("Error : partsNb must be <= " + str(len(parts)) + " because onlyOnce=True ( " + str(partsNb) + " given)")
        exit()

    if wordPartsNb <=0 or  wordPartsNb == None:
        if paretoDist == True:
            wordPartsNb = pareto(minPartsNb, maxPartsNb)
        else:
            wordPartsNb = randint(minPartsNb, maxPartsNb)
    totalPartsNb += wordPartsNb

    for i in range(0, wordPartsNb):
        partIndex = randint(0, len(parts)-1)
        totalRolls += 1
        if onlyOnce > 0:
            while partIndex in takenParts and partIndex < len(parts)-len(voyParts)-1: # kind of dirty, we don't want vowels to be rejected
                partIndex = randint(0, len(parts)-1)
                totalRolls += 1
            takenParts.append(partIndex)
        name = name + parts[partIndex]

    return name;

def pareto(a, b):
    result = paretovariate(2)
    if result > 3:
        result = 3
    result = (result-1)*(b-a)/(3-1)+a
    return int(result)
