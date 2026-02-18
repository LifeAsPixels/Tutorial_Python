from rich.console import Console
from rich.panel import Panel
from Tutorial import Advanced

def main():
    console.rule('advanced examples of interning')
    # these are bad examples because they should be False, True
    # but they are True, True
    Advanced.Interning.example1()
    # Advanced.Interning.example2()
    
    console.rule('Examples of using @dataclass, __slots__, and Typing')
    home = Advanced.GeoLocation(34.0522, -118.2437, "Los Angeles")
    console.print(home)

    console.rule('Inspecting the contents of a class instance')
    instance = Advanced.Interning()
    for name, attr in instance.__dict__.items():
        console.print('var name: ', name)
        console.print('attr val: ', attr)
    
    console.rule('Inspecting the contents of a class object')
    for name, attr in Advanced.Interning.__dict__.items():
        console.print('var name: ', name)
        console.print('attr val: ', attr)

if __name__ == '__main__':
    try:
        console = Console()
        main()
    except KeyboardInterrupt:
        console.print("\n")
        console.print(Panel("[bold green]Process Interrupted by User.[/bold green]", title="Shutdown"))
        exit(0)