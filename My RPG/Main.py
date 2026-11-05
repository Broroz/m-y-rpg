# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import Combate
import Jugador
import Zonas
import Recompensas
import Cofres
# =======================================================================
# ====                    BUCLE PRINCIPAL DE COMBATE                  ===
# =======================================================================

if 1 <= Zonas.seleccion <= 6:
    zonas_cofres = {
        1: "zona_1",
        2: "zona_2",
        3: "boss_1",
        4: "boss_2",
        5: "boss_3",
        6: "boss_4",
    }
    zona_cofre = zonas_cofres[Zonas.seleccion]
    Cofres.entrar_zona(zona_cofre)

    Combate.iniciar_combate(
        Jugador.jugador,
        Zonas.combate_actual,
        Jugador.Armas_equipadas,
        Jugador.ammo
    )

    if Jugador.jugador["hp"] > 0:
        Cofres.explorar_cofres(zona_cofre, Jugador.jugador)

    Cofres.salir_zona(zona_cofre)
