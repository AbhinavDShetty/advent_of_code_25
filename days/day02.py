"""
Day 02 Solver
"""

def solve(data: str):
    parts = [p.strip() for p in data.split(",") if p.strip()]
    ranges = []
    for p in parts:
        a,b = p.split("-")
        ranges.append((int(a), int(b)))
    print(ranges)

    def is_invalid_part1(n):
        s = str(n)
        if len(s) % 2 != 0:
            return False
        half = len(s) // 2
        return s[:half] == s[half:]

    def is_invalid_part2(n):
        s = str(n)
        length = len(s)
        for k in range(1, (length//2) + 1):
            if length % k != 0:
                continue
            block = s[:k]
            repeats = length // k
            if block * repeats == s and repeats >= 2:
                return True
        
        return False
    
    part1, part2 = 0, 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_part1(n):
                part1 += n
            if is_invalid_part2(n):
                part2 += n

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
