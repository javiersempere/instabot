#unfollow from unfollow file

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

bot = Bot()
bot.login()

unfollowing = bot.read_list_from_file("unfollow.txt")

for user_id in unfollowing:
    usuario = bot.get_username_from_user_id(user_id)
    print(usuario)
    bot.unfollow(usuario)
