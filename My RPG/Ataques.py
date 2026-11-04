# ==================================================================
# ====                   ATAQUES NORMALES                       ====
# ================================================================== 

Ataques_N = { 
    "puñetazo": {"nombre": "Puñetazo", "atk": 10, "ammo": 0},
    "patada": {"nombre": "Patada", "atk": 15, "ammo": 0}
}

# ===================================================================
# ====                   ATAQUES SPECIALES                       ====
# =================================================================== 

Ataques_S = {
    "disparo": {"nombre": "Disparo", "atk": 25, "ammo": 1, "desgaste": 5},
    "rafaga": {"nombre": "Rafaga", "atk": 125, "ammo": 10, "desgaste": 25},
    "disparo_critico": {"nombre": "Disparo Critico", "atk": 65, "ammo": 4, "arma": "Rifle", "desgaste": 25}
}

# ====================================================================
# ====                   ATAQUES COMPRABLES                       ====
# ==================================================================== 

Ataques_C = {
    "corte": {"nombre": "Corte", "atk": 100, "ammo": 0, "costo": 250},
    "trampas" : {"nombre": "Trampas", "atk": 150, "ammo": 0, "costo": 750}
}

# ===================================================================
# ====                   ATAQUES DE ARMAS                        ====
# ===================================================================

Ataques_A = {
    "explosion": {"nombre": "Explosión", "arma": "Lanza granadas", "atk": 150, "proyectiles": 10, "desgaste": 25 },
    "disparo_penetrante": {"nombre": "Disparo Penetrante", "arma": "Rifle de asalto", "atk": 200, "ammo_penetrante": 25, "desgaste": 20 },
    "disparo_antimateria": {"nombre": "Disparo Antimateria", "arma": "Rifle de antimateria", "atk": 500, "ammo_antimateria": 5, "desgaste": 10 },
    "fuego_quemarropa" : {"nombre": "Fuego a quemarropa", "arma": "Minigun", "atk": 200, "proyectiles": 100, "desgaste": 20 },
    "disparo_cargado" : {"nombre": "Disparo cargado", "arma": "Escopeta", "atk": 150, "cartuchos": 8, "desgaste": 20 }
}

# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

ataques = {**Ataques_N, **Ataques_S, **Ataques_C, **Ataques_A}