from random import randint

def player_attack(dragon_health: int, sword_sharpness: int) -> int:
    hit_value: int = randint(3, 10) + sword_sharpness
    dragon_defence: int = randint(0, 5)
    dragon_health -= hit_value - dragon_defence
    print(f"You hit Dragon: {hit_value}, Dragon defenced: {dragon_defence}, dragon_health is: {dragon_health}!")
    return dragon_health

def dragon_attack(player_health: int, shield_durability: int, spell_blast_damage: int) -> int:
    blast_damage_chance: int = randint(0, 100)
    if blast_damage_chance > 50:
        dragons_hit: int = randint(10, 15)
        players_defence: int = randint(0, 5) + shield_durability
        player_health -= dragons_hit - players_defence
        print(f"Dragon attacked: {dragons_hit}, Player defenced: {players_defence}, Player health is: {player_health}!")
    else:
        player_health -= spell_blast_damage
        print(f"Dragon dealt magic damage: {spell_blast_damage}, Player health is: {player_health}!")
    return player_health

def drink_health_potion(player_health: int, num_of_health_potions: int) -> tuple[int, int]:
    if num_of_health_potions > 0:
        num_of_health_potions -= 1
        player_health += 10
        print(f"You restored 10 health points. Now your health is {player_health}, health potions left: {num_of_health_potions}")
    else:
        print("No health potions left!")
    return player_health, num_of_health_potions

def main() -> None:
    player_health: int = 30
    sword_sharpness: int = 30
    shield_durability: int = 5
    num_of_health_potions: int = 3

    dragon_health: int = 100
    spell_blast_damage: int = 15

    player_input: str = input("Do you want to attack the dragon? (yes/no): ")
    if player_input == "yes":
        while dragon_health > 0 and player_health > 0:
            player_input: str = input("1. Hit the Dragon!, 2. Drink health potion! (or q to quit) ")
            if player_input == "1":
                dragon_health = player_attack(dragon_health, sword_sharpness)
                if dragon_health > 0:
                    player_health = dragon_attack(player_health, shield_durability, spell_blast_damage)
            elif player_input == "2":
                player_health, num_of_health_potions = drink_health_potion(player_health, num_of_health_potions)
            else:
                break

            if player_health <= 0:
                print("You have been defeated. The legends will sing of your bravery!")
            elif dragon_health <= 0:
                print("You have defeated the mighty dragon. You've saved the princess and become the King!")
    elif player_input == "no":
        print("You ran away cowardly... and decades later, only the scar on the cheek of a drunken old man in a tavern "
              "reminded of the once mighty warrior.")

if __name__ == "__main__":
    main()