#Crea un archivo con información sobre los seguidos
#a partir del archivo following0.txt

from instabot import Bot
import os
import sys
import re
import time

bot = Bot()
bot.login()

user_id = bot.user_id
sys.path.append(os.path.join(sys.path[0], "../"))

# la lista following0 se genera con following0.py
seg = bot.read_list_from_file("following0.txt")

#instagram acepta solo 99 por hora?
prim=199
ult=300

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
        # linea = linea+"\t"+re.sub(r"[^a-zA-Z0-9]+", ' ', biografia)
        linea = linea+"\t"+re.sub(r'\W+', ' ', biografia)
        # linea = linea+"\t"+biografia
        f.write(linea + "\n")
        print(linea)
