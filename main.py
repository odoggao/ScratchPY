import os
import warnings
import database as db
import time  # <--- ADICIONADO para manter o script vivo
import scratchattach as sa
import encryption
from dotenv import load_dotenv
global user
load_dotenv()
warnings.filterwarnings('ignore', category=sa.LoginDataWarning)

# Log into your Scratch account
session = sa.login(os.getenv("SCRATCH"), os.getenv("PASSWORD"))
project = os.getenv("PROJECT_ID")

cloud = session.connect_cloud(project)
events = cloud.events()
@events.event
def on_set(event):
    if event.var == "console":
        command = encryption.decode(str(event.value)).split(" ")
        print(command)
        
        if command[2] == "db":
            if command[1] == "set":
                db.set_value(command[3],command[4],command[5],command[6])
            if command[1] == "get":
                cloud.set_var("returned",encryption.encode(str(db.get_value(command[3],command[4],command[5],command[6]))))
@events.event
def on_ready():
    print("Now listening to live Scratch cloud events...")

# Inicia o monitoramento em segundo plano
events.start()

# <--- ADICIONADO: Mantém o script principal rodando sem gastar processamento
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Desconectando...")
