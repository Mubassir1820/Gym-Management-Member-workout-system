# Gym-Management-Member-workout-system

A role-based Gym Management & Workout Assignment system built using Django + Django REST Framework, designed to manage multiple gym branches, users, workout plans, and workout tasks with strict business rules and permissions.

This project is API-only and uses JWT authentication.

To run the project:
1. git clone <repo_link>
2. Create an enviormental variable
3. Install dependencies <python install -r requirements.txt>

Hosted public url: https://gym-management-member-workout-system.onrender.com

Roles & Permissions explanation
Role	                        Permissions
Super Admin	        Create gym branches, view all data, bypass branch restrictions
Gym Manager	        Manage users (Trainer, Member) within own branch
Trainer	            Create workout plans, assign workout tasks
Member	            View & update own workout tasks

List of available endpoints
Login: https://gym-management-member-workout-system.onrender.com/api/auth/login/
Refresh token: https://gym-management-member-workout-system.onrender.com/api/auth/refresh/
Profile: https://gym-management-member-workout-system.onrender.com/api/auth/profile/
Gym branch create: https://gym-management-member-workout-system.onrender.com/api/gymbranches/
Gym branch list: https://gym-management-member-workout-system.onrender.com/api/gymbranches/
Trainer create: https://gym-management-member-workout-system.onrender.com/api/auth/manager/users/
Trainer list: https://gym-management-member-workout-system.onrender.com/api/auth/manager/users/list/
WorkoutPlan create: https://gym-management-member-workout-system.onrender.com/api/workout-plans/
WorkoutPlan list: https://gym-management-member-workout-system.onrender.com/api/workout-plans/
WorkoutTask assign: https://gym-management-member-workout-system.onrender.com/api/tasks/assign/
WorkoutTask list: https://gym-management-member-workout-system.onrender.com/api/tasks/trainer/
WorkoutTask update: https://gym-management-member-workout-system.onrender.com/api/tasks/member/{id}/

How to use the postman collection
1. Open postman
2. Drag the .json file directly into the Postman window
3. The collection appears in the left sidebar
4. For token, add authorization -> Authorization type: Bearer Token -> Add token
5. Add inputs json in body section
