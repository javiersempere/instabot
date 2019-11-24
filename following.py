#Crea un archivo con información sobre los seguidos

from instabot import Bot
import os
import sys
import re
import time

bot = Bot()
bot.login()

user_id = bot.user_id
sys.path.append(os.path.join(sys.path[0], "../"))

# print (user_id)

Seguidos = bot.following
seg = list(Seguidos)

#instagram acepta solo 99 de un tirón
prim=100
ult=198

seguidos = seg[prim:ult]

with open("following.txt", "a", encoding='utf-8') as f:
# a para añadir al archivo, w para crear nuevo archivo
    for usuario in seguidos:
        user_info = bot.get_user_info(usuario)
        linea = str(usuario)
        linea = linea+"\t"+user_info["username"]
        linea = linea+"\t"+user_info["full_name"]
        bio=user_info["biography"].encode("ascii", "replace")
        biografia = bio.decode(encoding="ascii", errors="replace")
    #    linea = linea+"\t"+re.sub(r"[^a-zA-Z0-9]+", ' ', biografia)
        linea = linea+"\t"+re.sub(r'\W+', ' ', biografia)
        # linea = linea+"\t"+biografia
        f.write(linea + "\n")
        print(linea)
        # ajustar el sleep impide que instagram de error?
        # time.sleep(2)
