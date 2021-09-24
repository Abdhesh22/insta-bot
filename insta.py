from instabot import Bot
import os
import glob
import random
from tqdm.std import tqdm

time = random.randint(120, 150)
print(time)

bot = Bot(filter_private_users=True,filter_business_accounts=True, filter_previously_followed=True,filter_verified_accounts=True,follow_delay=time,max_follows_per_day=50)

password_file=open("password.txt","r")
password1 = password_file.read()
bot.login(username="sharma_siya28", password=password1)

userList=["mahi7781","rohitsharma45","dishapatani","rashmika_mandanna","sidmalhotra","norafatehi","raashiikhanna","deepikapadukone","aliaabhatt","thedeverakonda","virat.kohli"]

for user in userList:
    medias = bot.get_user_medias(user,filtration=True)
    post1 = medias[0]
    post2 = medias[1]
    post3 = medias[2]

    likers = bot.get_media_likers(post1)
    cnt =0
    for liker in tqdm(likers):
        if cnt<10:
            print(bot.get_username_from_user_id(liker))
            bot.follow(liker)
            cnt +=1


    likers = bot.get_media_likers(post2)
    cnt =0
    for liker in tqdm(likers):
        if cnt<10:
            print(bot.get_username_from_user_id(liker))
            bot.follow(liker)
            cnt +=1

    likers = bot.get_media_likers(post3)
    cnt =0
    for liker in tqdm(likers):
        if cnt<10:
            print(bot.get_username_from_user_id(liker))
            bot.follow(liker)
            cnt +=1