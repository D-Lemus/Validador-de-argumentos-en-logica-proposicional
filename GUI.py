import flet as ft
import shunting_yard as log
import truth_tables as TV
import premade_tables as preT

# ------ BOTONES Y FUNCIONES GLOBALES ----------------------------------------------
# usados varias veces en diferentes páginas
# ----------------------------------------------------------------------------------

def divisor():
    '''linea divisora'''
    return ft.Divider(color=ft.Colors.PRIMARY, thickness=2)

def boton_volver(pagina):
    '''regresa a pag_inicio'''
    return ft.ElevatedButton("← volver", on_click = pagina)

def boton_reset(accion, tip):
    '''regresa a página actual'''
    return ft.ElevatedButton("reset", on_click = accion, icon=ft.Icons.RESTART_ALT,
                                    tooltip=tip)

def boton_ayuda(accion_ayuda):
    return ft.IconButton(icon=ft.Icons.HELP,
                            icon_color=ft.Colors.PRIMARY,
                            icon_size=30,
                            style=ft.ButtonStyle(shape=ft.CircleBorder()),
                            on_click = accion_ayuda,
                            tooltip="Acerca de uso"
                            )
                            
def mensaje_ayuda(page, titulo, contenido):
    '''pop up mensaje'''
    ayuda = ft.AlertDialog(
                title=ft.Text(titulo),
                content=ft.Text(contenido),
                actions=[ft.TextButton("Ok!", on_click=lambda e: cerrar())],
                )
    def cerrar():
        ayuda.open=False
        page.update()
        
    page.overlay.append(ayuda)
    ayuda.open=True
    page.update()


def valida_calcular(texto, accion):
    return ft.ElevatedButton(texto, on_click = accion,
                            icon=ft.Icons.CHECK_CIRCLE,
                            width=120, height=120,
                            style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                            size=15,
                            weight="bold",
                            ),
                            shape=ft.RoundedRectangleBorder(radius=10),),
                            )

def teclado(lista_simbolos, acc_simbolos, acc_limpiar, tip, texto, accion_validar):
    '''crea varios botones y los acomoda'''
    botones_simbolos = []
    for s in lista_simbolos:
        botones_simbolos.append(ft.ElevatedButton(s, data=s, on_click=acc_simbolos, autofocus=False, 
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),
                            text_style=ft.TextStyle(size=20,weight="bold"),),)
        )
    b_limpiar = ft.IconButton(icon=ft.Icons.CLEANING_SERVICES,
                            icon_color=ft.Colors.BLACK,
                            icon_size=40,
                            bgcolor=ft.Colors.SECONDARY,
                            width=20, height=20,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            on_click = acc_limpiar,
                            tooltip= tip
                            )
    b_validar = ft.ElevatedButton(texto, on_click = accion_validar,
                            icon=ft.Icons.CHECK_CIRCLE,
                            width=150, height=150,
                            style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                            size=15,
                            weight="bold",
                            ),
                            shape=ft.RoundedRectangleBorder(radius=10),),
                            )
    grid_simbolos = ft.GridView(
        controls= botones_simbolos + [b_limpiar],
        runs_count=4,
        spacing=20,
        run_spacing=10,
        child_aspect_ratio=1.0,
        width=280,
        height=150,
        )
    return ft.Row(controls=[grid_simbolos, b_validar],
                            alignment = ft.MainAxisAlignment.CENTER,
                            vertical_alignment = ft.CrossAxisAlignment.CENTER,
                            spacing=30)

# ------ PÁGINA PRINCIPAL ----------------------------------------------------------

