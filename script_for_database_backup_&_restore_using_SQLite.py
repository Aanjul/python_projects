# For refrence https://medium.com/@estebanpiero/10-useful-python-scripts-for-everyday-tasks-b0d74f2ea62c

import sqlite3
import shutil

# Database file paths
source_db_file = 'source.db'
backup_db_file = 'backup.db'

# Function to create a backup of the SQLite database
def backup_database():
try:
	shutil.copy2(source_db_file, backup_db_file)
	print("Backup successful.")
	except Exception as e:
	print(f"Backup failed: {str(e)}")
# Function to restore the SQLite database from a backup
def restore_database():
try:
	shutil.copy2(backup_db_file, source_db_file)
	print("Restore successful.")
	except Exception as e:
	print(f"Restore failed: {str(e)}")
# Usage
while True:
	print("Options:")
	print("1. Backup Database")
	print("2. Restore Database")
	print("3. Quit")
	choice = input("Enter your choice (1/2/3): ")

	if choice == '1':
		backup_database()
	elif choice == '2':
		restore_database()
	elif choice == '3':
		break
	else:
	print("Invalid choice. Please enter 1,2, or 3.")