class FlightTable:
    def __init__(self):
        self.matches = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        team_matches = []
        for match in self.matches:
            if team_name in (match["Team 01"], match["Team 02"]):
                team_matches.append(match)
        return team_matches

    def search_by_location(self, location_name):
        location_matches = []
        for match in self.matches:
            if match["Location"] == location_name:
                location_matches.append(match)
        return location_matches

    def search_by_timing(self, timing):
        timing_matches = []
        for match in self.matches:
            if match["Timing"] == timing:
                timing_matches.append(match)
        return timing_matches

def main():
    flight_table = FlightTable()

    while True:
        print("Choose a search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter team name: ")
            team_matches = flight_table.search_by_team(team_name)
            print("Matches involving", team_name)
            for match in team_matches:
                print(match)
        elif choice == 2:
            location_name = input("Enter location: ")
            location_matches = flight_table.search_by_location(location_name)
            print("Matches at", location_name)
            for match in location_matches:
                print(match)
        elif choice == 3:
            timing = input("Enter timing: ")
            timing_matches = flight_table.search_by_timing(timing)
            print("Matches with timing", timing)
            for match in timing_matches:
                print(match)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
