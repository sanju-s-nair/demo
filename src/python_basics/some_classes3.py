class TheAcademy:
    total_goals = 0
    
    def __init__(self, goals = 1):
        self.goals = goals
        TheAcademy.all_goals = goals + TheAcademy.total_goals

    def update_goals(self, goals):
        self.goals = goals
        self.all_goals = goals + self.total_goals

    def update_total_goals(self, total_goals):
        self.total_goals = total_goals

    def conceded_goals(self, goals):
        self.goals = goals
        self.total_goals = self.total_goals - goals

club_performance = TheAcademy()

club_performance.update_total_goals(15)
club_performance.update_goals(10)
club_performance.conceded_goals(3)

print(club_performance.total_goals)
print(club_performance.all_goals)