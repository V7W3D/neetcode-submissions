class Solution:
    def hasDuplicate(self, nums: List[str]):
        nums_set = set()
        nums_count = 0
        for n in nums:
            if n != ".":
                nums_set.add(n)
                nums_count += 1
        if nums_count == len(nums_set):
            return False
        return True

    def buildColumn(self, matrix: List[List[str]], index: int) -> List[str]:
        column = []
        for row in matrix:
            column.append(row[index])
        return column
    
    def buildSubBox(self, matrix: List[List[str]], index: (int, int)) -> List[str]:
        box = []
        start_index = (index[0]*3, index[1]*3)
        for i in range(start_index[0], start_index[0]+3):
            row = matrix[i]
            for j in range(start_index[1], start_index[1]+3):
                box.append(row[j])
        return box

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.hasDuplicate(row):
                return False
        for i in range(0,9):
            column = self.buildColumn(board, i)
            if self.hasDuplicate(column):
                return False
        for i in range(0,3):
            for j in range(0,3):
                box = self.buildSubBox(board, (i,j))
                if self.hasDuplicate(box):
                    return False
        return True
