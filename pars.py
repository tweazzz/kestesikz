import instaloader
import os
import schedule
import time

def job():
    def download_public_posts(usernames, n):
        try:
            loader = instaloader.Instaloader()

            for username in usernames:
                loader.context.username = 'gggg_gkkkkllll'

                profile = instaloader.Profile.from_username(loader.context, username)
                count = 0

                for post in profile.get_posts():
                    if count >= n:
                        break

                    post_directory = os.path.join(username, f"post_{post.date_utc.strftime('%Y%m%d_%H%M%S')}")
                    os.makedirs(post_directory, exist_ok=True)

                    current_directory = os.getcwd()

                    try:
                        os.chdir(post_directory)

                        loader.download_post(post, target='.')
                        
                        print(f"Downloaded image for post {count + 1} from {username}")
                        print(f"Post saved in: {post_directory}")
                        print("-" * 30)
                    finally:
                        os.chdir(current_directory)

                    count += 1
        except instaloader.exceptions.InstaloaderException as e:
            print("Ошибка:", e)

    account_list = ['lalalalisa_m']
    download_public_posts(account_list, n=2)


schedule.every().day.at("16:21").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)