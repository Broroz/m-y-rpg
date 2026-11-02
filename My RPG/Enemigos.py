#                                                                           #####           #####
#                                                                           #====  ENEMIGOS ====#
#                                                                           #####           #####

perro_de_asalto ={
    "name" : ("Perro de asalto"),
    "hp" : 80,
    "atk" : 15,
    "def" : 20,
    "vel" : 22,
    "ammo" : 200,
    "exp" : 25
    }

Dron_defectuosos = {
    "name" : ("Dron defectuoso"),
    "hp" : 100,
    "atk" : 20,
    "def" : 15,
    "vel" : 30,
    "ammo" : 200,
    "exp" : 25
}

Automata = {
    "name" : ("Automata"),
    "hp" : 150,
    "atk" : 30,
    "def" : 20,
    "vel" : 25,
    "ammo" : 0,
    "exp" : 30
    }

automata_sirvienta = {
    "name" : ("automata sirvienta"),
    "hp" : 175,
    "atk" : 40,
    "def" : 30,
    "vel" : 25,
    "ammo" : 0,
    "exp" : 35
    }

enemigos = [perro_de_asalto, Dron_defectuosos, Automata, automata_sirvienta]
peso_n = [35, 25, 20, 20]

#                                                                           #####                   #####
#                                                                           #====  ENEMIGOS PESADOS ====#
#                                                                           #####                   #####

recolector_de_info = {
    "name" : ("Recolector de informacion"),
    "hp" : 125,
    "atk" : 45,
    "def" : 25,
    "vel" : 30,
    "ammo" : 200,
    "exp" : 45
}

cazarecompensa = {
    "name" : ("Caza recompensas"),
    "hp" : 150,
    "atk" : 50,
    "def" : 30,
    "vel" : 35,
    "ammo" : 200,
    "exp" : 45
}

escorpion_cibernetico = {
    "name" : ("Escorpion cibernetico"),
    "hp" : 200,
    "atk" : 50,
    "def" : 50,
    "vel" : 15,
    "ammo" : 0,
    "exp" : 50
}

perro_cañon = {
    "name" : ("Perro cañon"),
    "hp" : 250,
    "atk" : 60,
    "def" : 20,
    "vel" : 20,
    "ammo" : 200,
    "exp" : 50
}

enemigos_p = [recolector_de_info, cazarecompensa, escorpion_cibernetico, perro_cañon]

peso_p = [35, 25, 20, 20]

#                                                                                   #####           #####
#                                                                                   #====  BOSSES   ====#
#                                                                                   #####           #####

cyber_snake = {
    "name" : ("Cyber Snake"),
    "hp" : 750,
    "atk" : 105,
    "def" : 40,
    "vel" : 50,
    "ammo" : 1000,
    "exp" : 500
}

cyber_crocodile = {
    "name" : ("Cyber Crocodile"),
    "hp" : 1500,
    "atk" : 150,
    "def" : 50,
    "vel" : 40,
    "ammo" : 1000,
    "exp" : 1500
}

ia_automata = {
    "name" : ("IA Automata"),
    "hp" : 2500,
    "atk" : 200,
    "def" : 100,
    "vel" : 60,
    "ammo" : 1000,
    "exp" : 2500
}

ultimate_ia = {
    "name" : ("Ultimate IA"),
    "hp" : 5000,
    "atk" : 300,
    "def" : 150,
    "vel" : 100,
    "ammo" : 1000,
    "exp" : 5000
}

bosses = [cyber_snake, cyber_crocodile, ia_automata, ultimate_ia]