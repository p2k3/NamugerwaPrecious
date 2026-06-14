team = "National Team"
morale = 70
strength = 72
injuries = 0
points = 0

print("2026 FIFA World Cup Team Manager")
print()

name = input("Enter your team name or press Enter to use the default: ").strip()
if name != "":
    team = name

week = 1
while week <= 3:
    print()
    print(team + " status")
    print("Morale: " + str(morale))
    print("Strength: " + str(strength))
    print("Injuries: " + str(injuries))
    print("Points: " + str(points))
    print()
    print("Pre-tournament week " + str(week))
    print("1. Training")
    print("2. Friendly match")
    print("3. Recovery")
    print("4. Future feature")

    choice = input("Choose an action: ").strip()

    if choice == "":
        print("Enter a valid choice")
        continue

    if choice == "1":
        strength += 4
        morale += 2
        print("Training improved the team.")
    elif choice == "2":
        strength += 2
        morale += 4
        injuries += 1
        print("The friendly match built confidence.")
    elif choice == "3":
        if injuries > 0:
            injuries -= 1
            morale += 3
            print("The team recovered well.")
        else:
            print("No injuries to recover from.")
            continue
    elif choice == "4":
        print("This feature will be added later.")
        continue
    else:
        print("Invalid choice")
        continue

    if morale > 100:
        morale = 100
    if strength > 100:
        strength = 100

    week += 1

match = 1
while match <= 3:
    print()
    print(team + " status")
    print("Morale: " + str(morale))
    print("Strength: " + str(strength))
    print("Injuries: " + str(injuries))
    print("Points: " + str(points))
    print()
    print("Group stage match " + str(match))
    print("1. Attack")
    print("2. Balanced")
    print("3. Defend")

    choice = input("Choose a tactic: ").strip()

    if choice == "":
        print("Enter a valid tactic")
        continue

    if choice == "1":
        morale += 2
        strength -= 1
        result_score = strength + morale - (injuries * 4) + 8
    elif choice == "2":
        result_score = strength + morale - (injuries * 4) + 4
    elif choice == "3":
        morale -= 1
        result_score = strength + morale - (injuries * 4)
    else:
        print("Invalid tactic")
        continue

    if result_score >= 150:
        print("You won the match")
        points += 3
    elif result_score >= 125:
        print("The match ended in a draw")
        points += 1
    else:
        print("You lost the match")

    if morale > 100:
        morale = 100
    if morale < 0:
        morale = 0
    if strength > 100:
        strength = 100
    if strength < 0:
        strength = 0

    if points >= 7:
        print("The team qualified for the knockout stage")
        break

    if match == 3 and points < 4:
        print("The team did not qualify for the knockout stage")
        break

    match += 1

if points < 4:
    print()
    print("Tournament over")
    print("Final points: " + str(points))
else:
    rounds = ["Round of 16", "Quarter-final", "Semi-final", "Final"]
    round_index = 0

    while round_index < len(rounds):
        current_round = rounds[round_index]
        print()
        print(team + " status")
        print("Morale: " + str(morale))
        print("Strength: " + str(strength))
        print("Injuries: " + str(injuries))
        print("Points: " + str(points))
        print()
        print(current_round)
        print("1. Play safe")
        print("2. Take risks")
        print("3. Rest before the match")

        choice = input("Choose an option: ").strip()

        if choice == "":
            print("Enter a valid option")
            continue

        if choice == "1":
            result_score = strength + morale - (injuries * 5) + 6
        elif choice == "2":
            morale += 3
            strength += 1
            result_score = strength + morale - (injuries * 5) + 10
        elif choice == "3":
            if injuries > 0:
                injuries -= 1
                morale += 2
            else:
                print("The squad is already fit")
                continue
            result_score = strength + morale - (injuries * 5) + 2
        else:
            print("Invalid option")
            continue

        if result_score >= 165:
            print("The team won the " + current_round)
            if current_round == "Final":
                print("You won the World Cup")
                break
            points += 3
        else:
            print("The team lost the " + current_round)
            break

        if morale > 100:
            morale = 100
        if strength > 100:
            strength = 100

        round_index += 1

    print()
    print("Tournament summary")
    print("Team: " + team)
    print("Points: " + str(points))
    print("Morale: " + str(morale))
    print("Strength: " + str(strength))
    print("Injuries: " + str(injuries))