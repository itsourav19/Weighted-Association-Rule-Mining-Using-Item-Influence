
import itertools
import csv
from itertools import combinations
import time
import psutil

#Read the Database
start=time.time()
df = open('grocery.csv')
csv_f = csv.reader(df)

unique_items = []
transaction = 0

for row in csv_f:
    row = list(filter(None, row))
    transaction += 1
    l = len(row)
    for i in range(0, l):
        if row[i] in unique_items:
            pos = unique_items.index(row[i])
        else:
            unique_items.append(row[i])

for item in unique_items:
    tc = 0
    itmSp = 0
    df.seek(0)
    for row in csv_f:
        row = list(filter (None, row))
        if item in row:
            tc +=1
    itmSp = tc / transaction
    print("\tThe Support of " + str(item) + " => " + str(itmSp))


print("Read " + str(transaction) + " transactions successfully..")
print("\n################### Generating unique items ###################\n")
len=0
for i, e in enumerate(unique_items, 1):
    print(str(i) + '.', e)
    len=len+1
channel2 = channel3 = channel7=item_set2=channel8=unique_items
print(unique_items)
print("length: ",+len)


print("\n !!!!!!!!!!!!!!!!!!!!!! INFLUENCE OF ITEM !!!!!!!!!!!!!!!!!!!!!!!!!!!")
channel4=[]
channel5=[]
k=0
channel6=[]
for x in channel3:
    df.seek(0)
    sum=0
    for row in csv_f:
        row = list(filter(None, row))
        for x1 in row:
            if x==x1:
                #print(row)
                for x2 in row:
                    f0=0
                    if x==x2:
                        continue
                    else:
                        if not channel5:
                            channel5.append(x2)
                            sum=sum+1
                        else:
                            for x3 in channel5:
                                if x3==x2:
                                    f0=1
                                    break
                                else:
                                    continue
                            if f0==0:
                                channel5.append(x2)
                                sum=sum+1
    if(sum!=0):
        res = (sum+1) / len
        res = round(res, 3)
    else:
        res=0
    #print("%.2f" % res)
    print("influence of "+x+" : "+str(res))
    #print(channel5)
    channel5=[]
    channel6.append(res)
    #print("\n")
for i in range(0,len):
    print("influence of "+str(channel3[i])+" : "+str(channel6[i]))

print("!!!!!!!!!!!!!!!!!!Transactional weight!!!!!!!!!!!!!!!!!!!!!!!!!")
t=[]
sum_tw=0
df = open('grocery.csv')
csv_f = csv.reader(df)
c=0
for row in csv_f:
    tw=0
    count=0
    row=list(filter(None,row))
    #print(row)
    for x in row:
        for x1 in range(0,len):
            if x==channel3[x1]:
                tw=tw+channel6[x1]
            else:
                continue
        count=count+1
    k1=tw/count
    k1=round(k1,3)
    sum_tw=sum_tw+k1
    print('Transaction weight of T' +str(c+1)+' : ' +str(k1))
    t.append(k1)
    c=c+1

print("Total sum of Transaction weight: "+str(sum_tw))


#new part added


print("!!!!!!!!!!!!!!!!!!!!!!!!!Influence weight!!!!!!!!!!!!!!!!!!!!!!")
min_inf = float(input("Enter the minimum influence weight :: "))
item_set1=[]
item_set2=[]
channel1=[]
cnt=1
i = 0
while channel7:
    i=i+1
    channel1=[]
    it=0
    print("\n################### Generating Frequent " + str(i) + " item-set ###################\n")
    print(channel7)
    for x in itertools.combinations(channel7, i):
        print(x)
        tno = 0
        rno = 0
        iw = 0
        iw_fsum = 0
        df.seek(0)
        for row in csv_f:
            row = list(filter(None, row))
            x = list(x)
            if (set(x).issubset(row)):
                iw = iw + t[rno]
                tno = tno + 1
            rno = rno + 1
        if tno == 0:
            iw_fsum = 0
        else:
            iw_fsum = iw / sum_tw
        if iw_fsum >= min_inf:
            iw_fsum=round(iw_fsum,3)
            print(str(cnt) + ". " + str(x) + " | " + str(iw_fsum))
            cnt += 1
            item_set1.append(x)
            item_set2.append(iw_fsum)
            channel1.append(x)
            x = list(x)
            it = 1
    if it == 0:
        print("No frequent item set ")
        break

    channel7 = []

    for x in channel1:
        channel7 = channel7 + list(set(x) - set(channel7))

