"""
Day 06 Solver
"""
import re

def solve(data: str):
    def solve_part1(data):
        lines = data.splitlines()
        width = max(len(line) for line in lines)
        lines = [line.ljust(width) for line in lines]

        cols = []
        for c in range(width):
            if any(lines[r][c] != ' ' for r in range(len(lines))):
                cols.append(1)
            else:
                cols.append(0)

        segments = []
        i = 0
        while i < width:
            if cols[i] == 1:
                j = i
                while j + 1 < width and cols[j+1] == 1:
                    j += 1
                segments.append((i, j))
                i = j + 1
            else:
                i += 1

        total = 0
        last_row = lines[-1]
        for a, b in segments:
            numbers = []
            for r in range(len(lines) - 1):
                segment = lines[r][a:b+1]
                nums = re.findall(r"\d+", segment)
                numbers.extend(int(n) for n in nums)

            op_segment = last_row[a:b+1]
            op = "+" if "+" in op_segment else "*"
            if op == "+":
                result = sum(numbers)
            else:
                result = 1
                for n in numbers:
                    result *= n
            total += result
        return total


    def solve_part2(data):
        lines = data.splitlines()
        width = max(len(l) for l in lines)
        lines = [l.ljust(width) for l in lines]
        rows = len(lines)
        cols_has_char = [any(lines[r][c] != ' ' for r in range(rows)) for c in range(width)]
        
        segments = []
        i = 0
        while i < width:
            if cols_has_char[i]:
                start = i
                while i + 1 < width and cols_has_char[i+1]:
                    i += 1
                segments.append((start, i))
            i += 1

        grand_total = 0
        for (a, b) in segments:
            op_sub = lines[-1][a:b+1]
            m = re.search(r"[\+\*]", op_sub)
            op = m.group(0) if m else None
            numbers = []
            for col in range(b, a-1, -1):
                chars = [lines[r][col] for r in range(rows-1)]
                digit_str = "".join(chars).strip()
                if re.search(r"\d", digit_str):
                    digits_only = "".join(re.findall(r"\d", digit_str))
                    if digits_only:
                        numbers.append(int(digits_only))
            
            if op == "+":
                result = sum(numbers)
            elif op == "*":
                result = 1
                for n in numbers:
                    result *= n
            else:
                result = 0
            grand_total += result
        return grand_total

    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
