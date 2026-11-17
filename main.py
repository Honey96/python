
import json
import os

# Initial Stock
stock = {
    'A+': 10, 'A-': 0, 
    'B+': 5, 'B-': 0, 
    'O+': 8, 'O-': 0, 
    'AB+': 2, 'AB-': 0
}

VALID_BLOOD_GROUPS = {'A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'}
JSON_FILE = "donors.json"

def load_donors():
    """Load donors from donors.json"""
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

donors = load_donors()

def save_donors():
    """Save donors to donors.json"""
    with open(JSON_FILE, "w") as f:
        json.dump(donors, f, indent=4)

def add_donor():
    name = input("Name: ").strip()
    blood_group = input("Blood group: ").strip()
    
    try:
        units = int(input("Units: "))
    except ValueError:
        print("Invalid units. Please enter a positive whole number.")
        return

    if blood_group not in VALID_BLOOD_GROUPS:
        print("(b) Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    if units <= 0:
        print("Units must be a positive whole number.")
        return

    donors.append({"name": name, "blood_group": blood_group, "units": units})
    stock[blood_group] += units
    
    save_donors()
    print(f"Donor saved to {JSON_FILE}. Stock of {blood_group} is now {stock[blood_group]} units.")

def issue_blood():
    blood_group = input("Blood group: ").strip()
    
    try:
        units = int(input("Units: "))
    except ValueError:
        print("Invalid units. Please enter a positive whole number.")
        return

    if blood_group not in VALID_BLOOD_GROUPS:
        print("Invalid blood group.")
        return

    if stock.get(blood_group, 0) < units:
        print(f"(a) Insufficient stock: only {stock.get(blood_group, 0)} unit(s) of {blood_group} available.")
        return

    stock[blood_group] -= units
    print(f"{units} unit(s) of {blood_group} issued.")

def view_stock():
    print("\n--- Current Blood Stock ---")
    for bg, count in stock.items():
        print(f"{bg}: {count} unit(s)")

def search_donors():
    blood_group = input("Blood group: ").strip()
    
    if blood_group not in VALID_BLOOD_GROUPS:
        print("Invalid blood group.")
        return

    matching_donors = [d for d in donors if d['blood_group'] == blood_group]
    
    print(f"Donors with blood group {blood_group}:")
    if not matching_donors:
        print("No donors found.")
    else:
        for idx, donor in enumerate(matching_donors, 1):
            print(f"{idx}. {donor['name']} - {donor['units']} unit(s)")
    print(f"Total donors found: {len(matching_donors)}")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Add donor")
        print("2. Issue blood")
        print("3. View stock")
        print("4. Search donors")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1' or choice.lower() == 'add donor':
            add_donor()
        elif choice == '2' or choice.lower() == 'issue blood':
            issue_blood()
        elif choice == '3' or choice.lower() == 'view stock':
            view_stock()
        elif choice == '4' or choice.lower() == 'search donors':
            search_donors()
        elif choice == '5' or choice.lower() == 'exit':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please select from the menu.")

if __name__ == "__main__":
    main()