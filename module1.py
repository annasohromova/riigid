


def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    file=open(f,'r',ensoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('-') 
        riik_pealinn[k]=v 
        pealinn_riik[v]=k 
    file.close() 
    return riik_pealinn,pealinn_riik 

def leidma(k:dict, v:int):
    word=input()
    x=riigid_pealinnad.get(word)
    if x==None:
        p=riigid_pealinnad.get(word)
        if p==None:
            a=input('Lisada uue riigi või pealinn? ->').lower()
            while a not in ['jah','ei']:
                a=input('Ainult jah või ei')
            if a=='jah':
                loc=input(f'Kas {word} on riigi või pealinn? ').lower() 


def paranda():

    for line in file 


            