class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Inicialize o max_product com -inf para garantir que a primeira atualização de max_product seja válida
        max_product = float('-inf')
        # Inicialize current_max e current_min com 1
        current_max = 1
        current_min = 1
        # Loop pelos elementos em nums
        for num in nums:
            # Verifique se o número atual é negativo
            if num < 0:
                # Se o número é negativo, troque current_max e current_min
                current_max, current_min = current_min, current_max
            # Atualize current_max para o maior dos dois: o produto atual ou o número atual
            current_max = max(current_max * num, num)
            # Atualize current_min para o menor dos dois: o produto atual ou o número atual
            current_min = min(current_min * num, num)
            # Atualize max_product para o maior dos dois: max_product ou current_max
            max_product = max(max_product, current_max)
        # Retorne o valor final de max_product
        return max_product