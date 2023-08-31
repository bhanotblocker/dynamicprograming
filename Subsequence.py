#print all subsequences



def subsquence(a,ind,ans,ds):


    ans.append(ds[:])
        


    for i in range(ind,len(a)):

        if i!=ind and a[i]==a[i-1]:
            continue


        ds.append(a[i])
        subsquence(a,i+1,ans,ds)
        ds.pop()





a = ['a','b','c','a']
ds = []
ans= []
ind = 0

print(subsquence(a,ind,ans,ds))
print(ans)