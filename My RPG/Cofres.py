# ===============================================================
# ====                     LOOT COFRES                       ====
# ===============================================================

import random

import Items

cofres_z = {
    "zona_1": {
        "cantidad": 4,
        "recompensas": ["reli_1", "reli_2"],
    },
    "zona_2": {
        "cantidad": 4,
        "recompensas": ["reli_1", "reli_2", "reli_3"],
    },
    "boss_1": {
        "cantidad": 3,
        "recompensas": ["reli_2", "reli_3", "reli_4"],
    },
    "boss_2": {
        "cantidad": 3,
        "recompensas": ["reli_2", "reli_3", "reli_4"],
    },
    "boss_3": {
        "cantidad": 3,
        "recompensas": ["reli_4", "reli_5"],
    },
    "boss_4": {
        "cantidad": 3,
        "recompensas": ["reli_4", "reli_5"],
    },
}

# ======================================================================
# ====                     APERTURA DE COFRES                       ====
# ======================================================================

abrir = {zona: set() for zona in cofres_z}
zona_actual = None


def entrar_zona(zona):
    global zona_actual

    if zona not in cofres_z:
        raise ValueError(f"No hay cofres configurados para la zona {zona!r}.")

    abrir[zona].clear()
    zona_actual = zona


def abrir_cofre(zona, numero, jugador):
    if zona != zona_actual:
        raise RuntimeError("Debes entrar en la zona antes de abrir sus cofres.")
    if not isinstance(numero, int) or not 1 <= numero <= cofres_z[zona]["cantidad"]:
        raise ValueError(f"El cofre debe ser un número entre 1 y {cofres_z[zona]['cantidad']}.")
    if numero in abrir[zona]:
        print(f"El cofre {numero} ya está vacío.")
        return None

    recompensa = random.choice(cofres_z[zona]["recompensas"])
    item = getattr(Items, recompensa)
    if isinstance(item, tuple):
        item = item[0]

    jugador["inventario"].append(recompensa)
    abrir[zona].add(numero)
    print(f"El cofre {numero} contenía: {item['nombre']}.")
    return recompensa


def explorar_cofres(zona, jugador):
    while len(abrir[zona]) < cofres_z[zona]["cantidad"]:
        disponibles = [
            numero
            for numero in range(1, cofres_z[zona]["cantidad"] + 1)
            if numero not in abrir[zona]
        ]
        print(f"Cofres disponibles: {', '.join(map(str, disponibles))}. Escribe 0 para salir.")
        seleccion = input("¿Qué cofre quieres abrir? ").strip()

        if seleccion == "0":
            break
        if not seleccion.isdigit() or int(seleccion) not in disponibles:
            print("Selecciona un cofre disponible.")
            continue

        abrir_cofre(zona, int(seleccion), jugador)


def salir_zona(zona):
    global zona_actual

    if zona != zona_actual:
        raise RuntimeError("La zona que intentas abandonar no está activa.")

    abrir[zona].clear()
    zona_actual = None

