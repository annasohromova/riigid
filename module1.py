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