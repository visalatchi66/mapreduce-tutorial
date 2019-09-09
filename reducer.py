
# coding: utf-8

# In[2]:


def reducer():
    salestotal=0
    oldkey=None
    for line in sys.stdin:
        data=line.strip().split('\t')
        if len(data)!=2:
            continue
        thiskey,thissales=data
        if oldkey and oldkey!=thiskey:
            prin("{0}\t{1}".format(oldkey,salestotal))
            salestotal=0
            oldkey=thiskey
            salestotal+=thissales
        if oldkey!=None:
            print("{0}\t{1}".format(oldkey,salestotal))
def main():
    reducer()

