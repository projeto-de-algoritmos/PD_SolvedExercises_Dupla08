class Solution:
    def coinChange(self, coins, amount):
        # Inicializa a lista "dp" com infinito para todos os valores de 1 a amount
        dp = [float("inf")] * (amount + 1)
        # O valor 0 é alcançado com 0 moedas, então o valor de dp[0] é 0
        dp[0] = 0
        
        # Loop através de todos os valores de 1 a amount
        for i in range(1, amount + 1):
            # Loop através de todas as moedas disponíveis
            for coin in coins:
                # Se a moeda atual é menor ou igual ao valor atual, atualize dp[i]
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        # Retorna o número mínimo de moedas para alcançar o valor "amount"
        # Se o valor for infinito, significa que não é possível alcançar o valor "amount" com as moedas fornecidas, então retorne -1
        return dp[amount] if dp[amount] != float("inf") else -1