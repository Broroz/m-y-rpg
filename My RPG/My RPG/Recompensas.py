# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import random
import Enemigos
import Items

drop_boss = {boss["name"]: boss for boss in Enemigos.bosses}

# ====================================================================
# ====                     FUNCION DE LOOT                        ====
# ====================================================================

def generar_drop(l_comun, l_infrecuente, l_epico):
    comunes = random.choices(
        list(Items.comun.keys()),
        k=random.randint(*l_comun)
    )

    infrecuentes = random.choices(
        list(Items.infrecuente.keys()),
        k=random.randint(*l_infrecuente)
    )

    epicos = random.choices(
        list(Items.epico.keys()),
        k=random.randint(*l_epico)
    )

    return comunes + infrecuentes + epicos

# =================================================================
# ====                     LOOT ENEMIGOS                       ====
# =================================================================

def generar_drop_normal():
    return generar_drop(
        (3, 6),
        (1, 3),
        (0, 0)
    )


def generar_drop_p():
    return generar_drop(
        (1, 9),
        (1, 3),
        (0, 1)
    )


def generar_drop_b():
    return generar_drop(
        (1, 10),
        (3, 5),
        (1, 2)
    )

# ===============================================================
# ====                     LOOT BOSSES                       ====
# ===============================================================

# A decir verdad no entinedo del todo isinstance pero parece ser que toma un dic y lo desenpaqueta para que tome las tuplas() y esto sirve para que el comando tome las cantidades y los pueda imprimir 

def generar_drop_e(nombre_boss):
    if isinstance(nombre_boss, dict):
        recompensa = drop_boss.get(nombre_boss.get("name"))
    else:
        recompensa = drop_boss.get(nombre_boss)

    if recompensa is None:
        print("no hay recompensa por este boss")
        return {}

    drops = {}

    for item, cantidades in recompensa["drop_u"].items():
        cantidad = random.randint(*cantidades)
        drops[item] = cantidad

    for item, cantidades in recompensa["drop_e"].items():
        cantidad = random.randint(*cantidades)
        drops[item] = cantidad

    return drops

# =========================================================================
# ====                     LOOT EXCLUSIVO BOSSES                       ====
# =========================================================================

def entregar_singular(jugador, singular):

    if singular in jugador["Objetos obtenidos"]:
        return False

    jugador ["inventario"].append(singular)
    jugador ["singular_obtenido"].append(singular)
    print(f"Haz conseguido {Items.singulares[singular]['nombre']}!!!")

    return True