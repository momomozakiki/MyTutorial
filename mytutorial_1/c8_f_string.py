# Prints today's date with help
# of datetime library
import datetime

today = datetime.datetime.today()
print(f"{today}")
print(f"{today:%B %d, %Y}")

answer = 456
print(f'Your answer is "{answer}"')

newline = ord('\n')
print(f"newline: {newline}")
print(f"newline: {newline}")