print("\n all the frequent item set")
print(item_set1, "\n")
print(item_set2, "\n")
end=time.time()
print("Execution time: "+str((end-start))+"seconds")


#rule generation
len1=0
ruleno=0
item_set3=[]
item_set4=[]
item_set5=[]
for i in item_set1:
    len1=len1+1
#print(len1)
for i in range(0,len1,1):
    len2=0
    l1=list(item_set1[i])
    for k1 in l1:
        len2=len2+1
    #print("\n")
    #print("For the list: ",l1)
    #print("length: ",len2)
    for j in range(0,len1,1):
        len3=0
        if i==j:
            continue
        else:
            l2=list(item_set1[j])
            for k2 in l2:
                len3=len3+1
            f0=0
            for k3 in range(0,len2,1):
                for k4 in range(0,len3,1):
                    if l1[k3]==l2[k4]:
                        f0=1
                        break
                    else:
                        continue
            if f0==0:
                #print(l2)
                #print("length: ", len3)
                iw_fsum_l1=item_set2[i]
                l3=list(set(l1+l2))
                #print("combined list : ",l3)
                f1=0
                for k5 in range(0,len1,1):
                    result = all(elem in item_set1[k5] for elem in l3)
                    if result:
                        result1 = all(elem in l3 for elem in item_set1[k5])
                        if result1:
                            #print(item_set1[k5])
                            iw_fsum_l2 = item_set2[k5]
                            f1 = 1
                            break
                    else:
                        continue
                if f1==1:
                    iw_fsum_l3 = iw_fsum_l2 / iw_fsum_l1
                    iw_fsum_l3=round(iw_fsum_l3 ,2)
                    ruleno = ruleno + 1
                    #print("\t Rule : ", ruleno, "||", l1, "-->", l2, " : ", iw_fsum_l3)
                    item_set3.append(l1)
                    item_set4.append(l2)
                    item_set5.append(iw_fsum_l3)
                #else:
                    #print("\tXXXXX", l1, "-->", l2,"rule is not possible")
print("||||||||||||||||||||RULES FROM FREQUENT ITEM|||||||||||||||||||||||||")
count1=0
if(ruleno==0):
    print("\n XXXXXXXX   NO RULE XXXXXXXXX")
else:
    for k6 in range(0, ruleno, 1):
        print("\t Rule : ", k6 + 1, "||", item_set3[k6], "-->", item_set4[k6], " : ", item_set5[k6])

    item_set6 = []
    item_set7 = []
    item_set8 = []
    count1 = 0
    min_inf_conf = float(input("Enter the minimum influencial-confidence: "))
    for k7 in range(0, ruleno, 1):
        if (item_set5[k7] >= min_inf_conf):
            count1 = count1 + 1
            temp = []
            temp1 = []
            temp = item_set3[k7]
            item_set6.append(temp)
            temp1 = item_set4[k7]
            item_set7.append(temp1)
            temp2 = item_set5[k7]
            item_set8.append(temp2)

    print("||||||||||||||||||||SIGNIFICANT RULES|||||||||||||||||||||||||")
    for k6 in range(0, count1, 1):
        print("\t Rule : ", k6 + 1, "||", item_set6[k6], "-->", item_set7[k6], " : ", item_set8[k6])

#dissociation part

item_set9=[]
c_t=transaction
for k6 in range(0,count1,1):
    l1=list(item_set6[k6])
    l2=list(item_set7[k6])
    l3=list(set(l1+l2))
    #print(l1,"-->",l2)
    #print("super set: ",l3)
    lf_count=0
    rh_count=0
    c_lr=0
    df = open('Data5.csv')
    csv_f = csv.reader(df)
    for row in csv_f:
        row = list(filter(None, row))
        #print(row)
        if(set(l3).issubset(row)):
            #print(row)
            continue
        else :
            if(set(l1).issubset(row)):
                if(set(l2).issubset(row)):
                    #print(row)
                    continue
                else:
                    lf_count=lf_count+1;
            else:
                if(set(l2).issubset(row)):
                    rh_count=rh_count+1
    #print(lf_count)
    #print(rh_count)
    c_lr=lf_count+rh_count
    #print(c_lr)
    #print(c_t)
    d_value = c_lr / c_t
    d_value = round(d_value, 4)
    #print(d_value)
    item_set9.append(d_value)

print("|||||||||  DISSOCIATION OF RULES  ||||||||||||")
for k7 in range(0,count1,1):
    print("\t Rule : ", k7 + 1, "||", item_set6[k7], "-->", item_set7[k7], " : ", item_set9[k7])

