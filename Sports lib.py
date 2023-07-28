class SportRecord:
    def __init__(self, sport, player, score):
        self.sport = sport
        self.player = player
        self.score = score

class SportsRecords:
    def __init__(self):
        self.records = []

    def add_record(self, sport, player, score):
        record = SportRecord(sport, player, score)
        self.records.append(record)
        print("Record added successfully.")

    def display_records(self):
        if not self.records:
            print("No records found.")
        else:
            print("Sports Records:")
            for record in self.records:
                print(f"Sport: {record.sport}, Player: {record.player}, Score: {record.score}")
