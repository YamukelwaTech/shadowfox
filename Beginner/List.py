# Task 1

justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern",
]

no_members = len(justice_league)
print("the number of members is", no_members, "members")

# do not use append
new_members = "Batgirl", "Nightwing"
justice_league.extend(new_members)

print("the new members have been added", justice_league)
