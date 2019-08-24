def getWays(n, c):
    memo = {}
    return dp(c,n,len(c) - 1, memo)

def dp(arr, total, i, memo):
    key = str(total) + " : " + str(i)
    
    if key in memo:
        return memo[key]
    
    if total == 0:
        # Consegui achar a soma
        return 1
    
    if i < 0:
        return 0
    
    if total < 0:
        # Estourei o total, não achei soma
        return 0
    
    if total< arr[i]:
        # A posição atual não está incluida
        result = dp(arr,total,i-1, memo)
    
    else:
        # Testar o caso em que inclui e o que não inclui
        if total == arr[i]:
            # Só precisa considerar a moeda 1x
            result = dp(arr, total - arr[i], i-1, memo) + dp(arr, total, i-1,memo)
        
        else:
            # Considera a moeda mais de uma vez
            result = dp(arr, total - arr[i], i, memo)
            k = arr[i]
            
            while k < total:
                k = k + arr[i]
                result = dp(arr, total - arr[i], i, memo) + dp(arr, total, i-1, memo)
    
    memo[key] = result
    return memo[key]
