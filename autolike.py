# Hace like en lista de seguidores y seguidos

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

bot = Bot()
bot.login()

# bot.like_followers("sempere.javier", nlikes=2)
# bot.like_following("sempere.javier", nlikes=2)

# bot.like_followers(bot.username, nlikes=2)
# bot.like_following(bot.username, nlikes=2)

usuario = bot.username
print("Vamos a hacer like a los amigos de", usuario)

# print("followers: ", len(list(bot.get_user_followers(usuario))))
# print("following: ", len(list(bot.get_user_following(usuario))))

seguidores = bot.get_user_followers(usuario)
print("followers: ", len(list(seguidores)))

seguidos = bot.get_user_following(usuario)
print("following: ", len(list(seguidos)))

for user_id in seguidores:
     user_info = bot.get_user_info(user_id)
     print(user_info["username"])
     print(user_info["full_name"])
     bot.like_user(user_id, amount=2, filtration=False)

for user_id in seguidos:
      user_info = bot.get_user_info(user_id)
      print(user_info["username"])
      print(user_info["full_name"])
      bot.like_user(user_id, amount=2, filtration=False)