def main(page: ft.Page):
    'abre ventana'
    page.title = "Validador de Argumentos" #título de la pag

    # alinear y dar tamaño a la pag
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 700
    page.window.width = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
        ))

    def pag_inicio(e=None):
        'acomodo de pag inicio'
        page.clean() #limpia todo lo que haya antes en la pag
        
        # fondo interactivo
        def tes_a_efes(e):
            '''Cambio de T a F y de colores'''
            e.control.content.value = "F" if e.data == True else "T"
            e.control.content.color = ft.Colors.RED if e.data == True else ft.Colors.GREEN_700
            e.control.update()

        grid = ft.GridView(
            max_extent=50,
            child_aspect_ratio=1,
            )

        for _ in range(200):
            grid.controls.append(
                ft.Container(
                    content=ft.Text("T", size=15, weight="bold", color=ft.Colors.BLUE_GREY,),
                    on_hover=tes_a_efes,
                    alignment=ft.Alignment.CENTER,
                ))
        # fin de fondo interactivo

        # variables para textos simples (con tamaño, negritas y alineación)
        bienvenida = ft.Text("BIENVENIDX",
                             size = 60,
                             weight = "bold",
                             text_align = ft.TextAlign.CENTER,
                             )
        subsaludo = ft.Text("validador de argumentos",
                            size = 25,
                            text_align = ft.TextAlign.CENTER,
                            )

        # variables para botones con sombra ("texto dentro del botón", evento = función)
        b_empezar = ft.ElevatedButton("empezar!",
                                on_click = pag_argumentos,
                                width=200, height=90,
                                style=ft.ButtonStyle(text_style=ft.TextStyle(size=28,weight="bold",)),
                                tooltip=":D",
                                )
        b_tablas = ft.IconButton(icon=ft.Icons.TABLE_CHART,
                                icon_color=ft.Colors.BLACK,
                                icon_size=80,
                                bgcolor=ft.Colors.SECONDARY,
                                on_click = pag_tablas,
                                width=100, height=100,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
                                tooltip="tablas",
                                )
        b_calculadora = ft.IconButton(icon=ft.Icons.CALCULATE,
                                icon_color=ft.Colors.BLACK,
                                icon_size=80,
                                bgcolor=ft.Colors.SECONDARY,
                                on_click = pag_calculadora,
                                width=100, height=100,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
                                tooltip="calculadora"
                                )
        b_ayuda = boton_ayuda(
            lambda e:mensaje_ayuda(page,
                                "Herramientas",
                                "★ VALIDADOR: " \
                                "Introduce tu argumento para analizar su validez\n" \
                                "\t\t\t\t+ Calculadora: " \
                                "Descubre el valor de verdad de tu proposición\n" \
                                "\t\t\t\t+ Tablas: " \
                                "Conoce las tablas de verdad y equivalencias lógicas\n"
                                ))
        
        # acomoda botones en fila o columna y las agrega a la página
        b_extras = ft.Row(controls=[b_tablas, b_calculadora],
                          alignment=ft.MainAxisAlignment.CENTER, spacing=30,
                          )
        contenido = (ft.Column(
                    controls=[bienvenida, b_empezar, subsaludo, ft.Container(height=40), b_extras],
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    ))
        
        # layout: agrega todas las variables (inputs, botones, texto) a la pag
        page.add(ft.Stack([grid, b_ayuda, contenido],expand=True))
            
