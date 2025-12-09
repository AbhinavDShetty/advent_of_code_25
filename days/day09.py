"""
Day 09 Solver
"""

def solve(data: str):
    lines = data.splitlines()
    points = [tuple(map(int, pts.split(','))) for pts in lines]

    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            if area > max_area:
                max_area = area

    part1 = max_area
    part2 = "Part 2 Solution"

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
