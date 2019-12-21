# Hace like en lista de seguidores y seguidos

import argparse
import sys
import random
from instabot import Bot

bot = Bot()
bot.login()

usuario = bot.username
print("Vamos a hacer like a los amigos de", usuario)

seguidos = bot.get_user_following(usuario)
seguidores = bot.get_user_followers(usuario)
seguidores1 = set(seguidores) - set(seguidos)

lista = list(seguidos)
lista.extend(list(seguidores1))
random.shuffle(lista)

print("total: ", len(lista))

for user_id in lista:
      user_info = bot.get_user_info(user_id)
      print(user_info["username"],"-",user_info["full_name"])
      bot.like_user(user_id, amount=2, filtration=False)
