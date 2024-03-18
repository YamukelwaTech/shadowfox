# Task 1

justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern",
]

# 1
no_members = len(justice_league)
print("the number of members is", no_members, "members")

# 2
# do not use append
new_members = "Batgirl", "Nightwing"
justice_league.extend(new_members)
print("the new members have been added", justice_league)

# 3
wonder_women = justice_league.pop(2)
justice_league.insert(0, wonder_women)
print("the new order is", justice_league)

# 4
removed_hero = "Superman"
justice_league.remove(removed_hero)
justice_league.insert(justice_league.index("Aquaman"), removed_hero)
print("The new order after separating Aquaman and Flash is:", justice_league)

# 5
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("The new team assembled by Superman:", justice_league)

# 6
justice_league.sort()
print(
    "The sorted list of Justice League members is:",
    justice_league,
    "and the new leader is",
    justice_league[0],
)
