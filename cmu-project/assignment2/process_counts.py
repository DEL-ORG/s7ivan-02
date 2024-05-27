import subprocess
from collections import Counter

def get_user_process_counts():
    # Run the ps command to get the list of all users with active processes
    result = subprocess.run(['ps', '-eo', 'user'], capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode != 0:
        print("Error running ps command")
        return

    # Split the output into lines
    lines = result.stdout.splitlines()

    # The first line is the header, so skip it
    users = lines[1:]

    # Use Counter to count the occurrences of each user
    user_counts = Counter(users)

    # Exclude the root user
    if 'root' in user_counts:
        del user_counts['root']

    # Display the results
    for user, count in user_counts.items():
        print(f'User: {user}, Processes: {count}')

# Example usage
get_user_process_counts()
