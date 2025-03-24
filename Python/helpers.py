import os
import datetime
import random
from git import Repo


def all_dates_in_year(year):
    """
    Generates a list of all dates in a given year.

    Args:
        year (int): The year for which to generate dates.

    Returns:
        list: A list of strings, each representing a date in 'yyyy-mm-dd' format.
    """
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    dates = []
    for n in range(int((end_date - start_date).days) + 1):
        date = start_date + datetime.timedelta(n)
        dates.append(date.strftime("%Y-%m-%d"))
    return dates


def add_space_to_end_of_lines(file_path):
    """Opens a text file, adds a space to the end of each line, and saves the changes."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    modified_lines = [line.rstrip() + '#\n' for line in lines]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    
    
def commit_with_date(repo_path, commit_message, commit_date):
    """Commits changes to a git repository with a specific date.

    Args:
        repo_path (str): The path to the git repository.
        commit_message (str): The commit message.
        commit_date (datetime): The desired commit date and time.
    """
    repo = Repo(repo_path)
    
    # Stage all changes
    repo.git.add(".")

    # Format the date as required by git
    # date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S %z")

    # Set environment variables for author and committer dates
    # os.environ['GIT_AUTHOR_DATE'] = date_str
    # os.environ['GIT_COMMITTER_DATE'] = date_str

    # Commit the changes
    repo.git.commit('--date=', commit_date,
                    '-m', commit_message)
    
    # Push to the remote repository
    origin = repo.remote(name='origin')
    origin.push()

    


if __name__=="__main__":
    
    # Commit counts dictionary
    # commit_count = {1: random.randint(200, 250), 
    #                 2: random.randint(90, 110), 
    #                 3: random.randint(40, 60), 
    #                 4: random.randint(30, 50), 
    #                 5: random.randint(30, 50), 
    #                 6: random.randint(30, 50), 
    #                 7: random.randint(20, 40), 
    #                 8: random.randint(20, 40), 
    #                 9: random.randint(5, 15), 
    #                 10: random.randint(5, 15)}
    
    commit_count = {1: 1,}
    
    total_commits = sum(commit_count.values())
    print(f'{total_commits}')
    
    # Parameters
    repo_path = r"C:\Shamman Files\Personal\Github\Git-Demo"
    file_path = os.path.join(repo_path, 'readme.txt')
    commit_year = 2024
    year_dates = all_dates_in_year(commit_year)
    
    for key, value in commit_count.items():
        
        for _ in range(key):
        
            # Get dates
            selected_dates = random.sample(year_dates, value)
            
            for commit_date in selected_dates:
                
                print(f'{commit_date}, {key}, {value}')
            
                # Git
                commit_message = "from Laptop"
                # commit_date = datetime(2025, 3, 20, 10, 0, 0)  # Year, Month, Day, Hour, Minute, Second
                
                # Modify readme       
                add_space_to_end_of_lines(file_path)
            
                # commit_date = datetime(2024, 7, 20, 10, 30, 0)  # Year, Month, Day, Hour, Minute, Second
                commit_with_date(repo_path, commit_message, commit_date)