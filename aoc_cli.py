import typer
from rich.console import Console
from runner.run_day import run_day_module
from utils.aoc import fetch_real_input, fetch_example_inputs
from create_day import create_day
import importlib
import time

app = typer.Typer()
console = Console()

@app.command()
def run(day: int):
    """Run all example inputs + real input."""
    run_day_module(f"days.day{day:02d}", day)

@app.command()
def examples(day: int):
    """Print all example inputs."""
    ex = fetch_example_inputs(day)
    for i, block in enumerate(ex, start=1):
        console.rule(f"Example #{i}")
        console.print(block)

@app.command()
def fetch(day: int, kind: str = typer.Option("real", help="real/example")):
    """Fetch raw inputs."""
    if kind == "real":
        console.print(fetch_real_input(day))
    else:
        for i, ex in enumerate(fetch_example_inputs(day), start=1):
            console.rule(f"Example #{i}")
            console.print(ex)

@app.command()
def benchmark(day: int, runs: int = 5):
    """Benchmark solver over N runs of real input."""
    mod = importlib.import_module(f"days.day{day:02d}")
    txt = fetch_real_input(day)
    times = []
    out = None

    for _ in range(runs):
        start = time.perf_counter()
        out = mod.solve(txt)
        end = time.perf_counter()
        times.append(end - start)

    avg = sum(times) / runs
    console.print(f"[blue]Output:[/blue] {out}")
    console.print(f"[green]Average Time:[/green] {avg*1000:.3f} ms")

@app.command()
def create(day: int):
    """Create a dayXX.py template."""
    create_day(day)
    console.print(f"[green]Created template for day {day:02d}[/green]")

if __name__ == "__main__":
    app()
