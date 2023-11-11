
# There is 20 devops in the company that should be
# equally assigned to each of 8 scrum teams.
# Find out how many devops engineers will not be assigned
# with a team.
# Also find out how many devops engineers will be in
# each scrum team.

# In order to find number of devops engineers in each team
# divide the num of devops with the num of teams.

num_devops, num_teams = 20, 8

print("Each team will have", num_devops//num_teams, "devops engineers")

print("After the assignment there will be", num_devops%num_teams, "engineers unassigned.")
