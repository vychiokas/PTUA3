import os
from datetime import datetime
import pickle


# os.chdir('C:/Users/Vytautas/repositories/personal')
# print(os.getcwd())

# print(os.listdir())

# something = os.stat("main.py")
# something = os.stat("main.py").st_size
# print(os.stat("main.py").st_mtime)

# print(datetime.fromtimestamp(os.stat("main.py").st_mtime))


# with open("file.txt", 'w') as f:
#     f.write("Hello World!")


# f = open("file.txt", 'a')
# f.write("Hello World 123!")
# f.close()


# with open("file.txt", 'r+') as f:
#     f.write("Hello World 123!")
#     f.write("BYE!")


# with open("file.txt", 'r') as f:
#     print(f.read())



# with open("failas.txt", 'w', encoding="utf-8") as f:
#     f.write("Čia yra pirmas failo sakinys")
    
    
# with open("failas.txt", 'r', encoding="utf-8") as failas:
#     print(failas.read())

# with open("failas.txt", 'w', encoding="utf-8") as failas:
#     failas.write("Čia yra pirmas sakinys \n")

# with open("failas.txt", 'a', encoding="utf-8") as failas:
#     failas.write("Čia yra antras sakinys \n")


# with open("failas.txt", 'w', encoding="utf-8") as failas:
#     failas.write("Test")
#     failas.write("Test")
    

# with open("failas.txt", 'r+', encoding="utf-8") as failas:
#     failas.write("Test")
#     failas.seek(0)
#     failas.write("BE")


# with open("file.txt", 'r', encoding="utf-8") as failas:
#     print(failas.readlines())

# Čia yra pirmas sakinys
# Čia yra antras sakinys
# Čia yra trečias sakinys


# with open("file.txt", 'r', encoding="utf-8") as failas:
#     for line in failas:
#         print(line, end="")
        
        
# with open("file.txt", 'r', encoding="utf-8") as failas:
#     print(failas.readline(2))

# Čia yra pirmas sakinys
# Čia yra antras sakinys
# Čia yra trečias sakinys
# Čia yra ketvirtas sakinys

# print(failas.read(100))

# # Čia yra penktas sakinys
# # Čia yra šeštas sakinys
# # Čia yra septintas sakinys
# # Čia yra aštuntas sakinys

# print(failas.read(100))

# Čia yra devintas sakinys
# Čia yra dešimtas sakinys



# with open("file.txt", 'r', encoding="utf-8") as r_failas:
#     with open("file_copy.txt", 'w', encoding="utf-8") as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)


# with open("picture.jpg", 'r') as r_failas:
#     with open("picture_copy.jpg", 'w') as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)

# UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 65: character maps to <undefined>


# with open("picture.jpg", 'rb') as r_failas:
#     with open("picture_copy.jpg", 'wb') as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)


# import pickle

# a = 1024

# with open("a.pkl", "wb") as pickle_out:
#     pickle.dump(a, pickle_out)
    
# import pickle

# with open("a.pkl", "rb") as pickle_in:
#     naujas_a = pickle.load(pickle_in)

# print(naujas_a)

# 1024


# import pickle

# zodynas = {1:"Pirmas", 2:"Antras", 3:"Trečias"}

# with open("zodynas.pkl", "wb") as pickle_out:
#     pickle.dump(zodynas, pickle_out)
    
    
# import pickle

# with open("zodynas.pkl", "rb") as pickle_in:
#     naujas_zodynas = pickle.load(pickle_in)

# print(naujas_zodynas)

# {1: 'Pirmas', 2: 'Antras', 3: 'Trečias'}


# a = 10
# b = 7
# c = 23

# with open("abc.pkl", "wb") as pickle_out:
#     pickle.dump(a, pickle_out)
#     pickle.dump(b, pickle_out)
#     pickle.dump(c, pickle_out)

# # 10
# # 7
# # 23

# import pickle

# with open("abc.pkl", "rb") as pickle_in:
#     while True:
#         try:
#             print(pickle.load(pickle_in))
#         except EOFError:
#             break



# 10
# 7
# 23



# import pickle

# while True:
#     veiksmas = int(input("Pasirinkite veiksmą: 1 - peržiūrėti, 2 - įrašyti, 3 - išeiti"))
#     if veiksmas == 1:
#         try:
#             with open("zmones.pkl", 'rb') as failas:
#                 print(pickle.load(failas))
#         except:
#             print("Nėra tokio failo")
#             with open("zmones.pkl", 'wb') as failas:
#                 zmones = []
#                 pickle.dump(zmones, failas)
#     if veiksmas == 2:
#         with open("zmones.pkl", 'rb') as failas:
#             zmones = pickle.load(failas)
#             vardas = input("Įveskite naują vardą")
#             with open("zmones.pkl", 'wb') as failas:
#                 zmones.append(vardas)
#                 pickle.dump(zmones, failas)
#     if veiksmas == 3:
#         print("Programa baigta")
#         break


import pickle

class Automobilis:
    def __init__(self, marke, modelis):
        self.marke = marke
        self.modelis = modelis
    def drive(self):
        print("WROOM")

automobiliai = [Automobilis("Toyota", "Avensis"), Automobilis("Toyota", "Corolla"), Automobilis("Toyota", "Camry")]

with open("automobilis.pkl", "wb") as failas:
    pickle.dump(automobiliai, failas)

with open("automobilis.pkl", "rb") as failas:
    automobiliai = pickle.load(failas)
    for automobilis in automobiliai:
        print("Markė", automobilis.marke)
        print("Modelis", automobilis.modelis)
        automobilis.drive()



