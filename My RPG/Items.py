# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import random

# ===============================================================
# ====                   ITEMS DE DROPEO                     ====
# =============================================================== 

comun = {

"chatarra" : {"nombre": "Chatarra", "credits": 25},

"metal" : {"nombre": "Metal", "credits": 40},

"circuitos" : {"nombre": "Circuitos", "credits": 25},

"polimeros" : {"nombre": "Polimeros", "credits": 50},

}

infrecuente = {

    "aleacion de titaneo" : {"nombre": "Aleacion de Titaneo", "credits": 500, "descripcion": "Necesaria para la creacion de mejores herramientas"},

    "nucleo" : {"nombre": "Nucleo", "credits": 750, "descripcion": "Posee informacion util, prodria llevarte a una mina de terminales."},

    "aleacion de tungsteno" : {"nombre": "Aleacion de Tungsteno", "credits": 1000, "descripcion": "Un material muy versatil para la construccion de armas."}
}

epico = {

    "fuente de energia" : {"nombre": "Fuente de energia", "credits": 1300, "descripcion": "Valiosa debido a la cantidad de energia que posee, facilmente puede alimentar a 5 ciudades."},

    "terminales" : {"nombre": "Terminales", "credits": 2000, "descripcion": "Contienen informacion del viejo mundo, antes del caos tal vez puedan llevar a la gloria a la humanidad otra vez."}
}

singulares = {

    "modulo_1" : {
        "nombre": "modulo de velocidad",
        "credits": 0, 
        "descripcion": "Otrogado por la Cyber Snake, el portador obtendra una asombrosa velocidad de reaccion.",
        "stats" : {"vel": 25, "atk": 20, },
    },

    "modulo_2" : {
        "nombre": "nucleo de adaptacion",
        "credits": 0,
        "descripcion": "Otorgado por el Cyber Crocodile, este objeto otroga una gran cantidad de vitalidad",
        "stats": {"hp_max": 30, "def": 30,  }

    },

    "modulo_3" : {
        "nombre": "Modulo de combate",
        "credits": 0,
        "descripcion": "Otorgado por la IA automata, es un moculo especifico del combate",
        "stats": {"pc": 25, "crit": 15, "atk": 15}
    },

    "modulo_4" : {
        "nombre": "Modulo singular",
        "credits": 0,
        "descripcion": "Otrogado por la Ultimate IA, es improbable decifrarlo con la tecnologia actual.",
        "stats": {"pc": 15, "crit": 25, "atk": 15, "vel": 15, "def": 15, "hp_max": 15 }
    }
}

especiales = {

    "drop_snake" : {"nombre": "aleacion Inestable", "credits": 600, "descripcion": "Una aleacion muy inestable, altamente volatin no se recomienda su uso para personas comunes, otorgada por Cyber Snake"},

    "drop_croco" : {"nombre": "Aleacion Organica", "credits": 800, "descripcion": "Una aleacion escamosa, muy resistente y reflectante. Tal vez se pueda construir una traje con ella, es otorgada por el Cyber Crocodile." },

    "drop_ia" : {"nombre": "Terminales de IA", "credits": 2000, "descripcion": "Terminales tan importantes, poseen los planos de armas, trajes y del viejo mundo, es otorgada por IA's"},

    "drop_auto" : {"nombre": "Metal liquido", "credits": 3000, "descripcion": "Altamente valioso para fabricar armas y servotrajes, es otorgado por la IA Automata"},

    "drop_ulti" : {"nombre": "Aleacion Scarlet", "credits": 4000, "descripcion": "Altamente valioso. Se desconoce el uso del material, con la tecnologia actual es imposible de decifrar, otorgado por la Ultimate IA."},

    "chromebites" : {"nombre": "Chromebites", "descripcion": "La moneda del viejo mundo"}
}

# ===============================================================
# ====                   ITEMS DE TIENDA                     ====
# =============================================================== 

tienda = { 
    "nombre": "Botiquine", "precio": 20, "hp": 80, "max": 10,
    "nombre": "V-Deep", "precio": 300, "vel": 15, "max": 10,
    "nombre": "E-Deep", "precio": 300, "def": 15, "max": 10,
    "nombre": "A-Deep", "precio": 300, "atk": 15, "max": 10 ,
    "nombre": "Deep", "precio": 1000, "vel": 20, "def": 20, "atk": 20, "max": 5,
    "nombre": "Inside", "precio": 1500, "vel": 35, "def": 35, "atk": 35, "max": 3,
    "nombre": "Modulo de tactico", "precio": 2000, "atk": 30, "max": 1, 
    "nombre": "Nanobots", "precio": 200, "max": 10
    }

# ==================================================================
# ====                     LOOT DE COFRES                       ====
# ==================================================================

reli_1 = {"nombre": "Reliquea Comun", "PH": 1, "credits": 500, "descripcion": "Una reliquea comun no escasean, son muy abundantes."},
reli_2 = {"nombre": "Reliquea Infrecuente", "PH": 2, "credits": 1000, "descripcion": "Una reliquea algo rara de ver pero no escasean."}
reli_3 = {"nombre": "Reliquea Epica", "PH": 3, "credits": 1500, "descripcion": "Dificiles de encontrar debes tener mucha suerte."}
reli_4 = {"nombre": "Reliquea Especial", "PH": 4, "credits": 2000, "descripcion": "Son dificiles de encontrar, tanto que solo debe haber 10 por ciudad"}
reli_5 = {"nombre": "Reliquea Singular", "PH": 10, "credits": 3000, "descripcion": "No deberian existir, No deberian estar en las manos humanas, son articulos especiales de IA's"}
