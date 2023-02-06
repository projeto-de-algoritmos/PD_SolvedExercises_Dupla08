class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Verifique se a lista de entrada está vazia, retorne 0 se estiver
        if not nums:
            return 0

        # Inicialize uma lista "length_of_lis" com todos os elementos definidos como 1
        length_of_lis = [1] * len(nums)

        # Percorra a lista "nums"
        for current_index in range(len(nums)):
            # Verifique todos os elementos antes do elemento atual
            for previous_index in range(current_index):
                # Se o elemento anterior for menor que o elemento atual
                if nums[previous_index] < nums[current_index]:
                    # Atualize o "length_of_lis" no índice atual com o valor máximo entre o valor atual e o valor anterior mais 1
                    length_of_lis[current_index] = max(length_of_lis[current_index], length_of_lis[previous_index]+1)

        # Retorne o valor máximo na lista "length_of_lis"
        return max(length_of_lis)