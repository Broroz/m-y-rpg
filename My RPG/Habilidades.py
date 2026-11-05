arbol_1 = {
    "nombre": "Soporte Charly", 
    "hp_max":{
    "hp_max_1": 5, "costo": 2,
    "hp_max_2": 5, "costo": 4,
    "hp_max_3": 5, "costo": 6,
    "hp_max_4": 5, "costo": 8
    },
    "def":{
    "def_1": 5, "costo": 2,
   "def_2": 5, "costo": 4,
    "def_3": 5, "costo": 6,
    "def_4": 5, "costo": 8
    }
    }

arbol_2 = {
    "nombre": "Soporte Bravo",
    "atk":{
        "atk_1": 5, "costo": 6,
        "atk_2": 5, "costo": 8,
        "atk_3": 5, "costo": 10,
        "atk_4": 5, "costo": 12
    },
    "vel":{
        "vel_1": 5, "costo": 6,
        "vel_2": 5, "costo": 8,
        "vel_3": 5, "costo": 10,
        "vel_4": 5, "costo": 12
    },
    "pc":{
        "pc_1": 5, "costo": 6,
        "pc_2": 5, "costo": 8,
        "pc_3": 5, "costo": 10,
        "pc_4": 5, "costo": 12
    }
    }

arbol_3 = {   
    "hp_max":{
        "hp_max_1": 5, "costo": 2,
        "hp_max_2": 5, "costo": 4,
        "hp_max_3": 5, "costo": 6,
        "hp_max_4": 5, "costo": 8
    },
    "def":{
       "def_1": 5, "costo": 2,
       "def_2": 5, "costo": 4,
        "def_3": 5, "costo": 6,
        "def_4": 5, "costo": 8
    },
    "atk":{
        "atk_1": 5, "costo": 6,
        "atk_2": 5, "costo": 8,
        "atk_3": 5, "costo": 10,
        "atk_4": 5, "costo": 12
    },
    "vel":{
        "vel_1": 5, "costo": 6,
        "vel_2": 5, "costo": 8,
        "vel_3": 5, "costo": 10,
        "vel_4": 5, "costo": 12
    },
    "pc":{
        "pc_1": 5, "costo": 6,
        "pc_2": 5, "costo": 8,
        "pc_3": 5, "costo": 10,
        "pc_4": 5, "costo": 12
    },
    "crit":{
        "crit_1": 1, "costo": 8,
        "crit_2": 2, "costo": 10,
        "crit_3": 3, "costo": 12
    }
    }

soporte_IA = {
    "arbol_1": arbol_1,
    "arbol_2": arbol_2,
    "arbol_3": arbol_3,
}
habilidades = soporte_IA

# ==================================================================================
# ====                   SISTEMA DE ARBOL DE HABILIDADES                        ====
# ==================================================================================


def desbloquear_habilidad(jugador, rama, habilidad):
    datos = habilidades[rama][habilidad]

    if habilidad in jugador["habilidades"]:
        print("Ya tienes esta habilidad.")
        return False

    if jugador["puntos_habilidad"] < datos["costo"]:
        print("No tienes suficientes puntos.")
        return False

    for requisito in datos["requisitos"]:
        if requisito not in jugador["habilidades"]:
            print("No cumples los requisitos.")
            return False

    jugador["puntos_habilidad"] -= datos["costo"]
    jugador["habilidades"].append(habilidad)

    print(f"¡Has desbloqueado {datos['nombre']}!")
    return True