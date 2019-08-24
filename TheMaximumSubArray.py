def kadane(arr):
    # Solução utilizando Kadane's Algorithm pro somatório de subarrays
    i = 1
    size = len(arr) - 1
    
    # Verifica se array só tem 1 elemento
    if size == 0:
        return [arr[0], arr[0]]
    
    # Flag pra verificar se achou algum número positivo
    positive = False
    
    # Valores iniciais 
    maxCurrent = arr[0]
    maxGlobal = arr[0]
    
    if arr[0] > 0:
        maxSum = arr[0]
        positive = True
        
    else:
        maxSum = 0
        
    while i <= size:
        # Verificações do algoritmo de Kadane
        maxCurrent = max(arr[i], maxCurrent + arr[i])
        
        if maxCurrent > maxGlobal:
            maxGlobal = maxCurrent
        
        # Realiza a soma dos positivos
        if arr[i] > 0:
            maxSum += arr[i]
            positive = True
            
        i = i + 1
    
    if positive == False:
        maxSum = -1
        maxGlobal = -1
        
    return [maxGlobal, maxSum]
