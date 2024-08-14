import random
import pandas as pd

# Sample data template
sample_data_template = {
    "Name": "Melinda J Straka",
    "Gender": "Female",
    "Race": "White",
    "Birthday": "4/13/1988",
    "Address": "1300 Chandler Hollow Road, Bridgeville, Pennsylvania(PA), 15017",
    "Telephone": "412-496-1170",
    "Mobile": "412-861-9963",
    "Email (real)": "massivecvn+broadnax@gmail.com",
    "Blood Type": "A+",
    "Mother's Maiden Name": "Clark",
    "Occupation": "Loan Officer",
    "Company Name": "Titania",
    "Company Size": "1-10 employees",
    "Monthly Salary": "$4,100",
    "Security Answer": "asswipe",
    "Vehicle": "2015 Hyundai Elantra",
    "Website": "zoominbeauty.com",
    "Favorite Color": "Gold",
    "Favorite Movie": "Le professionnel(1981)",
    "Favorite Song": "I'm No Superman (Theme)(by Scrubs)",
    "Favorite Book": "Catching Fire (The Hunger Games)",
    "Favorite Sports": "Handball",
    "Username": "hannaleanne",
    "Password": "uale4eiSh",
    "Password after MD5": "a9340c31cd171b8d398585739ddf826e",
    "GUID": "14aead31-e11f-479a-ba0c-bd579e590ee1",
    "Register IP": "132.170.222.230",
    "Last Login IP": "132.170.222.230",
    "Security Question": "What is your cat's name?",
}

# Function to generate random data based on the template
def generate_random_data(template, num_records):
    data_list = []
    for _ in range(num_records):
        data = template.copy()
        data["Name"] = f"Person {_ + 1} {random.choice(['Smith', 'Johnson', 'Brown', 'Williams', 'Jones', 'Davis', 'Garcia', 'Martinez', 'Hernandez', 'Lopez'])}"
        data["Gender"] = random.choice(["Male", "Female", "Non-binary", "Other"])
        data["Race"] = random.choice(["White", "Black", "Asian", "Hispanic", "Native American", "Middle Eastern", "Mixed Race"])
        data["Birthday"] = f"{random.randint(1, 12)}/{random.randint(1, 28)}/19{random.randint(70, 99)}"
        data["Address"] = f"{random.randint(1000, 9999)} {random.choice(['Main', 'High', 'Maple', 'Oak', 'Pine', 'Cedar', 'Elm'])} St, City {random.randint(1, 100)}, State {random.choice(['CA', 'NY', 'TX', 'FL', 'PA', 'IL', 'OH', 'MI', 'GA', 'NC'])}, {random.randint(10000, 99999)}"
        data["Telephone"] = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        data["Mobile"] = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        data["Email (real)"] = f"person{_+1}@{random.choice(['example.com', 'test.com', 'demo.com', 'mail.com'])}"
        data["Blood Type"] = random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        data["Mother's Maiden Name"] = random.choice(["Clark", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Wilson", "Anderson"])
        data["Occupation"] = random.choice(["Loan Officer", "Engineer", "Doctor", "Teacher", "Artist", "Nurse", "Developer", "Lawyer", "Accountant", "Scientist"])
        data["Company Name"] = f"Company {random.randint(1, 100)}"
        data["Company Size"] = random.choice(["1-10 employees", "11-50 employees", "51-200 employees", "201-500 employees", "500+ employees"])
        data["Monthly Salary"] = f"${random.randint(3000, 10000)}"
        data["Security Answer"] = random.choice(["fluffy", "spot", "buddy", "asswipe", "whiskers", "mittens", "snowball", "boots", "tiger", "shadow"])
        data["Vehicle"] = f"20{random.randint(10, 22)} {random.choice(['Hyundai Elantra', 'Toyota Camry', 'Ford F-150', 'Honda Civic', 'Chevrolet Malibu', 'Nissan Altima', 'Jeep Wrangler'])}"
        data["Website"] = f"www.{random.choice(['personalblog', 'billing', 'payment', 'active', 'facebook', 'coolwebsite', 'bestsite', 'randomsite', 'mainsite', 'mysite'])}.com"
        data["Favorite Color"] = random.choice(["Gold", "Blue", "Red", "Green", "Black", "Purple", "Yellow", "Orange", "Pink", "Brown"])
        data["Favorite Movie"] = random.choice(["Le professionnel(1981)", "The Matrix", "Inception", "The Godfather", "Pulp Fiction", "The Dark Knight", "Forrest Gump", "Fight Club", "The Shawshank Redemption", "Titanic"])
        data["Favorite Song"] = random.choice(["I'm No Superman (Theme)(by Scrubs)", "Let it Be (by The Beatles)", "Bohemian Rhapsody (by Queen)", "Imagine (by John Lennon)", "Hotel California (by Eagles)", "Stairway to Heaven (by Led Zeppelin)", "Hey Jude (by The Beatles)", "Smells Like Teen Spirit (by Nirvana)", "Sweet Child O' Mine (by Guns N' Roses)", "Like a Rolling Stone (by Bob Dylan)"])
        data["Favorite Book"] = random.choice(["Catching Fire (The Hunger Games)", "1984 (by George Orwell)", "To Kill a Mockingbird (by Harper Lee)", "The Great Gatsby (by F. Scott Fitzgerald)", "Moby-Dick (by Herman Melville)", "Pride and Prejudice (by Jane Austen)", "The Catcher in the Rye (by J.D. Salinger)", "The Lord of the Rings (by J.R.R. Tolkien)", "Harry Potter and the Sorcerer's Stone (by J.K. Rowling)", "Brave New World (by Aldous Huxley)"])
        data["Favorite Sports"] = random.choice(["Handball", "Football", "Basketball", "Tennis", "Baseball", "Soccer", "Swimming", "Cycling", "Running", "Golf"])
        data["Username"] = f"user{_ + 1}"
        data["Password"] = f"{random.choice(['password1', 'qwerty', 'uale4eiSh', 'letmein', '123456', 'iloveyou', 'admin', 'welcome', 'monkey', 'dragon'])}"
        data["Password after MD5"] = f"{random.choice(['a9340c31cd171b8d398585739ddf826e', 'b1946ac92492d2347c6235b4d2611184', '098f6bcd4621d373cade4e832627b4f6', '5f4dcc3b5aa765d61d8327deb882cf99', 'e99a18c428cb38d5f260853678922e03', 'c4ca4238a0b923820dcc509a6f75849b', 'c81e728d9d4c2f636f067f89cc14862c', 'eccbc87e4b5ce2fe28308fd9f2a7baf3', 'a87ff679a2f3e71d9181a67b7542122c', 'e4da3b7fbbce2345d7772b0674a318d5'])}"
        data["GUID"] = f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}"
        data["Register IP"] = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        data["Last Login IP"] = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        data["Security Question"] = "What is your cat's name?"
        data_list.append(data)
    
    return data_list

# Generate 50 datasets
datasets = generate_random_data(sample_data_template, 50)

# Convert to DataFrame for easier handling
df = pd.DataFrame(datasets)

# Save to CSV
df.to_csv('dataset.csv', index=False)

print("50 enhanced datasets have been generated and saved to 'dataset.csv'.")
