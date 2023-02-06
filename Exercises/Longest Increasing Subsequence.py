class Solution:
    # Função para encontrar o comprimento da subsequência crescente mais longa
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Se a lista nums estiver vazia, retorna 0
        if not nums:
            return 0
        
        # Armazena o tamanho da lista nums em n
        n = len(nums)
        
        # Inicializa uma lista dp com tamanho n, com todos os valores inicialmente como 1
        dp = [1] * n
        
        # Loop que varre de 1 até n-1
        for i in range(1, n):
            # Loop que varre todos os elementos anteriores a nums[i]
            for j in range(i):
                # Se nums[j] for menor que nums[i], significa que eles podem ser usados para formar uma subsequência crescente
                if nums[j] < nums[i]:
                    # Atualiza dp[i] como o máximo entre o valor atual de dp[i] e dp[j] + 1
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Retorna o comprimento da subsequência crescente mais longa, que é o máximo valor em dp
        return max(dp)