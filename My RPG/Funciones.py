# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import random
import Armas
import Ataques

# =========================================================================
# ====                   SISTEMA DE VELOCIDADES                        ====
# =========================================================================

def comparar_velocidad(vel_1, vel_2):
    if vel_1 > vel_2:
        print("El jugador es mas rapido que el enemigo.")
        return 1
    elif vel_1 < vel_2:
        print("El enemigo es mas rapido que el jugador.")
        return 2
    else:
        print("El jugador y el enemigo tienen la misma velocidad.")
        return 0

# =====================================================================
# ====                   SISTEMA DE COMBATE                        ====
# =====================================================================  
 
def inicio_combate(combate_actual): 
    enemigos_combate = []
    
    for enemigo in combate_actual:
        enemigo_actual = enemigo.copy()
        enemigos_combate.append(enemigo_actual)
        
    return enemigos_combate

# =====================================================================
# ====                   SISTEMA DE NIVELES                        ====
# =====================================================================  

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
     #   enemigo["drop"] += enemigo["lv"] + (2 * nivel_extra)

    return combate_actual

# ======================================================================
# ====                     DATOS DE LAS ARMAS                       ====
# ======================================================================

def obtener_arma(nombre):

    return Armas.armas[nombre]

def normalizar_municion(tipo_municion):
    if tipo_municion is None:
        return None
    return str(tipo_municion).replace(" ", "").lower()


def obtener_cantidad_municion(ammo, tipo_municion):
    if ammo is None or tipo_municion is None:
        return 0

    if tipo_municion in ammo:
        return ammo[tipo_municion]

    clave_normalizada = normalizar_municion(tipo_municion)
    for clave, cantidad in ammo.items():
        if normalizar_municion(clave) == clave_normalizada:
            return cantidad

    return 0


def actualizar_cantidad_municion(ammo, tipo_municion, cantidad):
    if ammo is None or tipo_municion is None:
        return

    if tipo_municion in ammo:
        ammo[tipo_municion] = cantidad
        return

    clave_normalizada = normalizar_municion(tipo_municion)
    for clave in list(ammo.keys()):
        if normalizar_municion(clave) == clave_normalizada:
            ammo[clave] = cantidad
            return

    ammo[tipo_municion] = cantidad


def obtener_durabilidad_max(arma):
    if arma is None:
        return 0

    if "durabilidad_max" in arma:
        return arma["durabilidad_max"]
    if "durabilidad max" in arma:
        return arma["durabilidad max"]
    return arma.get("durabilidad", 0)


def mostrar_municion(arma_principal=None, arma_secundaria=None, ammo=None):
    if ammo is None:
        return

    if arma_principal is not None:
        tipo_municion = arma_principal.get("ammo")
        if tipo_municion is None:
            tipo_municion = arma_principal.get("proyectiles")
        if tipo_municion is None:
            tipo_municion = arma_principal.get("cartuchos")
        if tipo_municion is not None:
            cantidad = obtener_cantidad_municion(ammo, tipo_municion)
            print(f"municion principal ({tipo_municion}): {cantidad}")

    if arma_secundaria is not None:
        tipo_municion = arma_secundaria.get("ammo")
        if tipo_municion is None:
            tipo_municion = arma_secundaria.get("proyectiles")
        if tipo_municion is None:
            tipo_municion = arma_secundaria.get("cartuchos")
        if tipo_municion is not None:
            cantidad = obtener_cantidad_municion(ammo, tipo_municion)
            print(f"municion secundaria ({tipo_municion}): {cantidad}")
    elif arma_secundaria is None:
        print("No tienes arma secundaria.")


def mostrar_durabilidad(arma):
    if arma is None:
        return

    durabilidad_actual = arma.get("durabilidad", 0)
    durabilidad_maxima = obtener_durabilidad_max(arma)
    print(f"Durabilidad de {arma.get('nombre', 'arma')}: {durabilidad_actual}/{durabilidad_maxima}")
 
# ====================================================================================
# ====                   SISTEMA DE PREPARACION DE COMBATE                        ====
# ====================================================================================

def obtener_valor(objeto, *claves, default=0):
    if objeto is None:
        return default
    for clave in claves:
        if clave in objeto:
            return objeto[clave]
    return default


def mostrar_estado_combate(Jugador, enemigos, arma_principal=None, arma_secundaria=None, ammo=None):
    print("\n--- ESTADO DEL COMBATE ---")
    print(f"{Jugador['Nombre']} HP:{Jugador['hp']}/{Jugador['hp_max']} ATK:{Jugador['Atk']} DEF:{Jugador['def']} VEL:{Jugador['vel']} LV:{Jugador['lv']}")
    if arma_principal is not None:
        mostrar_municion(arma_principal, arma_secundaria, ammo)
        mostrar_durabilidad(arma_principal)
        if arma_secundaria is not None:
            mostrar_durabilidad(arma_secundaria)

    for enemigo in enemigos:
        print(f"{enemigo['name']} HP:{enemigo['hp']} ATK:{enemigo['atk']} DEF:{enemigo['def']} VEL:{enemigo['vel']} AMMO:{enemigo['ammo']} LV:{enemigo['lv']}")


def preparar_combate(Jugador, enemigos, Armas_equipadas, ammo):
    arma_primaria = obtener_arma(Armas_equipadas["primaria"])
    print(f"Arma principal: {arma_primaria['nombre']}")

    arma_secundaria = None
    if Armas_equipadas["secundaria"] is not None:
        arma_secundaria = obtener_arma(Armas_equipadas["secundaria"])
        print(f"Arma secundaria: {arma_secundaria['nombre']}")

    mostrar_estado_combate(Jugador, enemigos, arma_primaria, arma_secundaria, ammo)

