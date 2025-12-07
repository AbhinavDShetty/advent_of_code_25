"""
Day 07 Solver
"""
from collections import defaultdict

def solve(data: str):
    grid = [list(line.rstrip("\n")) for line in data.splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    S = None
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == 'S':
                S = (i,j)
                break
        if S:
            break
    
    start = (S[0] + 1, S[1])

    def part1_solution():
        active = {start}
        seen = set()
        splits = 0
        while active:
            nxt = set()
            for (r,c) in active:
                if (r,c) in seen:
                    continue
                seen.add((r,c))
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    continue
                cell = grid[r][c]
                if cell == "^":
                    splits += 1
                    for nc in (c-1, c+1):
                        if 0 <= nc < cols:
                            if (r, nc) not in seen:
                                nxt.add((r, nc))
                else:
                    nr = r + 1
                    if nr < rows:
                        if (nr, c) not in seen:
                            nxt.add((nr, c))
            active = nxt
        return splits

    def part2_solution():
        active = defaultdict(int)
        active[start] = 1
        timelines = 0
        while active:
            nxt = defaultdict(int)
            for (r,c), count in list(active.items()):
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    timelines += count
                    continue
                cell = grid[r][c]
                if cell == "^":
                    for nc in (c-1, c+1):
                        if 0 <= nc < cols:
                            nxt[(r, nc)] += count
                        else:
                            timelines += count
                else:
                    nr = r + 1
                    if nr < rows:
                        nxt[(nr, c)] += count
                    else:
                        timelines += count

            active = nxt
        return timelines






    part1 = part1_solution()
    part2 = part2_solution()

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
