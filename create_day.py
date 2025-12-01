import os

TEMPLATE = '''"""
Day {day:02d} Solver
"""

def solve(data: str):
    lines = data.splitlines()

    # TODO: Replace with actual solution
    part1 = "Part 1 Solution"
    part2 = "Part 2 Solution"

    return part1, part2

if __name__ == "__main__":
    print(solve("a\\nb\\nc"))
'''

def create_day(day: int):
    path = f"days/day{day:02d}.py"
    os.makedirs("days", exist_ok=True)
    if os.path.exists(path):
        print(f"{path} already exists.")
        return
    with open(path, "w") as f:
        f.write(TEMPLATE.format(day=day))
