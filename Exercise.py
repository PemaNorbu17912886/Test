from queue import Queue

# Initialize a queue to store patient names
patient_queue = Queue()

def register_patient():
    name = input("Enter patient name: ")
    patient_queue.put(name)
    print("Patient registered.")

def remove_patient():
    if not patient_queue.empty():
        removed_patient = patient_queue.get()
        print(f"{removed_patient} has met the doctor and removed from the queue.")
    else:
        print("No patients in the queue.")

def display_patient_queue():
    if not patient_queue.empty():
        print("Current Patient Queue:")
        for index, patient in enumerate(list(patient_queue.queue), start=1):
            print(f"{index}. {patient}")
    else:
        print("No patients in the queue.")

# Main program loop
while True:
    print("\nDesk Manager's Patient Registration and Appointment Scheduling System")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        register_patient()
    elif choice == '2':
        remove_patient()
    elif choice == '3':
        display_patient_queue()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
