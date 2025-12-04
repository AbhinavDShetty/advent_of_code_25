"""
Day 04 Solver
"""

def solve(data: str):
    
    lines = [list(row) for row in data.split("\n")]
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def count_accessible(grid):
        height = len(grid)
        width = len(grid[0])
        count = 0
        for x in range(height):
            for y in range(width):
                if grid[x][y] != '@':
                    continue
                neighbor = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < height and 0 <= ny < width and grid[nx][ny] == '@':
                        neighbor += 1
                if neighbor < 4:
                    count += 1
        return count
    
    def count_adjacent(grid, x, y):
        height = len(grid)
        width = len(grid[0])
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width and grid[nx][ny] == '@':
                count += 1
        return count

    def simulate_total_removed(grid):
        height = len(grid)
        width = len(grid[0])
        total_removed = 0
        g = [row[:] for row in grid]
        while True:
            to_remove = []
            for x in range(height):
                for y in range(width):
                    if g[x][y] == '@' and count_adjacent(g, x, y) < 4:
                        to_remove.append((x,y))
            if not to_remove:
                break
            for x, y in to_remove:
                g[x][y] = '.'
            total_removed += len(to_remove)
        return total_removed

    
    part1 = count_accessible(lines)
    part2 = simulate_total_removed(lines)

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
