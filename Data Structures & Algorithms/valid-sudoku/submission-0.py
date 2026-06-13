class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers_seen_in_rows = {}
        numbers_seen_in_columns = {}
        numbers_seen_in_boxes = {}
        for rowNumber in range(9):
            for colNumber in range(9):
                currentNumber = board[rowNumber][colNumber]

                if currentNumber == ".":
                    continue

                currentBox = (rowNumber// 3, colNumber // 3)
                
                if rowNumber not in numbers_seen_in_rows:
                    numbers_seen_in_rows[rowNumber] = set()
                if currentNumber in numbers_seen_in_rows[rowNumber]:
                    return False
                if colNumber not in numbers_seen_in_columns:
                    numbers_seen_in_columns[colNumber] = set()
                # If this 3x3 box does not have a set yet, create one.
                # Example:
                # numbers_seen_in_boxes[(0, 0)] stores numbers seen
                # in the top-left 3x3 box.
                if currentBox not in numbers_seen_in_boxes:
                    numbers_seen_in_boxes[currentBox] = set()
                if currentNumber in numbers_seen_in_columns[colNumber]:
                    return False

                # Check box duplicate:
                # This only checks the set for THIS 3x3 box.
                if currentNumber in numbers_seen_in_boxes[currentBox]:
                    return False

                # If no duplicate was found, record this number.
                numbers_seen_in_rows[rowNumber].add(currentNumber)
                numbers_seen_in_columns[colNumber].add(currentNumber)
                numbers_seen_in_boxes[currentBox].add(currentNumber)
        return True
       








            # check for no duplicates
             
                #check for no duplicates
        # go through the input 
        #go through each row it shouldnt repeat the same num
        #go through each col it shouldnt repeat the same number
        #check the 3 x 3 box but how? check the first 3 inputs in 3 cols in the board
        #box = (row // 3, col // 3)
        #return true if that 
        #return false if not