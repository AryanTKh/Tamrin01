class Patient:
    def __init__(self, id, name, family_name, age, height, weight):
        self.id = id
        self.name = name
        self.family_name = family_name
        self.age = age
        self.height = height
        self.weight = weight

class DoctorAppointmentSystem:
    def __init__(self):
        self.patients = {}
        self.visits = {}

    def add_patient(self, id, name, family_name, age, height, weight):
        if id in self.patients:
            return "error: this ID already exists"
        if age < 0:
            return "error: invalid age"
        if height < 0:
            return "error: invalid height"
        if weight < 0:
            return "error: invalid weight"
        self.patients[id] = Patient(id, name, family_name, age, height, weight)
        return "patient added successfully"

    def get_patient_info(self, id):
        if id not in self.patients:
            return "error: invalid ID"
        patient = self.patients[id]
        return f"patient name: {patient.name}\npatient family name: {patient.family_name}\npatient age: {patient.age}\npatient height: {patient.height}\npatient weight: {patient.weight}"

    def add_visit(self, id, beginning_time):
        if id not in self.patients:
            return "error: invalid id"
        if not (9 <= beginning_time <= 18):
            return "error: invalid time"
        for visit in self.visits.values():
            if visit["beginning_time"] == beginning_time:
                return "error: busy time"
        patient_visit_times = [visit["beginning_time"] for visit in self.visits.values() if visit["patient_id"] == id]
        if beginning_time in patient_visit_times:
            return "error: patient already has a visit at this time"
        self.visits[len(self.visits) + 1] = {
            "beginning_time": beginning_time,
            "patient_id": id
        }
        return "visit added successfully!"

    def delete_patient(self, id):
        if id not in self.patients:
            return "error: invalid id"
        del self.patients[id]
        self.visits = {k: v for k, v in self.visits.items() if v["patient_id"] != id}
        return "patient deleted successfully!"

    def display_visit_list(self):
        schedule = []
        for visit_id in sorted(self.visits.keys()):
            visit = self.visits[visit_id]
            patient = self.patients[visit["patient_id"]]
            visit_time = str(visit['beginning_time']).zfill(1)
            schedule.append(f"{visit_time}:00 {patient.name} {patient.family_name}")
        return "SCHEDULE:\n" + "\n".join(schedule)

    def process_command(self, command):
        parts = command.split()
        if len(parts) == 0:
            return ""  # Ignore empty lines
        if parts[0] == "add" and parts[1] == "patient" and len(parts) == 8:
            return self.add_patient(int(parts[2]), parts[3], parts[4], int(parts[5]), int(parts[6]), int(parts[7]))
        elif parts[0] == "display" and parts[1] == "patient" and len(parts) == 3:
            return self.get_patient_info(int(parts[2]))
        elif parts[0] == "add" and parts[1] == "visit" and len(parts) == 4:
            return self.add_visit(int(parts[2]), int(parts[3]))
        elif parts[0] == "delete" and parts[1] == "patient" and len(parts) == 3:
            return self.delete_patient(int(parts[2]))
        elif parts[0] == "display" and parts[1] == "visit" and parts[2] == "list" and len(parts) == 3:
            return self.display_visit_list()
        elif parts[0] == "exit" and len(parts) == 1:
            return "exit"
        else:
            return "invalid command"

def main():
    system = DoctorAppointmentSystem()
    while True:
        try:
            command = input().strip()
            result = system.process_command(command)
            if result == "exit":
                break
            if result != "":
                print(result)
        except:
            continue

if __name__ == "__main__":
    main()