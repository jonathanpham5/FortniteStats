from src.fortnite import get_stats, build_string_for_stats, get_all_stats, build_string_for_all_stats
from prettytable import *

username = 'default' # Here your username.
platform = 'pc' # Here your platform: psn, xbox, pc.

username = input("Enter username: ")
platform = input("Enter platform(psn, xbox, pc): ")

print("1. Solos")
print("2. Duos")
print("3. Squads")
print("4. All")
choice = input("Enter option for playlist(1-3): ")
if choice == '1':
	playlist = 'p2'
elif choice == '2':
	playlist = 'p10'
elif choice == '3':
	playlist = 'p9'
else:
	playlist = 'all'

print()

if not playlist == 'all':
	data = get_stats(username, playlist, platform)[0]
	print(build_string_for_stats(username, data))
else:
	data = get_all_stats(username, platform)
	build_string_for_all_stats(username, data)