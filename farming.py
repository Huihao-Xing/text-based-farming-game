from helpers import *

# Prompts user for valid input
# Repeats until they provide an integer between 0 and bound
def valid_input(prompt: str, bound: int) -> int:
    prompt += " [0 to %d]: " % bound
    new_prompt = prompt
    while True:
        inp = input(new_prompt)
        try:
            if 0 <= int(inp) <= bound: return int(inp)
        except: pass
        new_prompt = "Invalid input. " + prompt

# Repeat the game loop for a maximum number of turns
# Repeats forever if max_turns == -1
def main_game_loop(max_turns: int) -> int:

    # Initialize day, rent, balance, and inventory
    day = "Monday"
    rent_payment = 10.0
    balance = 100.0
    chickens = 1
    eggs = 0
    grubs = 0

    # Loop until balance or time runs out
    num_turns = 0
    while num_turns != max_turns and balance >= 0:

        # Keep counting until all turns are played
        num_turns += 1

        # Inform the user of their current situation
        print("%s: %.2f$ rent, %.2f$ dollars, %d chickens, %d eggs, %d grubs." % (
            day, rent_payment, balance, chickens, eggs, grubs))
    
        # Compute the maximum number of grubs the player can buy
        grub_bound = max_grubs(balance)
        
        # Prompt the human player for their grub purchase
        grubs_bought = valid_input("Enter # of grubs to buy", grub_bound)
        
        # Increase grubs by the amount bought
        grubs += grubs_bought
        
        # Decrease balance by the amount spent
        balance -= grubs_bought * 0.05
    
        # Handle egg sales on the weekdays
        if day not in ["Saturday","Sunday"]:

            # Compute the maximum number of dozens the player can sell
            dozen_bound = max_dozens(eggs, day)

            # Prompt the human player for their dozen sales
            dozens_sold = valid_input("Enter # of dozens to sell", dozen_bound)
            
            # Decrease eggs by the amount sold
            eggs -= dozens_sold * 12
            
            # Increase balance by the sales revenue
            balance += dozens_sold * 10

        # Measure total amount of grub used as feed today
        grubs_fed = measure_feed(grubs, chickens)
        
        # Compute total number of chickens slaughtered today
        chickens_slaughtered = slaughter_chickens(grubs, chickens)

        # Decrease grubs inventory by grubs_fed
        grubs -= grubs_fed

        # Decrease chicken inventory by chickens_slaughtered
        chickens -= chickens_slaughtered
        
        # Increase balance by revenue from chickens_slaughtered
        # Each chicken sells for 1$
        balance += chickens_slaughtered * 1

        # Compute total number of new eggs laid    
        eggs_laid = lay_eggs(chickens)
        
        # Compute total number of eggs hatched
        eggs_hatched = hatch(eggs)
        
        # Increase eggs inventory by eggs_laid
        eggs += eggs_laid
        
        # Decrease eggs inventory by eggs_hatched
        eggs -= eggs_hatched

        # Increase chickens inventory by eggs_hatched
        chickens += eggs_hatched
    
        # Inform user how much rent they are paying today
        print(" Paying %.2f rent." % rent_payment)
        
        # Decrease balance by rent_payment
        balance -= rent_payment
        
        # Increase rent_payment by 5%
        rent_payment *= 1.05
        
        # Turn is over, advance to next day of the week
        day = next_day(day)

    # Check the reason the loop ended
    if balance < 0: # balance ran out

        # Tell the player they ran out of money
        print("Game over, you ran out of money in %d days." % num_turns)

    if num_turns == max_turns: # time ran out
        
        # Tell the player their turns are over
        print("Game over, %d turns reached." % num_turns)
    
    # Return the total number of turns and final game state
    return num_turns

if __name__ == "__main__":

    # Start the main game loop
    main_game_loop(-1)

