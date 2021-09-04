class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = []
        for i in range(n):
            answer.append([0] * n)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        move_index = 0
        num = 1
        cur_row = 0
        cur_col = -1
        for i in range(n * n):
            cnt = 0
            while True:
                cnt += 1
                if cnt > 100:
                    break
                move = moves[move_index]
                next_row = cur_row + move[0]
                next_col = cur_col + move[1]
                if next_row < 0 or next_row > n-1 or next_col < 0 or next_col > n-1 \
                or answer[next_row][next_col] != 0:
                    move_index = (move_index + 1) % 4
                    continue
                break
            answer[next_row][next_col] = num
            cur_row = next_row
            cur_col = next_col
            num += 1
        return answer