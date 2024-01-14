# ********
# This file is individualized for Huihao.
# ********

# TODO: implement next_day
# It accepts one parameter for the current day of the week
# It should return the next day of the week
# Examples:
#   next_day("Monday") -> "Tuesday"
#   next_day("Sunday") -> "Monday"
def next_day(day: str) -> str:
    if day == "Monday":
        return "Tuesday"
    if day == "Tuesday":
        return "Wednesday"
    if day == "Wednesday":
        return "Thursday"
    if day == "Thursday":
        return "Friday"
    if day == "Friday":
        return "Saturday"
    if day == "Saturday":
        return "Sunday"
    if day == "Sunday":
        return "Monday"


# TODO: implement max_grubs
# It accepts one parameter for the current account balance
# It should return the maximum amount of grubs that can be bought
# Each grub costs 0.05
# You cannot buy more grubs than your current balance allows
# You also cannot buy more than 900 grubs
# Examples:
#   max_grubs(1.0) -> 20
#   max_grubs(123456.7) -> 900
def max_grubs(balance: float) -> int:
    number_max = int(balance / 0.05)
    max_default = 900
    max_grub_player_can_buy = min(number_max,max_default)
    return max_grub_player_can_buy

# TODO: implement max_dozens
# It accepts two parameters:
# - current number of eggs in inventory
# - current day of the week
# It should return the maximum amount of dozens that can be sold
# One dozen is 12 eggs, and you can only sell a whole number of dozens
# You can not sell more eggs than you have in inventory
# On Monday and Friday, you can sell at most 3 dozens
# On other weekdays, you can sell at most 2 dozens
# Examples:
#   max_dozens(10, Monday) -> 0
#   max_dozens(200, Friday) -> 3
#   max_dozens(200, Thursday) -> 2
#   max_dozens(20, Monday) -> 1
def max_dozens(eggs: int, day: str) -> int:
    num_in_unit_dozen = int(eggs/12)
    if day == "Monday":
        c = 3
    elif day == "Tuesday":
        c = 2
    elif day == "Wednesday":
        c = 2
    elif day == "Thursday":
        c = 2
    elif day == "Friday":
        c = 3
    else: #day == "Saturday" or "Sunday":
        c = 0

    dozen_can_sold = int(min(num_in_unit_dozen,c))
    return dozen_can_sold

# TODO: implement measure_feed
# It accepts two parameters:
# - current number of grubs in inventory
# - current number of chickens in inventory
# It should return the total amount of grub used for feeding today
# Each chicken must be fed either 9 or 0 grubs
# You must feed 9 grubs to as many chickens in inventory as possible
# You can not use more grub than you have in inventory
# Examples:
#   measure_feed(38, 3) -> 27
#   measure_feed(21, 3) -> 18
def measure_feed(grubs: int, chickens: int) -> int:
    if grubs > (chickens * 9):
        chick_num_can_be_feed = chickens * 9
    if grubs < (chickens * 9):
        for num in range(0,grubs,9):
            chick_num_can_be_feed = num
    else:
        chick_num_can_be_feed = chickens * 9
    return chick_num_can_be_feed

# TODO: implement slaughter_chickens
# It accepts two parameters:
# - current number of grubs in inventory
# - current number of chickens in inventory
# It should return the total number of unfed chickens today
# Each chicken must be fed either 9 or not fed at all
# You must feed 9 grubs to as many chickens in inventory as possible
# You can not use more grub than you have in inventory
# Examples:
#   slaughter_chickens(38, 3) -> 0
#   slaughter_chickens(21, 3) -> 1
def slaughter_chickens(grubs: int, chickens: int) -> int:
    if grubs > (chickens * 9):
        chick_num_can_be_feed = chickens * 9
    if grubs < (chickens * 9):
        for num in range(0,grubs,9):
            chick_num_can_be_feed = num
    else:
        chick_num_can_be_feed = chickens * 9
    chickens_num_feeded = chick_num_can_be_feed / 9
    chicken_unfed = int(chickens - chickens_num_feeded)
    return chicken_unfed

# TODO: implement lay_eggs
# It accepts one parameter for the current number of chickens in inventory
# It should return the total number of eggs laid today
# Use a for-loop to implement the summation formula shown in the instructions
# If there are no chickens, then zero eggs are laid
# Examples:
#   lay_eggs(0) -> 0
#   lay_eggs(1) -> 11
#   lay_eggs(2) -> 11
#   lay_eggs(3) -> 13
#   lay_eggs(4) -> 16
def lay_eggs(chickens: int) -> int:
    if chickens == 0:
        egg = 0
    if chickens < 3 and chickens > 0:
        egg = 11
    if chickens >= 3:
        egg = 0
        for num in range(0,chickens):
            egg = egg + int((11 * ( int(num) / int(chickens - 1) )**2))
    return egg

# TODO: implement hatch
# It accepts one parameter for the current number of eggs in inventory
# It should return the total number of eggs that hatch today
# 20% of the eggs (rounded to the nearest integer) hatch each day.
# Examples:
#   hatch(100) -> 20
#   hatch(12) -> 2
#   hatch(1) -> 0
def hatch(eggs: int) -> int:
    num_hatch = int(eggs * 0.2)
    return num_hatch

