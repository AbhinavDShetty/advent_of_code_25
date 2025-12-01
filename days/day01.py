"""
Day 01 Solver 
"""

def solve(data: str):
    start = 50
    lines = [ln.strip() for ln in data.strip().splitlines() if ln.strip()]
    rotations = [(ln[0], int(ln[1:])) for ln in lines]

    pos = start % 100
    part1, part2 = 0, 0

    for d, dist in rotations:
        if d == 'R':
            first_zero = (100 - pos) % 100
        else:
            first_zero = pos % 100
        if first_zero == 0:
            first_zero = 100
        if dist < first_zero:
            hits = 0
        else:
            hits = 1 + (dist - first_zero) // 100
        part2 += hits
        if d == 'L':
            pos = (pos - dist) % 100
        else:
            pos = (pos + dist) % 100
        if pos == 0:
            part1 += 1

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
