#unfollow non followers

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

bot = Bot()
bot.login()

bot.unfollow_non_followers(n_to_unfollows=10)