# ------ PÁGINA DE VALIDADOR DE ARGUMENTOS ----------------------------------------------------------

    def pag_argumentos(e=None):
        'acomodo pag de argumentos'
        page.clean()
        page.scroll = ft.ScrollMode.AUTO

        # detecta input activo para insertar simbolos
        campo = {"input_actual": None}
        def enfocar(e):
            campo["input_actual"] = e.control


        chat = ft.Column() #crea un espacio para agregar textos (argumentos y conclusiones) en forma de columna
        #inputs
        argumentos = ft.TextField(label="argumentos",
                            hint_text="p∨q",
                            autofocus=True,
                            on_focus = enfocar,
                            )
        conclu = ft.TextField(label="conclusion",
                            hint_text="r",
                            on_focus = enfocar,
                            )

        #lista donde se almacenaran las premisas 
        listas_premisas = []
        txt_premisas = ft.Text("Premisas: ", weight = "bold")
        txt_conclusion = ft.Text("Conclusión: ", weight = "bold")

        def send_click(e):
            '''mostrar en pantalla lo escrito en los inputs y agregarlo a lista'''
            #lista para guardar las premisas. Si el input de argumentos no está vacío, agrega el argumento a la lista de premisas y muestra las premisas guardadas en pantalla.
            if argumentos.value.strip() != "":
                listas_premisas.append(argumentos.value.strip())
                txt_premisas.value = "Premisas:\n" + "\n".join(listas_premisas)
                argumentos.value = ""
                page.update()
            else: txt_premisas.value = "INVALIDO"

        def send_conclusion(e):
            '''mostrar en pantalla lo escrito en el input'''
            if conclu.value.strip() != "":
                txt_conclusion.value = "Conclusión:\n" + conclu.value.strip()
                page.update()
            else: txt_conclusion.value = "INVALIDO"

        def limpiar_argumentos(e):
            chat.controls.clear()
            argumentos.value = ""
            conclu.value = ""
            txt_premisas.value = "Premisas: "
            txt_conclusion.value = "Conclusión: "
            listas_premisas.clear()
            page.update()

        argumentos.on_submit =  send_click #on_submit es para que se ejecute la función al presionar enter
        conclu.on_submit = send_conclusion

        fila_argumentos = ft.Row(
            controls = [argumentos, ft.ElevatedButton ("Send", on_click=send_click, icon=ft.Icons.SEND,)],
            alignment = ft.MainAxisAlignment.CENTER
        )
        fila_conclusion = ft.Row(
            controls = [conclu, ft.ElevatedButton("Send", on_click=send_conclusion, icon=ft.Icons.SEND,)],
            alignment = ft.MainAxisAlignment.CENTER
        )


        def insertar_simbolo(e):
            'agrega el texto del botón a campo de input actual'
            objetivo = campo["input_actual"]
            
            if objetivo:
                simbolo = e.control.data
                texto_actual = objetivo.value or ""
                objetivo.value = texto_actual + simbolo
                page.update()

            objetivo.focus()
        

        def validar_argumento(e):
            'conecta archivo truth_tables.py a GUI'
            try: # prueba todo el proceso de validación
                premises = listas_premisas
                conclusion = conclu.value.strip()
                
                # función de truth_tables.py
                valor, df, critical_index, ivalid_index = TV.generateTruthTable(premises, conclusion)

                filas = []

                for i, fila in df.iterrows():
                    color = None
                    if i in critical_index:
                        color = "#006400"
                    elif i in ivalid_index:
                        color = "#880808"
                    filas.append(ft.DataRow(
                        color = color,
                        cells = [
                            ft.DataCell(ft.Text(str(valor)))
                            for valor in fila]
                        ))

                # convierte dataframe en la datatable de flet (celda por celda)
                tabla_GUI = ft.DataTable( 
                    columns=[
                        ft.DataColumn(ft.Text(columna))
                        for columna in df.columns
                    ],
                    rows=filas
                )
                
                validez = ft.Text(f"El argumento es: {valor}",
                                size = 15,
                                text_align = ft.TextAlign.CENTER
                                )
            
                page.add(validez, ft.Column(controls=[tabla_GUI],
                                scroll=ft.ScrollMode.ALWAYS,
                                height=500,
                                expand=True,
                                ),)
                page.update()

            except Exception as ex: # Si sucede algún error que impida validar muestra un mensaje
                mensaje_ayuda(page, "Error",f"Error en algún input: {str(ex)}")
    

        b_ayuda = boton_ayuda(
            lambda e:mensaje_ayuda(page,
                                    "USO",
                                    "Requerimientos:\n" \
                                    "\tIngrese sus premisas y conclusión, luego haga click en 'send'\n" \
                                    "\tHaga click en 'validar'\n" \
                                    "Limitantes:\n" \
                                    "\tSi no se ingresan operadores no obtendrá una tabla válida\n" \
                                    "\tLos errores no indican claramente el problema con el input\n\n" \
                                    "OJO, CUIDA TU INPUT"
                                    ))
        b_teclado = teclado(["¬", "∧", "∨", "→", "↔", "(", ")"],insertar_simbolo,
                            limpiar_argumentos, "limpiar argumentos", "validar", validar_argumento)
        linea = divisor()
        b_reset = boton_reset(pag_argumentos, "eliminar tablas")
        b_volver = boton_volver(pag_inicio)

        # layout
        page.add(ft.Column(controls=[chat, fila_argumentos, fila_conclusion, b_teclado, linea, txt_premisas, txt_conclusion],
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            ),
            linea,
            ft.Row(controls=[b_reset, b_volver, b_ayuda],
                   alignment=ft.MainAxisAlignment.CENTER,
                   )
            )

