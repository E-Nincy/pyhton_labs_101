# What data type is the variable `mystery` at the end of the script?
# What data types does it hold at certain points earlier in the script?

mystery = None
# datatype: Nonetype ( represent absence of value)

mystery = "Sommerfeld"
# Datatype: str (string) because it holds a text

mystery = 137
# Datatype: int (integer) now holds a number

mystery = mystery + 0.0
# Datatype: Mistery is 137 (an int)
# 0.0 is a float
# Python automatically promotes int + float, so:
# Final value: 137.0
# Final datatype: float