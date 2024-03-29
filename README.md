In this project you will implement a single-player text-based farming game based on Python. The following three sections
provide an overview of the game, an explanation of the included .py files and how they are organized, and
the specific tasks you need to complete.

Overview:
In this game you raise chickens, buy supplies, sell products, and pay rent each day. Rent gradually increases.
The objective is to keep a positive balance in your bank account as long as possible. Each turn of the game
represents another day on the farm, and repeats the following steps in order:

1. The current day, rent payment, account balance, chicken inventory, egg inventory, and grub inventory
are displayed to the player.
2. The player decides how many new grubs to buy. Grub is food for the chickens. The amount you can
buy is limited by your current account balance, as well as available supply at the grub store.
3. The player decides how many eggs to sell. The amount you can sell is limited by current egg inventory,
as well as current demand at the egg market. Different days of the week have different demand, and
some days the market is closed so no eggs can be sold.
4. The chickens are fed grubs. Each chicken requires a daily serving size to survive, and you feed the
daily serving size to as many chickens as possible. If there is not enough grub to feed all the chickens,
the unfed chickens are slaughtered and sold.
5. The remaining chickens lay new eggs, increasing egg inventory. Different chickens lay different
numbers of eggs.
6. Some eggs are hatched, decreasing egg inventory and increasing chicken inventory.
7. The current rent payment is made, and then the daily rent payment is increased. If the account balance
is below zero, the game ends.

---

The lay_eggs function accepts one parameter for the
current number of chickens in inventory and returns the total number of eggs laid today. If there 
are zero chickens, then zero eggs are laid. If there is one chicken, then 11 eggs are laid. Otherwise,
different chickens produce different numbers of eggs. Suppose you have N > 1 chickens and number
them 1, 2, ..., N, from least to most productive. The 1st chicken produces zero eggs per day, and the
Nth chicken produces 11 eggs per day. In general, for 1 less or equal to k  and k less or equal to N, the number of eggs produced by
the kth chicken is:

![image](https://github.com/Huihao-Xing/text-based-farming-game/assets/119607601/3dd5567e-e9fc-4ea1-a1a0-bfd35ef58488)

where X is the largest integer less than or equal to x. So, the total number of eggs laid is:

![image](https://github.com/Huihao-Xing/text-based-farming-game/assets/119607601/ea210e80-56fa-4c3e-b304-8365c2eaa515)

As a concrete example, if you have N = 3 chickens, the total eggs laid is:

![image](https://github.com/Huihao-Xing/text-based-farming-game/assets/119607601/67ab24de-95b1-4a4d-86c1-645cde2630f9)



