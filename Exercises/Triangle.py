class Solution:
    def minimumTotal(self, triangulo):
        n = len(triangulo)
        dp = [0] * (n+1)
        
        # percorre o triangulo de baixo para cima
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                # usa programação dinâmica para atualizar dp
                dp[j] = triangulo[i][j] + min(dp[j], dp[j+1])
        
        # retorna a soma mínima do triângulo
        return dp[0]