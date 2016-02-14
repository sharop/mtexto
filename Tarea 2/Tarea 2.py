
# coding: utf-8

# In[1]:

__author__ = 'sharop'

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import string, numpy as np, getopt, sys, random, time, re, pprint, codecs, json
from pprint import pprint

data =[]
with codecs.open('corpus_entrenamiento.jsonline') as f:
    for line in f:
        data.append(json.loads(line.lower()))
    
data_tt =[]
with codecs.open('token_tag.jsonlines') as tt:
    for line in tt:
        data_tt.append(json.loads(line.lower()))
        
        
token_dict ={}
tag_dict ={}


# In[ ]:




# In[2]:

for item in data_tt:
    if tag_dict.has_key(item['tag']):
        tag_dict[item['tag']]= tag_dict[item['tag']]+1
    else:
        tag_dict[item['tag']]= 1
        
    if token_dict.has_key(item['token']):
        token_dict[item['token']]= token_dict[item['token']]+1
    else:
        token_dict[item['token']]= 1


# In[ ]:




# In[3]:

tags=sorted(tag_dict.keys())
tokens = sorted(token_dict.keys())


# In[4]:

B=[[0L for j in range(len(tags)) ] for i in range(len(tokens)) ]
A=[[0L for j in range(len(tags)) ] for i in range(len(tags)) ]


# In[5]:

for doc in data_tt:
    i= tokens.index(doc['token'])    
    j= tags.index(doc['tag'])    
    #if doc['tag']==u'ao':
    #print ((i,j))
    B[i][j] = B[i][j] + 1.0
B = np.array(B)
B = [i/sum(i) for i in B] 


# In[6]:

# Calculo Pi 
Pi =[0L for i in range(len(tags))]
for d in data:
    pTag = d['document'][0]['tag']
    idxTag = tags.index(pTag)
    Pi[idxTag] += 1
    #print (pTag,idxTag,Pi[idxTag])
Pi = np.array(Pi)
Pi = Pi/sum(Pi)


# In[7]:

## Construccion de matrix A
#Iteramos por cada documento
for document in data:
    # Cada documento contiene un elemento que corresponde al contenido.
    tagp=document['document'][0]['tag']
    for i in xrange (1,len(document['document'])):
        tagi = document['document'][i]['tag']
        #print(tagp,tagi)
        A[tags.index(tagp)][tags.index(tagi)] +=1
        tagp = tagi

A = np.array(A)
A = [i/sum(i) for i in A] 


# In[8]:

np.savetxt ('matA.dat',A)
np.savetxt('matB.dat',B)
np.savetxt('matPi.dat',Pi)


# In[ ]:




# In[ ]:



