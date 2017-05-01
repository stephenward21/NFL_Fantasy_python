import os
from random import randint
import random
from Team import Team
from Player import Player


players = []



julio_jones = Player("Julio Jones", 5000, 9, "Falcons")
matt_ryan = Player("Matt Ryan", 1000, 7, "Falcons")
devonta_freeman = Player("Devonta Freeman", 1000, 5, "Falcons")

drew_brees = Player("Drew Brees", 5000, 9, "Saints")
mark_ingram = Player("Mark Ingram", 2000, 3, "Saints")
michael_thomas = Player("Michael Thomas", 1000, 4, "Saints")

cam_newton = Player("Cam Newton", 5000, 10, "Panthers")
greg_olsen = Player("Greg Olsen", 900, 6, "Panthers")
kelvin_benjamin = Player("Kelvin Benjamon", 1000, 3, "Panthers")

falcons = Team("Falcons")
saints = Team("Saints")
panthers = Team("Panthers")

teams = {
		"falcons":falcons, 
		"saints": saints,
		"panthers":panthers
	}

teams['falcons'].add_player(julio_jones)
teams['falcons'].add_player(matt_ryan)
teams['falcons'].add_player(devonta_freeman)

teams['panthers'].add_player(cam_newton)
teams['panthers'].add_player(greg_olsen)
teams['panthers'].add_player(kelvin_benjamin)

teams['saints'].add_player(drew_brees)
teams['saints'].add_player(mark_ingram)
teams['saints'].add_player(michael_thomas)


falcons_roster = [julio_jones, matt_ryan, devonta_freeman]
saints_roster = [drew_brees, mark_ingram, michael_thomas]
panthers = [cam_newton, greg_olsen, kelvin_benjamin]



teams_competing_against = []






