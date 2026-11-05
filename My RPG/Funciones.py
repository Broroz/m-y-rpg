# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import random

# ======================================================================
# ====                   SISTEMA DE ENEMIGOS                        ====
# ======================================================================  
 
def inicio_combate(combate_actual): 
    enemigos_combate = []
    
    for enemigo in combate_actual:
        enemigo_actual = enemigo.copy()
        enemigos_combate.append(enemigo_actual)
        
    return enemigos_combate

# =====================================================================
# ====                     SISTEMA DE CICLOS                       ====
# =====================================================================

periodos = ("Mañana", "Tarde", "Noche", "Madrugada")

periodo_actual = periodos[0]

# =====================================================================
# ====                   SISTEMA DE NIVELES                        ====
# =====================================================================

def subir_nivel(jugador):
    while jugador["exp"] >= jugador["exp_necesaria"]:
        jugador["lv"] += 1
        jugador["exp"] -= jugador["exp_necesaria"]
        jugador["exp_necesaria"] += 75
        jugador["hp"] += 10
        jugador["hp_max"] += 10
        jugador["atk"] += 5
        jugador["vel"] += 5

    return jugador


def generar_nivel_enemigo(lv, categoria):
    if categoria == "enemigos":
        lv_min = lv
        lv_max = lv + 2
    elif categoria == "enemigos_p":
        lv_min = lv + 1
        lv_max = lv + 3
    elif categoria == "bosses":
        lv_min = lv + 3
        lv_max = lv + 6

    return random.randint(lv_min, lv_max)

def generar_enemigos(combate_actual, lv, categoria):
    for enemigo in combate_actual:
        enemigo["lv"] = generar_nivel_enemigo(lv, categoria)
        nivel_extra = enemigo["lv"] - lv
        enemigo["hp"] += enemigo["hp"] * (0.15 * nivel_extra)
        enemigo["atk"] += enemigo["atk"] * (0.2 * nivel_extra)
        enemigo["def"] += enemigo["def"] * (0.1 * nivel_extra)
        enemigo["vel"] += enemigo["vel"] * (0.2 * nivel_extra)
        enemigo["exp"] += enemigo["exp"] * (0.1 * nivel_extra)
        enemigo["ammo"] += enemigo["ammo"] * (3 * nivel_extra)

    return combate_actual

def new_func(enemigo, nivel_extra):
    enemigo["drop"] += enemigo["lv"] + (2 * nivel_extra)

# ===================================================================================
# ====                   SISTEMA DE ATK, DEF, VEL Y HP MAX                       ====
# ===================================================================================

def obtener_atk(jugador, ataques, armas_equipadas, trajes, servotrajes, modulos):
    atk_total = jugador.get("atk", 0)

    for equipo in (armas_equipadas, trajes, servotrajes, modulos):
        if isinstance(equipo, dict):
            atk_total += equipo.get("atk", 0)
        elif isinstance(equipo, (list, tuple)):
            for item in equipo:
                if isinstance(item, dict):
                    atk_total += item.get("atk", 0)
            if isinstance(ataques, dict):
                atk_total += ataques.get("atk", 0)

    return atk_total


def obtener_def(jugador, armas_equipadas, trajes, servotrajes,modulos):
    def_total = jugador.get("def", 0)

    for equipo in (armas_equipadas, trajes, servotrajes, modulos):
        if isinstance(equipo, dict):
            def_total +=equipo.get("def", 0)
        elif isinstance(equipo, (list, tuple)):
            for item in equipo:
                if isinstance(item, dict):
                    def_total += item.get("def", 0)

    return def_total

def obtener_vel(jugador, trajes, servotrajes, modulos):
    vel_total = jugador.get("vel", 0)

    for equipo in (trajes, servotrajes, modulos):
        if isinstance(equipo, dict):
            vel_total += equipo.get("vel", 0)
        elif isinstance(equipo, (list, tuple)):
            for item in equipo:
                if isinstance(item, dict):
                    vel_total += item.get("vel", 0)

    return vel_total

def obtener_hp_max(jugador, trajes, servotrajes, modulos):
    hp_max_total = jugador.get("hp_max", 0)

    for equipo in (trajes, servotrajes, modulos):
        if isinstance(equipo, dict):
            hp_max_total +=equipo.get("hp_max", 0)
        elif isinstance (equipo, (list, tuple)):
            for item in equipo:
                if isinstance(item, dict):
                    hp_max_total += item.get("hp-max", 0)

    return hp_max_total
