"""
Day 03 Solver
"""

def solve(data: str):
    lines = data.splitlines()

    def max_joltage_part1(s):
        digits = [int(c) for c in s if c.isdigit()]
        n = len(digits)
        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                candidate = digits[i] * 10 + digits[j]
                if candidate > best:
                    best = candidate
        return best

    def max_joltage_part2(s):
        k = 12
        n = len(s)
        need = k
        start = 0
        result = []
        while need > 0:
            end = n - need + 1
            window = s[start:end]
            best_digit = max(window)
            best_index = window.index(best_digit)
            result.append(best_digit)
            start += best_index + 1
            need -= 1
        return int("".join(result))

    part1 = sum(max_joltage_part1(line.strip()) for line in lines if line.strip())
    part2 = sum(max_joltage_part2(line.strip()) for line in lines if line.strip())

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
