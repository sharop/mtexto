import re


rules = ['([aeiou]s)$','(és)$','(íes|úes)','[^aeiouáéíóúiz](es)$','(ces)$','[aeiou](s|x)$']
     


def CheckRule(word):
    appliedrule =[]
    for idx_rule in range(len(rules)):
        appliedrule.append((idx, re.search(rules[idx_rule], word)))

    return appliedrule


        
    

