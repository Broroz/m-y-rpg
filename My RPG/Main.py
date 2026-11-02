# =================================================================
# ====                     IMPORTACIONES                       ====
# =================================================================

import random
import Enemigos    
import Funciones  
import Ataques

# =====================================================================
# ====                     DATOS DEL JUGADOR                       ====
# =====================================================================

Jugador = {
    "Nombre": input("Cual es el nombre del protagonista?: "),
    "vel": 10,
    "hp": 100,
    "hp_max": 100,
    "Atk": 25,
    "def": 10,
    "lv": 1 
}
ammo = {
        "ammo": 10,
        "ammo_max": 10,
        "cartuchos": 0,
        "cartuchos_max": 15,
        "proyectiles": 0,
        "proyectiles_max": 20,
        "9 mm": 0,
        "9 mm_max": 100,
        "ammo_antimateria": 0,
        "ammo_antimateria_max": 5,
        "ammo_penetrante": 0,
        "ammo_penetrante_max": 10
}

Armas_equipadas = { "primaria" : "pistola", "secundaria" : None}

#trajes_equipadas = { "1er armadura" : "none"}
#servotrajes_equipadas = { "1er servotraje" : "none"}

hp = 100
hp_max = 100
atk = 25
ammo_actual = 10
ammo_max = 10
lv = 1
exp = 0 
exp_necesaria = 100
credits = 0
inventario = []

# =====================================================================
# ====                 SISTEMA DE NIVELAMIENTO                     ====
# =====================================================================

while exp >= exp_necesaria:
    lv += 1
    exp -= exp_necesaria
    exp_necesaria = int(exp_necesaria + 75)
    hp += 10
    hp_max += 10
    atk += 5
    Jugador["vel"] += 5  

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

# Unificamos los participantes
participantes = { 
    "jugador": Jugador, 
    "enemigo": Enemigos.enemigos, 
    "enemigos_p": Enemigos.enemigos_p, 
    "bosses": Enemigos.bosses
}

# =====================================================================
# ====                   SISTEMA DE ZONAS 2                        ====
# =====================================================================

while True:
    seleccion = int(input(f"selecciona el lugar al que deseas ir (1-8): "))

    if seleccion == 1:
        combate_actual = Funciones.inicio_combate(zonas[seleccion])
        combate_actual = Funciones.generar_enemigos(combate_actual, lv, "enemigos")
        print("Has entrado en la Ruina Yomu. \n \n prepárate para el combate.")
        Funciones.preparar_combate(Jugador, combate_actual, Armas_equipadas, ammo)

    elif seleccion == 2:
        combate_actual = Funciones.inicio_combate(random.choice(zonas[seleccion]))
        combate_actual = Funciones.generar_enemigos(combate_actual, lv, "enemigos_p")
        print("Has entrado en la Ruina Yonozuka, \n \n prepárate para el combate.")
        Funciones.preparar_combate(Jugador, combate_actual, Armas_equipadas, ammo)

    elif seleccion == 3:
        combate_actual = Funciones.inicio_combate([zonas[seleccion]])
        combate_actual = Funciones.generar_enemigos(combate_actual, lv, "bosses")
        print("Has entrado en el Desierto de la Muerte.")
        print("\n El ambiente es muy tranquilo.")
        print("\n Mas tranquilo de lo que deberia")
        print("\n...")
        print("\n Algo se acerca que es eso")
        print("\n Pero algo se mueve en la arena a una velocidad inhumana,")
        print(f"\n {Jugador['Nombre']} Mierda se acerca, esto es malo, no estoy preparado para esto.")
        print("\n Sale algo gigante de la arena")
        print(f"\n {Enemigos.cyber_snake['name']}... CLANG--  BRRRRRRRRRR-- KRRSHSHSH.")
        Funciones.preparar_combate(Jugador, combate_actual, Armas_equipadas, ammo)

    elif seleccion == 4:
        combate_actual = Funciones.inicio_combate([zonas[seleccion]])
        combate_actual = Funciones.generar_enemigos(combate_actual, lv, "bosses")
        print("Has entrado en el Laboratorio de la Muerte,")
        print(f"\n {Jugador['Nombre']} Hay un rumor que dice que aqui se encuentra el enemigo mas peligroso.")
        print(f"\n {Jugador['Nombre']} Espero sea solo un rumor, no quiero morir aqui, tuve suficiente con esa serpiente.")
        print(f"\n {Jugador['Nombre']} ... Busquemos esa reliqueas y larguemonos de aqui.")  
        print(f"\n {Enemigos.cyber_crocodile['name']}... BAAAAAMMMM-- CLASSHHHHHHH.") 
        Funciones.preparar_combate(Jugador, combate_actual, Armas_equipadas, ammo)

    elif seleccion == 5:
        combate_actual = Funciones.inicio_combate([zonas[seleccion]])
        combate_actual = Funciones.generar_enemigos(combate_actual, lv, "bosses")
        print("Has entrado en la Ciudad Decadente,")
        print(f"\n {Jugador['Nombre']} Esta ciudad es un algo...")
        print(f"\n {Jugador['Nombre']} ... Pero bueno, vamos a buscar esa reliquea y larguemonos de aqui.")
        print(f"\n {Jugador['Nombre']} Podemos hacer un trato? solo quiero los chromebites que deseasacambio de ellos.")
        print(f"\n {Enemigos.ia_automata['name']}... Me pueden dar algo a cambio de ellos! Es tu vida, ustedes los de nuevo mundo saquean al viejo mundo como si fueran los dueños pero es hora de que paguen por sus crimenes.")
        Funciones.preparar_combate(Jugador, combate_actual, Armas_equipadas, ammo)

    elif seleccion == 6:
        combate_actual = Funciones.inicio_combate([zonas[seleccion]])
        combate_actual = Funciones.generar_enemigos(combate_actual, lv, "bosses")
        print("Has entrado en el Centro de Mando.")
        print(f"\n {Jugador['Nombre']} Este es el lugar mas peligroso de todo el viejo mundo, pero debe haber mas servotrajes, trajes de aumento, reliqueas y chromebites aqui, este es mi paraiso.")
        print(f"\n {Enemigos.ultimate_ia['name']}... Se te perdio algo? No te preocupes, solo sera un momento, no te preocupes, no te dolera, solo sera un momento.")
        print(f"\n {Jugador['Nombre']} no gracias yo ya me iba, por muchas cosas valiosas que haya aqui, no vale la pena morir por ellas.")
        print(f"\n CLANKKK. \n {Enemigos.ultimate_ia['name']} Nadie tiene permitido irse de aqui, nadie, no importa quien seas.")
        Funciones.preparar_combate(Jugador, combate_actual, Armas_equipadas, ammo)

