sonastik={}
file=open("riigid_pealinnad.txt","r")
for line in file:
    k, v=line.strip().split('-') 
    sonastik[k.strip()]=v.strip() 

print(sonastik)
