# =================================================================
# ====                   ARMAS DE INICIO                       ====
# ================================================================= 

Armas_I = {
    "pistola": {"nombre": "Pistola", "atk": 15, "ammo": "ammo", "durabilidad": 50, "durabilidad max": 50, "reparaciones": 0, "reparaciones max": 2, "precio": 100},
    "laetum": {"nombre": "laetum", "atk": 20, "ammo": "ammo", "durabilidad": 50, "durabilidad_max": 50, "reparaciones": 0, "reparaciones max": 2, "precio": 100},
    "rifle": {"nombre": "Rifle", "atk": 25, "ammo": "ammo", "durabilidad": 70, "durabilidad_max": 70, "reparaciones": 0, "reparaciones max": 2, "precio": 100}
}
# ===================================================================
# ====                   ARMAS DE PROGRESO                       ====
# =================================================================== 

Armas_P = {
    "escopeta": {"nombre": "Escopeta", "atk": 35, "ammo": "cartuchos", "durabilidad": 60, "durabilidad_max": 60, "reparaciones": 0, "reparaciones max": 2, "precio": 100},
    "minigun": {"nombre": "Minigun", "atk": 50, "ammo": "9mm", "durabilidad": 80, "durabilidad_max": 80, "reparaciones": 0, "reparaciones max": 2, "precio": 100},
    "lanza_granadas": {"nombre": "Lanza granadas", "atk": 75, "proyectiles": "proyectiles", "durabilidad": 50, "durabilidad_max": 50, "reparaciones": 0, "reparaciones max": 2, "precio": 100}
}

# =================================================================
# ====                   ARMAS DE ENDGAME                      ====
# ================================================================= 

Armas_E = {
    "rifle_AAH": {"nombre": "Rifle AAH", "atk": 40, "ammo": "ammo_penetrante", "durabilidad": 70, "durabilidad_max": 70, "reparaciones": 0, "reparaciones max": 3, "precio": 100},
    "rifle_de_CWH": {"nombre": "Rifle CWH", "atk": 100, "ammo": "ammo_antimateria", "durabilidad": 90, "durabilidad_max": 50, "reparaciones": 0, "reparaciones max": 3, "precio": 100}
}

# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

armaS = [Armas_I, Armas_P, Armas_E]
armas = {**Armas_I, **Armas_P, **Armas_E}