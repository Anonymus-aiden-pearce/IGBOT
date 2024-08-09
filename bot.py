import os
import time
import random
from instabot import Bot
from celeb_list import celebs  # Import the list of celebrities

# Remove default config to prevent issues with the library
if os.path.exists("config"):
    os.rmdir("config")

# Initialize the bot
bot = Bot()

# Login to Instagram
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
bot.login(username=username, password=password)

# Function to follow/unfollow celebrities with timeouts and random intervals
def follow_unfollow_celebs(celebs):
    for index, celeb in enumerate(celebs):
        bot.follow(celeb)
        time.sleep(random.uniform(2, 5))  # Random delay between 2 to 5 seconds
        bot.unfollow(celeb)
        time.sleep(random.uniform(2, 5))  # Random delay between 2 to 5 seconds

        if (index + 1) % 10 == 0:  # Every 10 operations
            print("Taking a short break to avoid detection...")
            time.sleep(random.uniform(60, 120))  # Timeout between 1 to 2 minutes

# Function to track unfollowers
def track_unfollowers():
    followers = bot.get_user_followers(bot.user_id)
    followings = bot.get_user_following(bot.user_id)
    unfollowers = [user for user in followings if user not in followers]
    print("Unfollowers: ", unfollowers)

# Function to unfollow all users
def unfollow_all():
    bot.unfollow_everyone()

# Function to unfollow non-verified accounts
def unfollow_non_verified():
    followings = bot.get_user_following(bot.user_id)
    for user_id in followings:
        if not bot.get_user_info(user_id).get('is_verified'):
            bot.unfollow(user_id)

# Function to download profile info, stories, saved content, following/followers list
def download_profile_data(target_username):
    bot.download_profile(target_username, profile_pic=True)
    bot.download_stories(user_ids=[bot.get_user_id_from_username(target_username)])
    bot.download_saved_content()
    bot.save_followers_list(target_username)
    bot.save_following_list(target_username)

# Main function to provide options
def main():
    print("\nChoose an option:")
    print("1. Follow/Unfollow Celebrities")
    print("2. Track Unfollowers")
    print("3. Unfollow All Users")
    print("4. Unfollow Non-Verified Accounts")
    print("5. Download Profile Data")
    choice = input("\nEnter your choice: ")

    if choice == '1':
        follow_unfollow_celebs(celebs)
    elif choice == '2':
        track_unfollowers()
    elif choice == '3':
        unfollow_all()
    elif choice == '4':
        unfollow_non_verified()
    elif choice == '5':
        target_username = input("Enter the username to download profile data: ")
        download_profile_data(target_username)
    else:
        print("Invalid choice. Please try again.")

    print("Task completed successfully!")

if __name__ == "__main__":
    main()