# =========================================================================================
# ====                   DATOS DE INICIO DE COMBATE DEL COMBATE                        ====
# =========================================================================================

    if 1 <= seleccion <= 6:

        resultado = Funciones.iniciar_combate(Jugador, combate_actual)
        arma_principal = Funciones.obtener_arma(Armas_equipadas["primaria"])

        if Armas_equipadas["secundaria"] is not None:
            arma_secundaria = Funciones.obtener_arma(Armas_equipadas["secundaria"])
        else:
            arma_secundaria = None

        seleccion_ataque = input("Que ataque desea realizar?")
        ataque = Funciones.obtener_ataque(seleccion_ataque)
        print(ataque)

        arma_activa = arma_principal
        objetivo = combate_actual[0]
        if Funciones.usar_ataque(ataque, arma_activa, ammo, objetivo):
            if objetivo.get("hp", objetivo.get("Hp", 0)) > 0:
                daño_enemigo = Funciones.aplicar_daño({"atk": objetivo["atk"]}, Jugador)
                print(f"{objetivo['name']} te golpea por {daño_enemigo} de daño.")
            Funciones.mostrar_estado_combate(Jugador, combate_actual, arma_activa, arma_secundaria, ammo)

# =====================================================================
# ====                   SISTEMA DE ZONAS 3                        ====
# =====================================================================

    elif seleccion == 7:
        print("Has entrado en tu casa. \n \n aqui puedes descansar y recuperar tu salud los debuff han desaparecido.")
        print(f"\n {Jugador['Nombre']} Que bueno es estar en casa, me siento seguro aqui, puedo descansar y recuperar mi salud.")
        print(f"\n {Jugador['Nombre']} ... Pero bueno, no puedo quedarme aqui para siempre, tengo que seguir adelante.")

    elif seleccion == 8:
        print("Has entrado en la tienda. \n \n aqui puedes comprar y vender objetos, armas y armaduras.")
        print(f"\n {Jugador['Nombre']} Hora de abastecerme de municion mi vida depende de ello, no quiero morir por falta de municion.")

    else:
        print("Seleccion invalida, por favor selecciona un lugar valido (1-8).")

