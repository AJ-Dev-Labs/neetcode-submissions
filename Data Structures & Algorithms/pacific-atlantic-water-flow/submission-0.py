class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        p_set, a_set = set(), set()
        p_queue, a_queue = deque(), deque()

        for i in range(COLS):
            p_queue.append((0, i))
            p_set.add((0, i))

        for i in range(ROWS):
            p_queue.append((i, 0))
            p_set.add((i, 0))

        for i in range(COLS):
            a_queue.append((ROWS - 1, i))
            a_set.add((ROWS - 1, i))

        for i in range(ROWS):
            a_queue.append((i, COLS - 1))
            a_set.add((i, COLS - 1))

        def getCells(queue, visit):
            while queue:
                i, j = queue.popleft()
                for i_off, j_off in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    r = i + i_off
                    c = j + j_off
                    if r >= 0 and c >= 0 and r < ROWS and c < COLS and (r,c) not in visit and heights[r][c] >= heights[i][j]:
                        visit.add((r, c))
                        queue.append((r, c))
            return visit

        p_cells = getCells(p_queue, p_set)
        a_cells = getCells(a_queue, a_set)

        return list(p_cells.intersection(a_cells))

        