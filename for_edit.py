import os
import time
import random
from instabot import Bot
from celeb_list import celebs  # Import the list of celebrities
from termcolor import colored

# Remove default config to prevent issues with the library
if os.path.exists("config"):
    os.rmdir("config")

# Initialize the bot
bot = Bot()

def print_logo():
    logo = """
    MM"""""`MM                   dP dP                     
    MM  .mmm. `MM  .d8888b. .d8888b. 88 88 .d8888b. dP .d8888b.
    MM  MMMMM  MM  88ooood8 88ooood8 88 88 88'  `88 88 88'  `88
    MM  MMMMM  MM  88.  ... 88.  ... 88 88 88.  .88 88 88.  .88
    MM  `MMM'  MM  `88888P' `88888P' dP dP `88888P8 dP `88888P'
    """
    print(colored(logo, 'yellow'))

def display_menu():
    print_logo()
    print(colored("[v1.0] coded by cyber kallan (arjun arz)", 'red'))
    print(colored("[01] Unfollow Tracker", 'red'))
    print(colored("[02] Increase Followers", 'yellow'))
    print(colored("[03] Download Stories", 'red'))
    print(colored("[04] Download Saved Content", 'yellow'))
    print(colored("[05] Download Following List", 'red'))
    print(colored("[06] Download Followers List", 'yellow'))
    print(colored("[07] Download Profile Info", 'red'))
    print(colored("[08] Activate Unfollower", 'yellow'))

def login():
    username = input(colored("Username: ", 'yellow'))
    password = input(colored("Password: ", 'yellow'))
    print(colored(f"[*] Trying to login as {username}", 'yellow'))
    bot.login(username=username, password=password)
    print(colored("[+] Login Successful", 'green'))

def follow_unfollow_celebs(celebs):
    for index, celeb in enumerate(celebs):
        print(colored(f"Trying to follow celebgram {celeb} ...", 'yellow'), end="")
        bot.follow(celeb)
        time.sleep(random.uniform(2, 5))  # Random delay between 2 to 5 seconds
        print(colored("OK", 'green'))
        print(colored(f"Trying to unfollow celebgram {celeb} ...", 'yellow'), end="")
        bot.unfollow(celeb)
        print(colored("OK", 'green'))
        time.sleep(random.uniform(2, 5))  # Random delay between 2 to 5 seconds

        if (index + 1) % 10 == 0:  # Every 10 operations
            print(colored("Taking a short break to avoid detection...", 'red'))
            time.sleep(random.uniform(60, 120))  # Timeout between 1 to 2 minutes

def track_unfollowers():
    followers = bot.get_user_followers(bot.user_id)
    followings = bot.get_user_following(bot.user_id)
    unfollowers = [user for user in followings if user not in followers]
    print(colored("Unfollowers: ", 'yellow'), unfollowers)

def unfollow_all():
    bot.unfollow_everyone()

def unfollow_non_verified():
    followings = bot.get_user_following(bot.user_id)
    for user_id in followings:
        if not bot.get_user_info(user_id).get('is_verified'):
            bot.unfollow(user_id)

def download_profile_data(target_username):
    bot.download_profile(target_username, profile_pic=True)
    bot.download_stories(user_ids=[bot.get_user_id_from_username(target_username)])
    bot.download_saved_content()
    bot.save_followers_list(target_username)
    bot.save_following_list(target_username)

def main():
    login()
    while True:
        display_menu()
        choice = input(colored("\n[::] Choose an option: ", 'yellow'))

        if choice == '1':
            track_unfollowers()
        elif choice == '2':
            follow_unfollow_celebs(celebs)
        elif choice == '3':
            target_username = input(colored("Enter the username to download stories: ", 'yellow'))
            bot.download_stories(user_ids=[bot.get_user_id_from_username(target_username)])
        elif choice == '4':
            bot.download_saved_content()
        elif choice == '5':
            target_username = input(colored("Enter the username to download following list: ", 'yellow'))
            bot.save_following_list(target_username)
        elif choice == '6':
            target_username = input(colored("Enter the username to download followers list: ", 'yellow'))
            bot.save_followers_list(target_username)
        elif choice == '7':
            target_username = input(colored("Enter the username to download profile info: ", 'yellow'))
            download_profile_data(target_username)
        elif choice == '8':
            unfollow_non_verified()
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

        cont = input(colored("Do you want to perform another operation? (y/n): ", 'yellow'))
        if cont.lower() != 'y':
            break

    print(colored("Task completed successfully!", 'green'))

if __name__ == "__main__":
    main()