# ------ PÁGINA DE TABLAS DE CONECTORES LÓGICOS ----------------------------------------------------------

    def pag_tablas(e=None):
        'acomodo pag de tablas'
        page.clean()

        # funciones de premade_tables.py
        t_not = preT.table_NOT()
        t_and = preT.table_AND()
        t_or = preT.table_OR()
        t_if = preT.table_CONDITIONAL()
        t_onlyif = preT.table_BICONDITIONAL()

        titulos = ["NEGACION", "CONJUNCION", "DISYUNCION", "CONDICIONAL", "BICONDICIONAL"]
        tablas = [t_not, t_and, t_or, t_if, t_onlyif]

        dict_titulos = dict(zip(titulos, tablas))

        # une tablas con su título
        titulos_tabla = []
        for t in dict_titulos:
            titulos_tabla.append(ft.Column([ft.Text(t, size=20), dict_titulos[t]],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        ))
            
        b_ayuda = boton_ayuda(
            lambda e:mensaje_ayuda(page,
                                    "INFORMACIÓN",
                                    "Las tablas de esta página son de los operadores" \
                                    "lógicos. Es la base de la lógica!\n" \
                                    "Usa este conocimiento sabiamente..."
                                    ))
        b_volver = boton_volver(pag_inicio)

        # layout
        page.add(ft.Row(controls=titulos_tabla, scroll=ft.ScrollMode.AUTO, spacing=50,),
                 ft.Row(controls=[b_volver, b_ayuda],
                   alignment=ft.MainAxisAlignment.CENTER,
                   ))

# ------ PÁGINA DE CALCULADORA DE PROPOSICIONES COMPUESTAS ----------------------------------------------------------

    def pag_calculadora(e=None):
        'acomodo pag calculadora'
        page.clean()
        page.scroll = ft.ScrollMode.AUTO

        campo = {"input_actual": None}
        def enfocar(e):
            campo["input_actual"] = e.control

        def calcular(e):
            'conecta archivo de shunting_yard.py con GUI'
            try: # prueba todo el proceso de calculo
                input = proposicion.value
                values = valores.value.split(",")
                
                shunt = log.shuntingYard(input)
                var_values = log.proposition_dict(shunt, values)
                boolShunt = log.applyBooleanValues(shunt, var_values)
                result = log.performCalculation(boolShunt)

                propo = ft.Text(f"Proposicion: {input}",
                                size = 15,
                                text_align = ft.TextAlign.CENTER
                                )
                resultado = ft.Text(f"Resultado: {result}\n",
                                size = 15,
                                text_align = ft.TextAlign.CENTER
                                )
                
                page.add(propo, resultado)

            except Exception as ex: # Si sucede algún error que impida validar muestra un mensaje
                mensaje_ayuda(page, "Error",f"Error en la premisa: {str(ex)}") 

        def insertar_simbolo(e):
            'agrega el texto del botón a campo actual'
            objetivo = campo["input_actual"]
            
            if objetivo:
                simbolo = e.control.data
                texto_actual = objetivo.value or ""
                objetivo.value = texto_actual + simbolo
                page.update()

            objetivo.focus()

        def limpiar_proposicion(e):
            proposicion.value = ""
            valores.value = ""
            page.update()
        
        proposicion = ft.TextField(label="Proposicion", hint_text="(p∨q)∧(¬r→s)", on_focus = enfocar, autofocus=True)
        valores = ft.TextField(label="Valores de las Variables", hint_text="true,false,true,false", on_focus = enfocar)
        
        b_ayuda = boton_ayuda(
            lambda e:mensaje_ayuda(page,
                                    "USO",
                                    "Requerimientos:\n" \
                                    "\tUse premisas válidas y con operadores lógicos\n" \
                                    "\tPara asignar valor de verdad use true/false y separe con comas\n" \
                                    "\tLos valores de verdad serán asignados en el orden\n" \
                                    "\tque se detecten las premisas (de izquierda a derecha)\n" \
                                    "Limitantes:\n" \
                                    "\tAl ingresar cualquier elemento, palabra o frase\n" \
                                    "\tno obtendrá un resultado correcto\n" \
                                    "\tSi no se ingresan valores de verdad no funciona la calculadora\n" \
                                    "\tNo se puede usar espacios en la asignación de valores\n\n" \
                                    "OJO, CUIDA TU INPUT"
                                    ))
        b_reset = boton_reset(pag_calculadora, "borrar\nreultados pasados")
        b_volver = boton_volver(pag_inicio)
        b_teclado = teclado(["0", "¬", "∧", "∨", "1", "→", "↔"], insertar_simbolo, limpiar_proposicion, "limpiar proposicion", "calcula", calcular)

        # layout
        page.add(proposicion, valores, b_teclado,
                 ft.Row(controls=[b_reset, b_volver, b_ayuda],
                   alignment=ft.MainAxisAlignment.CENTER,
                   )) 

    # inicializa página
    pag_inicio()
    page.update()

# ejemplo argumento:
# p→q,p∧r,¬q∨r
# r

ft.app(target=main)