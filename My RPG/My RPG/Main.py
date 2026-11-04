# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import Combate
import Jugador
import Zonas
import Recompensas
# =======================================================================
# ====                    BUCLE PRINCIPAL DE COMBATE                  ====
# =======================================================================

if 1 <= Zonas.seleccion <= 6:
    Combate.iniciar_combate(
        Jugador.jugador,
        Zonas.combate_actual,
        Jugador.Armas_equipadas,
        Jugador.ammo
    )
