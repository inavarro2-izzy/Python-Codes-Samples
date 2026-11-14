# Israel Navarro
# November 14, 2026
# Check the Dragon Slayer inventory and debuffs for three game tasks.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


def check_task(player, task_name, required_items, blocked_debuff):
    # A task succeeds only when all required items are present
    # and the character does not have the prohibited debuff.
    missing = [item for item in required_items if item not in player.weapons]
    has_debuff = blocked_debuff in player.weaknesses
    print("\nTask:", task_name)
    print("Missing items:", missing if missing else "None")
    print("Blocked by", blocked_debuff + ":", has_debuff)
    if not missing and not has_debuff:
        print("Result: Task can be completed.")
    else:
        print("Result: Task cannot be completed.")
    return not missing and not has_debuff


if __name__ == "__main__":
    player1 = character('', '', '')
    player1.nickname = 'Dragon Slayer'
    player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
    player1.weaknesses = ['slow']

    print("Character:", player1.nickname)
    for item in player1.weapons:
        print("Item:", item)
    for debuff in player1.weaknesses:
        print("Debuff:", debuff)

    # Requirements are taken directly from the lab instructions.
    check_task(player1, "Climb a mountain", ['rope', 'coat', 'first aid kit'], 'slow')
    check_task(player1, "Cook a meal", ['pan', 'groceries'], 'small')
    check_task(player1, "Write a book", ['pen', 'paper', 'idea'], 'confusion')