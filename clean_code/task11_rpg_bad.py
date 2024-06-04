from random import randint

player_health = 30
sword_sharpness = 30
shield_durability = 5
num_of_health_potions = 3

dragon_health = 100
dragon_shield = 100
dragon_spell_blast = 3
spell_blast_damage = 15

player_input = input("Do you want to attack the dragon? (yes/no):")
print(player_input)

if player_input == "yes":
    player_input = 1
    while dragon_health > 0 and player_health > 0 and player_input != "q":
        if player_input == 1:
            hit_value = randint(3,10) + sword_sharpness
            dragon_defence = randint(0,5)
            dragon_health -= hit_value - dragon_defence
            print(f"You hit Dragon: {hit_value}, Dragon defenced: {dragon_defence}, dragon_health is: {dragon_health}!")

            blast_damage_chance = randint(0, 100)
            if blast_damage_chance > 50:
                dragons_hit = randint(10, 15)
                players_defence = randint(0, 5) + shield_durability
                player_health -= dragons_hit - players_defence
                print(f"Dragon attacked: {dragons_hit}, Player defenced: {players_defence}, Player health is: {player_health}!")
            else:
                player_health -= spell_blast_damage
                print(f"Dragon dealt magic damage: {spell_blast_damage}, Player health is: {player_health}!")

        elif player_input == 2:
            if num_of_health_potions > 0:
                num_of_health_potions -= 1
                player_health += 10
            print(f"You restored 10 health points. Now your health is {player_health}, health potions left: {num_of_health_potions}")

        if player_health <= 0:
            print("You have been defeted. The legends will sing of your bravery!")
        if dragon_health <= 0:
            print("You have defeted the mighty dragon. You've saved the princess and become the King!")
        player_input = int(input("1. Hit again!, 2. Drink health potion! "))
elif player_input == "no":
    print("You ran away cowardly... and decades later, only the scar on the cheek of a drunken old man in a tavern "
          "reminded of the once mighty warrior.")