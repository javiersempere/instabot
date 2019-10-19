# hace like y follow a la gente a la que mi whitelist hace follow

import random
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

bot = Bot()
bot.login()

lista = []
mis_seguidos = bot.read_list_from_file("whitelist.txt")
# print (Seguidos)

skipped = bot.skipped_file
followed = bot.followed_file
unfollowed = bot.unfollowed_file

# print("skipped:", skipped.set)

# añade los seguidos de mis seguidos en la lista
for user_id in mis_seguidos:
    Seguidos2 = bot.get_user_followers(user_id, 15)
    seguidos2 = list(Seguidos2)
    lista.extend(seguidos2)

# ordena y baraja la lista
lista1 = list(set(lista) - skipped.set - followed.set - unfollowed.set)#
random.shuffle(lista1)

print("La lista tiene: ", len(lista1), " usuarios") 

# print ("longitud de lista", len(lista))
# print ("longitud de lista1", len(lista1))

# hace follow y like a 30 usuarios de lista1
n = 1
t = 1
while n < 30:
    print("usuario",n)
    usuario = lista1[t]
    t += 1
    if bot.follow(usuario):
        print ("usuario ",usuario, "seguido")
        n += 1
        # bot.like_user(usuario, amount=2, filtration=False)
