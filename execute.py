import pandas as pd
import numpy as np
import regex
import emoji
import re
import matplotlib.pyplot as plotter

expfile=input("Enter Dir of File : ")
file = open(expfile,mode='r',encoding="utf8")
data = file.read()
file.close()
#print(data)
pattern = re.compile('\d+:\d+\s+-\s+([a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?):\s+')
messengers = re.findall(pattern,data)
if(len(messengers)==0):
    pattern = re.compile('\d+:\d+\s+[a-z][a-z]\s+-\s+([a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?):\s+')
messengers = re.findall(pattern,data)
senders = (np.unique(messengers))
countdict={}
for sender in senders:
	countdict.update({sender:messengers.count(sender)})
countlist = sorted(countdict.items(), key=lambda kv: kv[1])
#print(countlist)


messages_split = pattern.split(data)

sep_msgs=[]
for each in countdict.keys():
    for msg in range(len(messages_split)):
        if each == messages_split[msg]:
            sep_msgs.append(messages_split[msg+1])

cleaned_sep_msg = []
for each in sep_msgs:
    if '\n0' in each:
        cleaned_sep_msg.append(each.split('\n0'))
    elif '\n1' in each:
        cleaned_sep_msg.append(each.split('\n1'))
    elif '\n2' in each:
        cleaned_sep_msg.append(each.split('\n2'))
    elif '\n3' in each:
        cleaned_sep_msg.append(each.split('\n3'))
my_msg = []
for each in cleaned_sep_msg:
    my_msg.append(each[0])

for each in countdict.keys():
    if messages_split[-2] == each:
        my_msg.insert(countdict[each]-1,messages_split[-1])

        who_sent_what = []
prev = 0
for each in countdict.keys():
    num = countdict[each]
    
    nex = num+prev
    messages = my_msg[prev:nex]
    who_sent_what.append(messages)
    prev = nex


# %% [code]
count=0
countofeach=[]
col2=[]
for entry in who_sent_what:
    countofeach.append(len(entry))
    for text in entry:
        col2.append(text)


col1=[]
for i in range(len(who_sent_what)):
    send=list(countdict.keys())
    for j in range(countofeach[i]):
        col1.append(send[i])

df=pd.DataFrame(list(zip(col2,col1)),columns=['message','sender'])
print(df)
df.groupby(df.sender).count().plot(kind='bar')
plotter.show()


