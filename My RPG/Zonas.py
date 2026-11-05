# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import random
import Enemigos
import Funciones
import Funciones
import Jugador
import Combate
import Estados

jugador = Jugador.jugador
ammo = Jugador.ammo
Armas_equipadas = Jugador.Armas_equipadas

# =====================================================================
# ====                    SISTEMA DE ZONAS                         ====
# =====================================================================

# primera zona 
ruina = random.choices(Enemigos.enemigos, weights=Enemigos.peso_n, k=2)

# 2da zona 
ruina_1 = random.choices(Enemigos.enemigos_p, weights=Enemigos.peso_p, k=1)
ruina_2 = random.choices(Enemigos.enemigos_p, weights=Enemigos.peso_p, k=2)
ruina_3 = random.choices(Enemigos.enemigos_p, weights=Enemigos.peso_p, k=1) + random.choices(Enemigos.enemigos, weights=Enemigos.peso_n, k=2)
ruina_4 = random.choices(Enemigos.enemigos_p, weights=Enemigos.peso_p, k=3)

combates = [ruina_1, ruina_2, ruina_3, ruina_4]
combate = random.choice(combates)

# zona de bosses
desierto = Enemigos.cyber_snake.copy()
laboratorio = Enemigos.cyber_crocodile.copy()
ciudad_decadente = Enemigos.ia_automata.copy()
centro_de_mando = Enemigos.ultimate_ia.copy()

zonas = {
    1: ruina,
    2: combates,
    3: desierto,
    4: laboratorio,
    5: ciudad_decadente,
    6: centro_de_mando,
    7: "casa",          
    8: "tienda"
}

# =====================================================================
# ====                   SISTEMA DE ZONAS 2                        ====
# =====================================================================

seleccion = int(input(f"selecciona el lugar al que deseas ir (1-8): "))

if seleccion == 1:
    combate_actual = Funciones.inicio_combate(zonas[seleccion])
    combate_actual = Funciones.generar_enemigos(combate_actual, jugador["lv"], "enemigos")
    print("Has entrado en la Ruina Yomu. \n \n prepárate para el combate.")
    Combate.preparar_combate(jugador, combate_actual, Armas_equipadas, ammo)

elif seleccion == 2:
    combate_actual = Funciones.inicio_combate(random.choice(zonas[seleccion]))
    combate_actual = Funciones.generar_enemigos(combate_actual, jugador["lv"], "enemigos_p")
    print("Has entrado en la Ruina Yonozuka, \n \n prepárate para el combate.")
    Combate.preparar_combate(jugador, combate_actual, Armas_equipadas, ammo)

elif seleccion == 3:
    combate_actual = Funciones.inicio_combate([zonas[seleccion]])
    combate_actual = Funciones.generar_enemigos(combate_actual, jugador["lv"], "bosses")
    print("Has entrado en el Desierto de la Muerte.")
    print("\n El ambiente es muy tranquilo.")
    print("\n Mas tranquilo de lo que deberia")
    print("\n...")
    print("\n Algo se acerca que es eso")
    print("\n Pero algo se mueve en la arena a una velocidad inhumana,")
    print(f"\n {jugador['Nombre']} Mierda se acerca, esto es malo, no estoy preparado para esto.")
    print("\n Sale algo gigante de la arena")
    print(f"\n {Enemigos.cyber_snake['name']}... CLANG--  BRRRRRRRRRR-- KRRSHSHSH.")
    Combate.preparar_combate(jugador, combate_actual, Armas_equipadas, ammo)

elif seleccion == 4:
    combate_actual = Funciones.inicio_combate([zonas[seleccion]])
    combate_actual = Funciones.generar_enemigos(combate_actual, jugador["lv"], "bosses")
    print("Has entrado en el Laboratorio de la Muerte,")
    print(f"\n {jugador['Nombre']} Hay un rumor que dice que aqui se encuentra el enemigo mas peligroso.")
    print(f"\n {jugador['Nombre']} Espero sea solo un rumor, no quiero morir aqui, tuve suficiente con esa serpiente.")
    print(f"\n {jugador['Nombre']} ... Busquemos esa reliqueas y larguemonos de aqui.")  
    print(f"\n {Enemigos.cyber_crocodile['name']}... BAAAAAMMMM-- CLASSHHHHHHH.") 
    Combate.preparar_combate(jugador, combate_actual, Armas_equipadas, ammo)

elif seleccion == 5:
    combate_actual = Funciones.inicio_combate([zonas[seleccion]])
    combate_actual = Funciones.generar_enemigos(combate_actual, jugador["lv"], "bosses")
    print("Has entrado en la Ciudad Decadente,")
    print(f"\n {jugador['Nombre']} Esta ciudad es un algo...")
    print(f"\n {jugador['Nombre']} ... Pero bueno, vamos a buscar esa reliquea y larguemonos de aqui.")
    print(f"\n {jugador['Nombre']} Podemos hacer un trato? solo quiero los chromebites que deseasacambio de ellos.")
    print(f"\n {Enemigos.ia_automata['name']}... Me pueden dar algo a cambio de ellos! Es tu vida, ustedes los de nuevo mundo saquean al viejo mundo como si fueran los dueños pero es hora de que paguen por sus crimenes.")
    Combate.preparar_combate(jugador, combate_actual, Armas_equipadas, ammo)

elif seleccion == 6:
    combate_actual = Funciones.inicio_combate([zonas[seleccion]])
    combate_actual = Funciones.generar_enemigos(combate_actual, jugador["lv"], "bosses")
    print("Has entrado en el Centro de Mando.")
    print(f"\n {jugador['Nombre']} Este es el lugar mas peligroso de todo el viejo mundo, pero debe haber mas servotrajes, trajes de aumento, reliqueas y chromebites aqui, este es mi paraiso.")
    print(f"\n {Enemigos.ultimate_ia['name']}... Se te perdio algo? No te preocupes, solo sera un momento, no te preocupes, no te dolera, solo sera un momento.")
    print(f"\n {jugador['Nombre']} no gracias yo ya me iba, por muchas cosas valiosas que haya aqui, no vale la pena morir por ellas.")
    print(f"\n CLANKKK. \n {Enemigos.ultimate_ia['name']} Nadie tiene permitido irse de aqui, nadie, no importa quien seas.")
    Combate.preparar_combate(jugador, combate_actual, Armas_equipadas, ammo)

# =====================================================================
# ====                   SISTEMA DE ZONAS 3                        ====
# =====================================================================

elif seleccion == 7:
    print("Has entrado en tu casa. \n \n Aqui puedes descansar para eliminar el agotamiento; la hemorragia requiere Nanobots.")
    print(f"\n {jugador['nombre']} Que bueno es estar en casa, me siento seguro aqui y puedo aliviar mi agotamiento.")
    Estados.descansar()
    print(f"\n {jugador['nombre']} ... Pero bueno, no puedo quedarme aqui para siempre, tengo que seguir adelante.")

elif seleccion == 8:
    print("Has entrado en la tienda. \n \n aqui puedes comprar y vender objetos, armas y armaduras.")
    print(f"\n {jugador['nombre']} Hora de abastecerme de municion mi vida depende de ello, no quiero morir por falta de municion.")

else:
    print("Seleccion invalida, por favor selecciona un lugar valido (1-8).")