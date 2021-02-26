# WebScraping_Assignment_2021
Webscraping using python and selenium
## Moodle_Login
This folder consists of a python file moodleLogin.py that takes arguments from the terminal as:
</br>
**python   .\moodleLogin.py   _username_   _password_**
</br>
You are automatically logged into moodle after running the python script thus skipping those irritaing captchas!
## Codeforces
This folder consists of 3 files: 1 for fetching problems of a particular contest and other 2 for bonus tasks. Each of the python scripts run in headless mode. 
### fetch_round.py:
This python script takes contest number as argument along with the file name at the time of running in the terminal:
</br>
**python   .\fetch_round.py   _contest_number_**
</br>
The problems will be downloaded in a hierarchical folder structure, with the contents of a problem kept in the directory ./<contest_number>/<problem_label>/. inside the same directory as the python file. The contents of a problem include photo of the problem statement along with inputs and outputs (present in the problem on codeforces) as text files.
### pastX.py:
This python script takes no. of past contents to be scraped as argument along with the file name at the time of running in the terminal:
</br>
**python   .\pastX.py   _no_of_past_contests_**
</br>
pastX.py finds the past x contests given as argument and accesses the terminal to launch fetch_round.py for each of the contests obtained. The problems will be downloaded in a hierarchical folder structure just likh fetch_round, the difference being, there are now multiple directories for multiple contests. If the past contests given as argument exceeds the past contests given on a single page, the python script navigates to the next page thus making extensive use of page navigation too!
### difficulty_range.py
This python script takes difficulty range setters(start and end), no. of problems as arguments along with the file name at the time of running in the terminal:
</br>
**python   .\difficulty_range.py   _starting_difficulty_lvl_   _ending_difficulty_lvl_   _no_of_problems_to_be_scraped_**
</br>
The problems between the specified difficulty range will be downloaded in a hierarchical folder structure, with the contents of a problem kept in the directory ./<Difficulty_Range_start-end>/<contest_name+problem_label>/. The number of problems to be scraped will depend on the argument in the terminal. There are generally 100 problems on a page after filtering, the python file also takes care of this and makes use of page navigation to get the required no. of problems. 
