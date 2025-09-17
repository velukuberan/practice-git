def table(which_table: int, start: int, end: int) -> None:
    if end < start:
        raise ValueError(f"End({end}) can't be lesser than Start({start})")

    print("\nPrinting the Table\n")

    for i in range(start, end + 1):
        print(f"{which_table:3} x {i:3} = {which_table*i:3}")

which_table = int(input("Which table you want to display: "))
start = int(input("Start of the Table: "))
end = int(input("End of the Table: "))

try:
    table(which_table, start, end)
except ValueError as e:
    print(e)

