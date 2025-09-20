# ================================
# Personal Academic & Life Portfolio
# Author: Darin Word
# ================================

# Personal Info
full_name = "Darin Word"
student_email = "daword@ncat.edu"
hometown = "Fayetteville, NC"
graduation_semester = "Spring 2029"
major = "Computer Science"

# Academic Data
current_courses_list = ['COMP 163', 'MATH 110', 'ENG 100', 'HIS 106', 'GEEN 111', 'COMP SCI']
completed_courses_list = []
credit_hours_list = [3, 4, 3, 3, 1, 1]
GPA_history_lists = [3.6, 2.7, 3.7, 2.9, 3.0]  

# Contact Info
Emergency_contact_tuple = ("Tiffany Johnson (Mom)", "910-555-5555")
Home_address_tuple = ("3019 Chizzle ln", "Fayetteville, NC 28306")
Instagram_info_tuple = ("Instagram", "@_nnirad", 1687)
Twitter_info_tuple = ("Twitter", "@Darinnn_5", 29)
Birthday_tuple = ("Birthday", "15", "7", "2007")

# Interests & Skills
Current_skills_set = {"Python basics", "HTML", "Problem solving", "Time management"}
Skills_to_learn_set = {"JavaScript", "Data structures", "Git", "Web design"}
Career_interests_set = {"Software development", "Web development", "Cyber Security", "Game development"}
Hobbies_set = {"Gaming", "Basketball", "Sleeping", "Music"}
Entertainment_backlog_set = {"One Piece", "Flash", "Demon Slayer"}

#Org. Mapping
Current_course_dict = {"COMP 163": 3,
 "MATH 150": 3, 
 "ENG 101": 3, 
 "HIS 105": 3,}
Course_professors_dict = {"COMP 163": 
"Prof. Rhodes", "MATH 150":"Dr. Lee", 
"ENG 101":"Dr. Martinez", "HIS 105": 
"Dr. Brown"}
Course_room_dict = {"COMP 163": "M-Eric 300", 
"MATH 150": "Marteena 201", 
"ENG 101": "Crosby 121", 
"HIS 105": "Crosby 210"}
Monthly_budget_dict = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
Study_hours_per_subject_dict = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
Contact_directory_dict = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

#Required Calculations
Total_credits = sum(credit_hours_list) #used sum tool to calculate all credit hours
cumulative_gpa = round(sum(GPA_history_lists) / len(GPA_history_lists), 2) #used round tool to round gpa to nearest 100th, sum tool to calculate gpa list, and len tool to divide by gpa list by 4
completed_count = len(completed_courses_list) #used len tool to find how many courses were completed
total_study_hours = sum(Study_hours_per_subject_dict.values()) #used "sum" to add all study hours and "value" so it would take the interger and not the string
Academic_load = (Total_credits) + (total_study_hours) # added all credits with all study hours
monthly_budget_total = sum(Monthly_budget_dict.values()) #used "sum" to add all costly things and values to get the interger
daily_food_budget = round(Monthly_budget_dict["Food"] / 30,2) #used "round" to round up the 100th place and divided by 30 to get Monthly
annual_budget = (monthly_budget_total) * 12 #multiplied monthy budget by 12 to get yearly budget
study_cost_per_hour = round(Monthly_budget_dict["Books"] / total_study_hours, 2) #used "round" to get a interger and then divided by all study hours 

#Analytics Calculations
Total_social_followers = (Instagram_info_tuple[2]) + (Twitter_info_tuple[2]) #use key value to get the right info and add them together
Skills_Comparison = len(Current_skills_set) - len(Skills_to_learn_set) #used "len" to to get current skills and skills to Learn
contact_count = len(Contact_directory_dict) #used "len" to get number of Contacts
backlog_count = len(Entertainment_backlog_set) #used "len" to get number of entertainment backlogs
workload = Total_credits + total_study_hours #added all credits with all study hours

print("================================================================")
print("          PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print("Student:", full_name, "|", "Email:", student_email)
print("From:", hometown, "|", "Graduating:", graduation_semester)
print("Major:", major)
print()
print("=== ACADEMIC PROFILE ===")
print("Current Semester:", Total_credits, "credits across 4 courses")
print("Cumulative GPA:", cumulative_gpa)
print("Weekly Study Time:", total_study_hours, "hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")
print()
print("Current Courses:") 
print("COMP 163 -", Current_course_dict["COMP 163"],"credits -",Course_professors_dict["COMP 163"], "-", Course_room_dict["COMP 163"])
print("MATH 150 -", Current_course_dict["MATH 150"],"credits -",Course_professors_dict["MATH 150"], "-", Course_room_dict["MATH 150"])
print("ENG 101 -", Current_course_dict["ENG 101"],"credits -",Course_professors_dict["ENG 101"], "-", Course_room_dict["ENG 101"])
print("HIS 105 -", Current_course_dict["HIS 105"],"credits -",Course_professors_dict["HIS 105"], "-", Course_room_dict["HIS 105"])
print()
print("=== PERSONAL DEVELOPMENT ===")
print("Current Skills:",Current_skills_set)
print("Learning Goals:",Skills_to_learn_set)
print("Career Interests:",Career_interests_set)
print("Skills Currently Have:", len(Current_skills_set))
print("Skills Want to Learn:", len(Skills_to_learn_set))
print()
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${Monthly_budget_dict["Food"]} (${daily_food_budget}/day)")
print(f"Entertainment: ${Monthly_budget_dict["Entertainment"]}")
print(f"Books: ${Monthly_budget_dict["Books"]}")
print(f"Transportation: ${Monthly_budget_dict["Transportation"]}")
print(f"Annual Projection: ${annual_budget}")
print()
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {Emergency_contact_tuple}")
print(f"Home Address: {Home_address_tuple}")
print(f"Social Media Presence: {Total_social_followers} followers across 2 platforms")
print(f"Key Contacts: {len(Contact_directory_dict)} people in directory")
print()
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses_list)}")
print(f"Current Academic Load: {workload} weekly commitments")
print(f"Entertainment Backlog: {len(Entertainment_backlog_set)} items")
print(f"Current Hobbies: {len(Hobbies_set)} activities")
print(f"================================================================")