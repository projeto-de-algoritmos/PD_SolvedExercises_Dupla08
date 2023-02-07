class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        
        for col in range(1, num_cols):
            grid[0][col] += grid[0][col-1] # Adiciona a soma da coluna anterior a atual
        for row in range(1, num_rows):
            grid[row][0] += grid[row-1][0] # Adiciona a soma da linha anterior a atual
        
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                current_sum = grid[row][col]
                # Adiciona a soma mínima da linha ou coluna anterior ao caminho atual
                grid[row][col] = current_sum + min(grid[row-1][col], grid[row][col-1])
        
        # Retorna a soma mínima do último elemento da matriz
        return grid[-1][-1]