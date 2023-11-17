import re

def extract_email_domains(file_path):
    # Set to store unique email domains
    unique_domains = set()

    # Regular expression pattern for matching email addresses
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')

    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            # Read each line in the file
            for line in file:
                # Find all email addresses in the line using the regular expression
                matches = re.findall(email_pattern, line)
                
                # Extract and add unique domains to the set
                for email in matches:
                    username, domain = email.split('@')
                    unique_domains.add(domain)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    return unique_domains

# Example usage:
file_path = "C:/Users/dhine/Documents/git workouts/python/task/email.txt"
result = extract_email_domains(file_path)

if result:
    print("Unique Email Domains:")
    for domain in result:
        print(domain)
