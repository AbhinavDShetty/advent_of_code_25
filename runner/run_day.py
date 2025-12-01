import importlib
import time
from typing import Callable
from rich.console import Console
from rich.table import Table
from rich import box
from utils.aoc import fetch_real_input, fetch_example_inputs

console = Console()

def timeit(fn: Callable, *args, **kwargs):
    start = time.perf_counter()
    out = fn(*args, **kwargs)
    end = time.perf_counter()
    return out, (end - start)

def run_day_module(module_name: str, day: int):
    console.rule(f"[bold cyan]Advent of Code — Day {day:02d}")

    try:
        mod = importlib.import_module(module_name)
    except ModuleNotFoundError:
        console.print(f"[red]Module {module_name} not found.[/red]")
        return

    console.print("[yellow]Fetching example inputs...[/yellow]")
    try:
        examples = fetch_example_inputs(day)
    except Exception as e:
        console.print(f"[red]Error fetching examples: {e}[/red]")
        return

    results = []

    for i, ex in enumerate(examples, start=1):
        console.print(f"[green]Running Example #{i}[/green]")
        try:
            (p1, p2), elapsed = timeit(mod.solve, ex)
            results.append(("example", i, p1, p2, elapsed))
        except Exception as e:
            console.print(f"[red]Example #{i} crashed: {e}[/red]")

    console.print("[yellow]Fetching REAL input...[/yellow]")
    try:
        real_input = fetch_real_input(day)
        (p1, p2), elapsed = timeit(mod.solve, real_input)
        results.append(("real", None, p1, p2, elapsed))
    except Exception as e:
        console.print(f"[red]Real input error: {e}[/red]")
        return

    table = Table(title=f"Day {day:02d} Results", box=box.SIMPLE_HEAVY)
    table.add_column("Type")
    table.add_column("Example #")
    table.add_column("Part 1")
    table.add_column("Part 2")
    table.add_column("Time (ms)")

    for typ, idx, p1, p2, t in results:
        row_type = "[magenta]EXAMPLE[/magenta]" if typ == "example" else "[blue]REAL[/blue]"
        idx_str = "-" if idx is None else str(idx)
        table.add_row(row_type, idx_str, str(p1), str(p2), f"{t*1000:.3f}")

    console.print(table)
