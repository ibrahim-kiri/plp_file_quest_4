import os
import sys

class FileAdventurer:
    @staticmethod
    def create_adventure_log():
        # Create an initial adventure log file for the user
        default_log = """My Coding Adventure Log
        Welcome, brave coder! This is your personal adventure log.
        Write about your coding journey, dreams, and achievements.

        Remember:
        - Every great programmer started exactly where you are now
        - Mistakes are just learning opportunities
        - Keep exploring and having fun!

        Date Started: Today is the beginning of something awesome!
        """
        try:
            with open('adventure_log.txt', 'w', encoding='utf-8') as log_file:
                log_file.write(default_log)
            print("Adventure log created successfully!")
            print("Check 'adventure_log.txt' to see your new log!")
        except Exception as e:
            print(f"Oops! Couldn't create log: {e}")

    @staticmethod
    def read_adventure_log():
        """
        Read and display the contents of the adventure log.
        """
        try:
            with open('adventure_log.txt', 'r', encoding='utf-8') as log_file:
                content = log_file.read()
                print("\nHere's your adventure log:")
                print("-" * 40)
                print(content)
                print("-" * 40)
        except FileNotFoundError:
            print("Adventure log not found! Let's create one first.")
            FileAdventurer.create_adventure_log()
        except Exception as e:
            print(f"Error reading log: {e}")

    @staticmethod
    def add_log_entry():
        """
        Add a new entry to the adventure log.
        """
        try:
            # Ensure the log exists
            if not os.path.exists('adventure_log.txt'):
                FileAdventurer.create_adventure_log()

            # Prompt for new entry
            print("\nAdd a new log entry!")
            entry = input("What exciting thing happened in your coding journey today? \n> ")

            # Append to existing log
            with open('adventure_log.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(f"\n\nNew Entry:\n{entry}")

            print("Entry added successfully!")
        except Exception as e:
            print(f"Couldn't add entry: {e}")

    @staticmethod
    def decode_secret_message():
        """
        A fun file handling mini-game to decode a secret message.
        """
        secret_message = """
        Secret Coding Challenge!

        I'll create a secret message file,
        and you'll decode it by reading the file!
        """

        try:
            # Create a secret message file
            with open('secret_mission.txt', 'w', encoding='utf-8') as secret_file:
                secret_file.write(secret_message)

            # Read and decode
            with open('secret_mission.txt', 'r', encoding='utf-8') as secret_file:
                decoded = secret_file.read()
                print("\nSecret Message Decoded:")
                print("-" * 30)
                print(decoded)
                print("-" * 30)
        except Exception as e:
            print(f"Mission failed: {e}")

def main_menu():
    """
    Interactive menu for file handling adventures!
    """
    while True:
        print("\nBeginner's File Handling Adventure")
        print("Choose your mission:")
        print("1. Create Adventure Log")
        print("2. Read Adventure Log")
        print("3. Add Log Entry")
        print("4. Decode Secret Message")
        print("5. End Adventure")

        choice = input("\nEnter your choice (1-5): ")

        # Dictionary mapping choices to functions
        missions = {
            '1': FileAdventurer.create_adventure_log,
            '2': FileAdventurer.read_adventure_log,
            '3': FileAdventurer.add_log_entry,
            '4': FileAdventurer.decode_secret_message,
        }

        # Execute chosen mission
        if choice in missions:
            missions[choice]()
        elif choice == '5':
            print("Thanks for your coding adventure! Goodbye!")
            break
        else:
            print("Invalid mission. Try again!")

def main():
    """
    Main function to start the file handling adventure.
    """
    print("Welcome to the coding Adventure!")
    print("Let's explore the world of file handling together!")

    main_menu()

# Magical line that starts the adventure
if __name__ == "__main__":
    main()