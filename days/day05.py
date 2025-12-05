"""
Day 05 Solver
"""

def solve(data: str):
    ranges_part, ids_part = data.strip().split("\n\n")
    ranges = []
    for line in ranges_part.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    ids = [int(line) for line in ids_part.splitlines()]

    fresh_count = 0
    for x in ids:
        if any(start <= x <= end for start, end in ranges):
            fresh_count += 1

    part1 = fresh_count

    ranges.sort()
    merged = []
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    
    merged.append((cur_start, cur_end))

    part2 = sum(end - start + 1 for start, end in merged)

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
