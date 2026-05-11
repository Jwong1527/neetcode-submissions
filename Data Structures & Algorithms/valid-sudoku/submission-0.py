class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)

        cols = collections.defaultdict(set)

        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i]
                
                or board[i][j] in cols[j]

                or board[i][j] in squares [ (i // 3, j // 3)] ):
                
                    return False
            
                rows[i].add(board[i][j])

                cols[j].add(board[i][j])

                squares[ (i // 3, j // 3) ].add(board[i][j])

            #If this number has not been yet seen in this 3x3 -> Add it to the set.

        return True #If the false condition never hits -> Return True -> Valid 

        
        