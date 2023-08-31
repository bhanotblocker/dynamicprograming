def countsubsequence(a,k,ds,ind):

    if k == 0:
        return 1
    
    if ind == 0:
        if a[ind] == k:
            return 1
        else:
            return 0
        


    nottake = countsubsequence(a,k,ds,ind-1)
    take = 0
    if a[ind]<=k:
        take = countsubsequence(a,k-a[ind],ds,ind-1)

    return take+nottake

# memo
def countmemo(a,k,dp,ind):
    if k == 0:
        return 1
    
    if ind == 0:
        if a[ind] ==k:
            return 1
        else:
            return 0
        
    if dp[ind]!=-1:
        return dp[ind]
    nottake = countmemo(a,k,dp,ind-1)
    take = 0
    if a[ind]<= k:
        take = countmemo(a,k-a[ind],dp,ind-1)

    dp[ind] = take+nottake
    return dp[ind]

a = [1,2,2,3]
k = 3
ind = len(a)-1
ds = []
dp = [-1 for i in range(len(a))]
print(countsubsequence(a,k,ds,ind))
print(countmemo(a,k,dp,ind))