# ===========================
# ========MAIN LOOP==========
# ============================
os.system('clear')
print "Welcome to the NFC SOUTH TECH BOWL!"
print "What would you like to do? "
print "1. CHOOSE TEAM"
print "2. VIEW ROSTERS"
while True:
	user_input = raw_input("> ")
	os.system('clear')
	if (user_input == "1"):
		print "Select your TEAM"
		counter = 0
		for team in teams:
			counter += 1
			print "%d. %s" % (counter, teams[team].team_name)
		user_choose_team = int(raw_input("> "))
		print "\n"
		os.system('clear')
		if (user_choose_team -1 == 0):
			"%s" % (teams['falcons'].falcon_display())
			"%s" % (teams['falcons'].players[0].print_player())
			print "\n"
			"%s" % (teams['falcons'].players[1].print_player())
			print "\n"
			"%s" % (teams['falcons'].players[2].print_player())
			print "\n"
			"%s" % (teams['falcons'].available_salary())
			"%s" % (teams['falcons'].total_team_strength())
			print "\n"
			print "Would you like to:"
			print "1. COMPETE"
			print "2. EDIT ROSTER"
			user_choose_compete = raw_input("> ")
			os.system('clear')

			# CHOOSING THE FALCONS
			if (user_choose_compete == "1"):
				teams_competing_against.append(teams['saints'])                         # Randomized array of competing teams
				teams_competing_against.append(teams['panthers'])
				challenger = random.choice(teams_competing_against)
				print "You have been set to compete against The %s" % challenger.team_name
				user_accepts_game = raw_input("Accept? Y or N? ")
				if (user_accepts_game == "y"):
					if challenger.team_strength < 21:
						print "You WON! DIRTY BIRD!"
					else:
						print "You LOST"
			elif (user_choose_compete == "2"):
				# counter = 0
				# for team in teams:
				# 	counter += 1
					# print "%d. %s" % (counter, teams[team].team_name)
				print "%s" % teams['falcons'].players[0].name
				print "%s" % teams['falcons'].players[1].name
				print "%s\n" % teams['falcons'].players[2].name
				user_choose_trade = raw_input("Trade your Quarterback? Y or N ")
				print "\n"
				if (user_choose_trade == "y" or user_choose_trade == "Y"):
					print "Choose: "
					print "1. Cam Newton"
					print "2. Drew Brees"
					user_choose_qb = raw_input("> ")
					if (user_choose_qb == "1"):
						teams['falcons'].del_player(matt_ryan)
						teams['falcons'].add_player(cam_newton)
						print "\n"
						print "Your new roster: "
						print "%s" % teams['falcons'].players[0].name
						print "%s" % teams['falcons'].players[1].name
						print "%s\n" % teams['falcons'].players[2].name
					if (user_choose_qb == "2"):
						teams['falcons'].del_player(matt_ryan)
						teams['falcons'].add_player(drew_brees)
						print "\n"
						print "Your new roster: "
						print "%s" % teams['falcons'].players[0].name
						print "%s" % teams['falcons'].players[1].name
						print "%s\n" % teams['falcons'].players[2].name
						
				if (user_choose_trade == "n" or user_choose_trade == "N"):
					pass


			else:
				print "That's not an option!"

		# CHOOSING THE PANTHERS
		elif (user_choose_team -1 == 1):
			"%s" % (teams['panthers'].panther_display())
			"%s" % (teams['panthers'].players[0].print_player())
			print "\n"
			"%s" % (teams['panthers'].players[1].print_player())
			print "\n"
			"%s" % (teams['panthers'].players[2].print_player())
			print "\n"	
			"%s" % (teams['panthers'].available_salary())
			"%s" % (teams['panthers'].total_team_strength())
			print"\n"
			print "Would you like to:"
			print "1. Compete"
			print "2. Edit Roster"
			user_choose_compete = raw_input("> ")
			os.system('clear')
			if (user_choose_compete == "1"):
				teams_competing_against.append(teams['falcons'])                         # Randomized array of competing teams
				teams_competing_against.append(teams['saints'])
				challenger = random.choice(teams_competing_against)
				print "You have been set to compete against The %s" % challenger.team_name
				user_accepts_game = raw_input("Accept? Y or N? ")
				if (user_accepts_game == "y"):
					if challenger.team_strength < 19:
						print "You WON! MR. CHARLOTTE"
					else:
						print "You LOST"
			elif (user_choose_compete == "2"):
				# counter = 0
				# for team in teams:
				# 	counter += 1
				# 	print "%d. %s" % (counter, teams[team].team_name)
				print "%s" % teams['panthers'].players[0].name
				print "%s" % teams['panthers'].players[1].name
				print "%s\n" % teams['panthers'].players[2].name
				user_choose_trade = raw_input("Trade your Quarterback? Y or N ")
				print "\n"
				if (user_choose_trade == "y" or user_choose_trade == "Y"):
					print "Choose: "
					print "1. Matt Ryan"
					print "2. Drew Brees"
					user_choose_qb = raw_input("> ")
					if (user_choose_qb == "1"):
						teams['panthers'].del_player(cam_newton)
						teams['panthers'].add_player(matt_ryan)
						print "\n"
						print "Your new roster: "
						print "%s" % teams['panthers'].players[0].name
						print "%s" % teams['panthers'].players[1].name
						print "%s\n" % teams['panthers'].players[2].name
					if (user_choose_qb == "2"):
						teams['panthers'].del_player(cam_newton)
						teams['panthers'].add_player(drew_brees)
						print "\n"
						print "Your new roster: "
						print "%s" % teams['panthers'].players[0].name
						print "%s" % teams['panthers'].players[1].name
						print "%s\n" % teams['panthers'].players[2].name
						
				if (user_choose_trade == "n" or user_choose_trade == "N"):
					pass
			else:
				print "That's not an option!"

        #CHOOSING THE SAINTS
		elif (user_choose_team -1 == 2):
			"%s" % (teams['saints'].saint_display())
			"%s" % (teams['saints'].players[0].print_player())
			print "\n"
			"%s" % (teams['saints'].players[1].print_player())
			print "\n"
			"%s" % (teams['saints'].players[2].print_player())
			print "\n"
			"%s" % (teams['saints'].available_salary())
			"%s" % (teams['saints'].total_team_strength())
			print"\n"
			print "Would you like to:"
			print "1. Compete"
			print "2. Edit Roster"
			user_choose_compete = raw_input("> ")
			os.system('clear')
			if (user_choose_compete == "1"):
				teams_competing_against.append(teams['falcons'])                         # Randomized array of competing teams
				teams_competing_against.append(teams['panthers'])
				challenger = random.choice(teams_competing_against)
				print "You have been set to compete against The %s" % challenger.team_name
				user_accepts_game = raw_input("Accept? Y or N? ")
				if (user_accepts_game == "y"):
					if challenger.team_strength < 16:
						print "You WON! GO SAINTS!"
					else:
						print "You LOST"
			elif (user_choose_compete == "2"):
				# counter = 0
				# for team in teams:
				# 	counter += 1
				# 	print "%d. %s" % (counter, teams[team].team_name)
					print "%s" % teams['saints'].players[0].name
					print "%s" % teams['saints'].players[1].name
					print "%s\n" % teams['saints'].players[2].name
					user_choose_trade = raw_input("Trade your Quarterback? Y or N ")
					print "\n"
					if (user_choose_trade == "y" or user_choose_trade == "Y"):
						print "Choose: "
						print "1. Cam Newton"
						print "2. Matt Ryan"
						user_choose_qb = raw_input("> ")
						if (user_choose_qb == "1"):
							teams['saints'].del_player(drew_brees)
							teams['saints'].add_player(cam_newton)
							print "\n"
							print "Your new roster: "
							print "%s" % teams['saints'].players[0].name
							print "%s" % teams['saints'].players[1].name
							print "%s\n" % teams['saints'].players[2].name
						if (user_choose_qb == "2"):
							teams['saints'].del_player(drew_brees)
							teams['saints'].add_player(matt_ryan)
							print "\n"
							print "Your new roster: "
							print "%s" % teams['saints'].players[0].name
							print "%s" % teams['saints'].players[1].name
							print "%s\n" % teams['saints'].players[2].name
						
					if (user_choose_trade == "n" or user_choose_trade == "N"):
						pass
			else:
				print "That's not an option!"
	if (user_input == "2"):
		counter = 0
		for team in teams:
			counter += 1
			print "%d. %s" % (counter, teams[team].team_name)
			print "%s" % teams[team].players[0].name
			print "%s" % teams[team].players[1].name
			print "%s\n" % teams[team].players[2].name
			print "ENTER \"1\" to CONTINUE"
