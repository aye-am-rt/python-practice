

if __name__ == '__main__':
    mat=[[-1, 2, 3],
         [4, 5, -6],
         [7, 8, 9]]
    r=3
    c=3
    
    MinProd=[[0 for i in range(c)] for j in range(r)]
    MaxProd=[[0 for i in range(c)] for j in range(r)]
    MinProd[0][0]=MaxProd[0][0]=mat[0][0]
    
        
    for i in range(r):
        for j in range(c):
            maxVal=float('-inf')
            minVal=float('inf')
            if( i==0 and j==0):
                maxVal=mat[i][j]
                minVal=mat[i][j]
            if i>0:
                tempMax=max(mat[i][j]*MaxProd[i-1][j],mat[i][j]*MinProd[i-1][j])
                maxVal=max(tempMax,maxVal)
                tempMin=min(mat[i][j]*MaxProd[i-1][j],mat[i][j]*MinProd[i-1][j])
                minVal=min(tempMin,minVal)
            if j>0:
                tempMax=max(mat[i][j]*MaxProd[i][j-1],mat[i][j]*MinProd[i][j-1])
                maxVal=max(tempMax,maxVal)
                tempMin=min(mat[i][j]*MaxProd[i][j-1],mat[i][j]*MinProd[i][j-1])
                minVal=min(tempMin,minVal)
            
            MaxProd[i][j]=maxVal
            MinProd[i][j]=minVal
                
            
    print(MaxProd[2][2])
    
        
    print("Max prod mat ===")
    for i in range(3):
        for j in range(3):
            print(MaxProd[i][j],end="  ")
        print("  ")
        
    print("Min prod mat ===")
    for i in range(3):
        for j in range(3):
            print(MinProd[i][j],end="  ")
        print("  ")
    
