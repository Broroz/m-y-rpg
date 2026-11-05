# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import Funciones

periodos = Funciones.periodos
periodo_actual = Funciones.periodo_actual

# ==========================================================
# ====                     ESTADOS                       ===
# ==========================================================

huesos = {"nombre": "Huesos Rotos", "efecto": 0.3, "activo": False, "antidoto": "Nanobots"}

agotamiento = {
    "nombre": "Agotamiento",
    "efecto": 0.0,
    "incremento": 0.20,
    "activo": False,
    "antidoto": "Descansar",
}

desangrado = {
    "nombre": "Hemorragia",
    "efecto": 10,
    "activo": False,
    "antidoto": "Nanobots",
    "turnos_restantes": 0,

}

estados = {
    "huesos": huesos,
    "agotamiento": agotamiento,
    "desangrado": desangrado,
}
# ======================================================================
# ====                     SISTEMA DE ESTADOS                       ====
# ======================================================================

def aplicar_estados(nombre_agotamiento):
    if nombre_agotamiento == agotamiento["nombre"]:
        agotamiento["efecto"] = round(
            min(agotamiento["efecto"] + agotamiento["incremento"], 0.9), 2
        )
        agotamiento["activo"] = True


def calculo_stats(jugador):
    reduccion = agotamiento["efecto"] if agotamiento["activo"] else 0
    factor = 1 - reduccion

    return {
        "hp": jugador["hp"],
        "hp_max": round(jugador["hp_max"] * factor, 2),
        "atk": round(jugador["atk"] * factor, 2),
        "vel": round(jugador["vel"] * factor, 2),
        "def": round(jugador["def"] * factor, 2),
    }


def aplicar_estado(nombre_desangrado):
    if nombre_desangrado == desangrado["nombre"]:
        desangrado["activo"] = True
        desangrado["turnos_restantes"] = 8


def inicio_turno(jugador):
    if not desangrado["activo"]:
        return

    daño = desangrado["efecto"]
    jugador["hp"] = max(0, jugador["hp"] - daño)
    desangrado["turnos_restantes"] -= 1
    print(f"La hemorragia te causa {daño} de daño. HP: {jugador['hp']}")

    if desangrado["turnos_restantes"] <= 0:
        desangrado["activo"] = False
        desangrado["turnos_restantes"] = 0
        print("La hemorragia ha terminado.")


def avanzar_periodo(jugador=None):
    global periodo_actual

    siguiente = (periodos.index(periodo_actual) + 1) % len(periodos)
    periodo_actual = periodos[siguiente]
    aplicar_estados(agotamiento["nombre"])

    if jugador is not None and agotamiento["activo"]:
        jugador["hp"] = min(jugador["hp"], calculo_stats(jugador)["hp_max"])

    return periodo_actual


def use_nanobots():
    for estado in estados.values():
        if estado["antidoto"] == "Nanobots":
            estado["activo"] = False
            if estado is desangrado:
                estado["turnos_restantes"] = 0


def descansar():
    agotamiento["efecto"] = 0.0
    agotamiento["activo"] = False
