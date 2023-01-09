import prettytable
import math
table = prettytable.PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Charmer", "Squalor"])
table.add_column("Type", ["electric", "fire", "water"])
table.add_column("Power", ["23", "45", "34"])
table.add_row(["pizazz", "bird", "100"])
table.add_row(["magma", "fire", "120"])
table.add_row(["bulbous", "grass", "65"])
table.add_row(["onix", "Rock", "1000"])
table.add_autoindex("No.")
# table.align["Type"] = "l"  # tapping into the table and changing the variable align into the left align
# table.set_style()
# table.get_string()
print(math.pi)
print(table)