# ===============================================================================
# ====                   SISTEMA DE INICIO DE COMBATE                        ====
# ===============================================================================

def iniciar_combate(Jugador, combate_actual):
    return comparar_velocidad(Jugador["vel"], combate_actual[0]["vel"])


def obtener_ataque(nombre):

    return Ataques.ataques[nombre]

# ===========================================================+++++++++==========
# ====                   SISTEMA DE ARMAS Y MUNICION                        ====
# ==================================================+++++++++===================

#aprendi un nuevo concepto .get se puede utilizar para situaciones como la operacion de busqueda de un ataque especifico para la arma (gib hub es lo mejor que pude encontrar)

def verificar_requi_ataques(ataque, Arma_equipada, ammo ):
    if ataque is None:
        return False

    if "arma" in ataque:
        if Arma_equipada is None:
            return False
        if Arma_equipada.get("nombre") != ataque["arma"]:
            return False

    for clave, valor in ataque.items():
        if clave not in ["nombre", "arma", "atk", "durabilidad", "costo", "desgaste", "durabilidad_max", "durabilidad max", "reparaciones", "reparaciones max"]:
            if valor <= 0:
                continue

            if ammo is None:
                return False

            if clave == "ammo":
                if Arma_equipada is None:
                    return False
                tipo_municion = Arma_equipada.get("ammo")
            else:
                tipo_municion = clave

            if tipo_municion is None or obtener_cantidad_municion(ammo, tipo_municion) < valor:
                return False

    return True


def descontar_municion(ataque, Arma_equipada, ammo):
    if ataque is None or not verificar_requi_ataques(ataque, Arma_equipada, ammo):
        return False

    for clave, cantidad in ataque.items():
        if clave in ["nombre", "arma", "atk", "durabilidad", "costo", "desgaste", "durabilidad_max", "durabilidad max", "reparaciones", "reparaciones max"]:
            continue

        if cantidad <= 0:
            continue

        if clave == "ammo":
            tipo_municion = Arma_equipada.get("ammo")
        else:
            tipo_municion = clave

        municion_actual = obtener_cantidad_municion(ammo, tipo_municion)
        actualizar_cantidad_municion(ammo, tipo_municion, municion_actual - cantidad)

    return True


def verificar_durabilidad(ataque, Arma_equipada):
    if Arma_equipada is None:
        return False

    desgaste = ataque.get("desgaste", 0)
    return Arma_equipada.get("durabilidad", 0) >= desgaste


def descontar_durabilidad(ataque, Arma_equipada):
    if "desgaste" not in ataque:
        return True

    if not verificar_durabilidad(ataque, Arma_equipada):
        return False

    Arma_equipada["durabilidad"] -= ataque["desgaste"]
    return True

def aplicar_daño(ataque, objetivo):
    if ataque is None or objetivo is None:
        return 0

    daño_base = ataque.get("atk", 0)
    defensa = obtener_valor(objetivo, "Defen", "def", "DEFEN", default=0)
    daño = max(0, daño_base - defensa)

    hp_actual = obtener_valor(objetivo, "Hp", "hp", "HP", default=0)
    nuevo_hp = max(0, hp_actual - daño)

    if "Hp" in objetivo:
        objetivo["Hp"] = nuevo_hp
    elif "hp" in objetivo:
        objetivo["hp"] = nuevo_hp
    else:
        objetivo["hp"] = nuevo_hp

    return daño


def obtener_tipo_municion_arma(arma, ataque=None):
    if arma is None:
        return None

    for clave in ["ammo", "proyectiles", "cartuchos", "ammo_penetrante", "ammo_antimateria"]:
        if arma.get(clave) is not None:
            return arma.get(clave)

    if ataque is not None:
        for clave, valor in ataque.items():
            if clave in ["nombre", "arma", "atk", "durabilidad", "costo", "desgaste", "durabilidad_max", "durabilidad max", "reparaciones", "reparaciones max"]:
                continue
            if valor > 0:
                return clave

    return None


def usar_ataque(ataque, arma_equipada, ammo, objetivo=None):
    if ataque is None:
        print("Ese ataque no existe.")
        return False

    if objetivo is None:
        print("No hay enemigo objetivo para atacar.")
        return False

    if not verificar_requi_ataques(ataque, arma_equipada, ammo):
        print(f"No puedes usar {ataque.get('nombre', 'este ataque')} con el arma actual o sin municion suficiente.")
        return False

    if not verificar_durabilidad(ataque, arma_equipada):
        print(f"La durabilidad de {arma_equipada.get('nombre', 'el arma')} es insuficiente para usar {ataque.get('nombre', 'este ataque')}.")
        return False

    if not descontar_municion(ataque, arma_equipada, ammo):
        print("No se pudo descontar la municion.")
        return False

    if not descontar_durabilidad(ataque, arma_equipada):
        print("No se pudo descontar la durabilidad.")
        return False

    daño = aplicar_daño(ataque, objetivo)
    print(f"Ataque usado: {ataque.get('nombre', 'ataque')}")
    print(f"Daño infligido: {daño}")
    vida_actual = obtener_valor(objetivo, 'Hp', 'hp', default=0)
    vida_maxima = obtener_valor(objetivo, 'Hp_max', 'hp_max', default=vida_actual)
    print(f"Vida del enemigo: {vida_actual}/{vida_maxima}")

    tipo_municion = obtener_tipo_municion_arma(arma_equipada, ataque)
    if tipo_municion is not None:
        print(f"Municion restante: {obtener_cantidad_municion(ammo, tipo_municion)}")
    mostrar_durabilidad(arma_equipada)

    if obtener_valor(objetivo, 'Hp', 'hp', default=0) <= 0:
        print(f"{objetivo.get('name', 'Enemigo')} ha sido derrotado.")

    return True
