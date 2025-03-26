import os
import datetime
import random
from git import Repo
from datetime import date, timedelta

def list_dates_between(start_date, end_date):
    """
    Returns a list of dates between start_date and end_date (inclusive).

    Args:
        start_date (date): The start date.
        end_date (date): The end date.

    Returns:
        list: A list of dates.
    """
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    return dates

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

    modified_lines = [line.rstrip() + '.\n' for line in lines]

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
    repo.git.commit('--date=', datetime.datetime.strptime(commit_date, "%Y-%m-%d"),
                    '-m', commit_message)
    
    # Push to the remote repository
    origin = repo.remote(name='origin')
    origin.push()

    


if __name__=="__main__":
    
    # Commit counts dictionary
    # commit_count = {1: random.randint(50, 60), 
    #                 2: random.randint(40, 50), 
    #                 3: random.randint(20, 40), 
    #                 4: random.randint(20, 40), 
    #                 5: random.randint(20, 40), 
    #                 6: random.randint(20, 40), 
    #                 7: random.randint(10, 20), 
    #                 8: random.randint(10, 20), 
    #                 9: random.randint(5, 15), 
    #                 10: random.randint(5, 15)}
    
    # commit_count = {1: random.randint(10, 20), 
    #                 2: random.randint(10, 20), 
    #                 3: random.randint(10, 20), 
    #                 4: random.randint(10, 20), 
    #                 5: random.randint(10, 20), 
    #                 6: random.randint(5, 7),
    #                 7: random.randint(5, 7),}
                    
    commit_count = {1: random.randint(10, 20), 
                    # 2: random.randint(10, 15), 
                    # 3: random.randint(10, 15), 
                    4: random.randint(10, 15),}
    
    # commit_count = {1: 2,}
    
    total_commits = sum(commit_count.values())
    print(f'{total_commits}')
    
    git_folder_list = [
        # "ECG-Classifier-Android",
        # "FCNN-Speech-Denoising",
        # "Learning-MMSE-Estimator",
        # "WiFi-Sniffer",
        # "Raspberry-Pi-User-Management",
        # "SVM-Nonlinear-Equalization",
        # "Arduino-Robot-Hand",
        # "Emotion-Recognition",
        "WiFi-Ranging-Positioning", 
        # "AMT-Channel-Simulation",
        ]
    start_date_list = [
        # "2021-05-21",
        # "2019-08-25",
        # "2019-01-13",
        # "2018-08-25",
        # "2020-08-29",
        # "2020-01-14",
        # "2017-08-16",
        # "2017-02-20",
        # "2021-01-01",
        # "2018-08-25",
        # "2018-05-01",
        # "2019-05-29",
        "2025-01-01",
        ]
    end_date_list = [
        # "2021-08-14",
        # "2019-12-17",
        # "2019-05-27",
        # "2018-12-17",
        # "2020-12-19",
        # "2020-05-29",
        # "2018-05-01",
        # "2018-08-31",
        # "2024-12-31",
        # "2021-02-21",
        # "2018-08-25",
        # "2019-08-25",
        "2025-03-20",
        ]
    
    for i in range(len(git_folder_list)):
        sel_folder = git_folder_list[i]
        
        selected_folder = sel_folder
        
        # Parameters
        repo_path = os.path.join(r"E:\Shamman Files\Github", selected_folder)
        file_path = os.path.join(repo_path, 'commit.txt')
        
        # dates in given year
        # commit_year = 2022
        # dates_list = all_dates_in_year(commit_year)
        
        # dates between two days
        start_date = datetime.datetime.strptime(start_date_list[i],"%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_list[i],"%Y-%m-%d").date()
        dates_list = list_dates_between(start_date, end_date)
    
        
        for key, value in commit_count.items():
            
            for _ in range(key):
            
                # Get dates
                selected_dates = random.sample(dates_list, value)
                
                for commit_date in selected_dates:
                    
                    print(f'{commit_date}, {key}, {value}')
                    processed_date = datetime.datetime.strptime(commit_date, "%Y-%m-%d").isoformat()
                
                    # Git
                    commit_message = "from Laptop"
                    # commit_date = datetime(2025, 3, 20, 10, 0, 0)  # Year, Month, Day, Hour, Minute, Second
                    
                    # Modify readme       
                    add_space_to_end_of_lines(file_path)
                
                    # commit_date = datetime(2024, 7, 20, 10, 30, 0)  # Year, Month, Day, Hour, Minute, Second
                    # commit_with_date(repo_path, commit_message, commit_date)
                    
                    # Open the repository
                    repo = Repo(repo_path)
                    
                    # Add all changes
                    repo.git.add(".")
                    
                    # Commit with the specific date
                    # with repo.config_writer() as config:
                    #     config.set_value("user", "name", "shoudha") # Replace with your name
                    #     config.set_value("user", "email", "shammannoorshoudha@gmail.com") # Replace with your email
                    repo.git.commit(message=commit_message, date=processed_date)
                            
                    # Push the changes
                    origin = repo.remote(name='origin')
                    origin.push()
                    
                    
                    