def towerofhanoi(n,source,desnation,auxiliary):
    if n==1:
        print("move disk 1 from source",source,"to desnation",desnation)
        return
    towerofhanoi(n-1,source,auxiliary,desnation)
    print("move disk",n,"from soucre",source,"to desnation",desnation)
    towerofhanoi(n-1,auxiliary,desnation,source)

n=3
towerofhanoi(n,'a','b','c')