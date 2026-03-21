import flet as ft
import shunting_yard as log
import truth_tables as TV
import premade_tables as preT


# Iniciar Ventana
def main(page: ft.Page):
    'abre ventana'
    page.title = "Validador de Argumentos" #título de la pag

    #alinear y dar tamaño a la pag
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
        
        #fondo interactivo
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
        
        ##franja = ft.Container(content=grid, height=180)

        overlay = ft.Container(
            width=500,
            height=4000,
            bgcolor="#010101FF",
            alignment=ft.Alignment.CENTER,
            ignore_interactions=True
            )

        #variables para textos simples (con tamaño, negritas y alineación)
        bienvenida = ft.Text("BIENVENIDX",
                             size = 60,
                             weight = "bold",
                             text_align = ft.TextAlign.CENTER,
                             )
        subsaludo = ft.Text("validador de argumentos",
                            size = 25,
                            text_align = ft.TextAlign.CENTER,
                            )
        
        #variables para botones con sombra ("texto dentro del botón", evento = función)
        b_empezar = ft.ElevatedButton("empezar!",
                                      on_click = pag_argumentos,
                                      width=200, height=90,
                                      style=ft.ButtonStyle(text_style=ft.TextStyle(size=28,weight="bold",)),
                                      tooltip="tip",
                                             )
        b_tablas = ft.IconButton(icon=ft.Icons.TABLE_CHART,
                                 icon_color=ft.Colors.BLACK,
                                 icon_size=80,
                                 bgcolor=ft.Colors.SECONDARY,
                                 on_click = pag_tablas,
                                 width=100, height=100,
                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
                                 tooltip="tablas de operadores lógicos",
                                 )
        b_calculadora = ft.IconButton(icon=ft.Icons.CALCULATE,
                                      icon_color=ft.Colors.BLACK,
                                      icon_size=80,
                                      bgcolor=ft.Colors.SECONDARY,
                                      on_click = pag_calculadora,
                                      width=100, height=100,
                                      style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
                                      tooltip="calculadora de proposiciones compuestas"
                                      )
        b_extras = ft.Row(controls=[b_tablas, b_calculadora],
                          alignment=ft.MainAxisAlignment.CENTER, spacing=30,
                          )
        #agregar todas las variables (texto y botones) a la pag
        contenido = (ft.Column(
            controls=[bienvenida, b_empezar, subsaludo, ft.Container(height=40), b_extras],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            ))
        page.add(ft.Stack([grid, overlay, contenido],expand=True))
            

    def pag_argumentos(e=None):
        'acomodo pag de argumentos'
        page.clean()
        page.scroll = ft.ScrollMode.AUTO

        #Para insertar simbolos en ambos input
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
                            hint_text="(p∨q)∧(¬r→s)",
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
            'agrega el texto del botón a campo actual'
            objetivo = campo["input_actual"]
            
            if objetivo:
                simbolo = e.control.data
                texto_actual = objetivo.value or ""
                objetivo.value = texto_actual + simbolo
                page.update()

            objetivo.focus()
        

        def validar_argumento(e):
            'conecta archivo truth_tables.py a GUI'

            premises = listas_premisas
            conclusion = conclu.value.strip()
            
            #usa función de truth_tables.py. Todavía no funciona 
            valor, df = TV.generateTruthTable(premises, conclusion)

            # debug -> print(valor, df)

            tabla_GUI = ft.DataTable( 
                columns=[
                    ft.DataColumn(ft.Text(columna))
                    for columna in df.columns
                ],
                rows=[
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text(str(valor)))
                        for valor in fila])
                        for _, fila in df.iterrows()]
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


        divisor = ft.Divider(color=ft.Colors.PRIMARY, thickness=2)
        b_reset = ft.ElevatedButton("reset", on_click = pag_argumentos,icon=ft.Icons.RESTART_ALT,
                                    tooltip="eliminar tablas")
        b_volver = ft.ElevatedButton("← volver", on_click = pag_inicio)
        b_limpiar = ft.IconButton(icon=ft.Icons.CLEANING_SERVICES,
                                  icon_color=ft.Colors.BLACK,
                                  icon_size=40,
                                  bgcolor=ft.Colors.SECONDARY,
                                  width=20, height=20,
                                  style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                                  on_click = limpiar_argumentos,
                                  tooltip="limpiar argumentos"
                                  )
        b_validar = ft.ElevatedButton("validar", on_click = validar_argumento,
                                    icon=ft.Icons.CHECK_CIRCLE,
                                    width=120, height=120,
                                    style=ft.ButtonStyle(
                                    text_style=ft.TextStyle(
                                    size=15,
                                    weight="bold",
                                    ),
                                    shape=ft.RoundedRectangleBorder(radius=10),),
                                    )
        b_no = ft.ElevatedButton("¬", data="¬", on_click=insertar_simbolo, autofocus=False, 
                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),
                                                      text_style=ft.TextStyle(size=20,
                                                                              weight="bold"),),)
        b_y = ft.ElevatedButton("∧", data="∧", on_click=insertar_simbolo, autofocus=False, 
                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),
                                                      text_style=ft.TextStyle(size=20,weight="bold"),))
        b_o = ft.ElevatedButton("∨", data="∨",on_click=insertar_simbolo, autofocus=False, 
                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),
                                                      text_style=ft.TextStyle(size=20,weight="bold"),),)
        b_con = ft.ElevatedButton("→", data="→", on_click=insertar_simbolo, autofocus=False, 
                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),
                                                      text_style=ft.TextStyle(size=20,weight="bold"),),)
        b_bicon = ft.ElevatedButton("↔", data="↔", on_click=insertar_simbolo, autofocus=False, 
                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),
                                                      text_style=ft.TextStyle(size=20,),),)

        teclado = ft.GridView(
            controls=[b_no, b_y, b_o, b_con, b_bicon, b_limpiar,],
            runs_count=3,
            spacing=10,
            run_spacing=10,
            child_aspect_ratio=1.0,
            width=200,
            height=150,
        )

        b_simbolos = ft.Row(controls=[teclado, b_validar],
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing=100)

        #agregar todas las variables (botones) a la pag. Todavía no están los inputs
        page.add(ft.Column(controls=[chat, fila_argumentos, fila_conclusion, b_simbolos, divisor, txt_premisas, txt_conclusion],
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            ),
            divisor,
            ft.Row(controls=[b_reset, b_volver,],
                   alignment=ft.MainAxisAlignment.CENTER,
                   )
            )


    # Acomodar página tablas
    def pag_tablas(e=None):
        page.clean()

        t_not = preT.table_NOT()
        t_and = preT.table_AND()
        t_or = preT.table_OR()
        t_if = preT.table_CONDITIONAL()
        t_onlyif = preT.table_BICONDITIONAL()


        b_volver = ft.ElevatedButton("← volver", on_click = pag_inicio)

        page.add(ft.Row(
            controls=[
                ft.Column([ft.Text("NEGACION", size=20), t_not],
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=10,
                          ),
                ft.Column([ft.Text("CONJUNCION", size=20), t_and],
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=10,),
                ft.Column([ft.Text("DISYUNCION", size=20), t_or],
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=10,),
                ft.Column([ft.Text("CONDICIONAL", size=20), t_if],
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=10,),
                ft.Column([ft.Text("BICONDICIONAL", size=20), t_onlyif],
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=10,),
                ],
                scroll=ft.ScrollMode.AUTO,
                spacing=50,
            ))
        page.add(b_volver)

    #Pagina de calculadora. Prueba para conectar lógica con GUI usando flet
    def pag_calculadora(e=None):
        page.clean()

        def calcular(e):
            input = proposicion.value
            values = valores.value.split(",")
            propo = ft.Text(f"Proposicion: {input}",
                            size = 15,
                            text_align = ft.TextAlign.CENTER
                            )
            shunt = log.shuntingYard(input)
            var_values = log.proposition_dict(shunt, values)
            boolShunt = log.applyBooleanValues(shunt, var_values)
            result = log.performCalculation(boolShunt)

            resultado = ft.Text(f"Resultado: {result}\n",
                            size = 15,
                            text_align = ft.TextAlign.CENTER
                            )
            page.add(propo, resultado)
            #print(f"Resultado: {result}\n")
        
        proposicion = ft.TextField(label="Proposicion", hint_text="(p∨q)∧(¬r→s)")
        valores = ft.TextField(label="Valores de las Variables", hint_text="true,false,true,false")
        b_volver = ft.ElevatedButton("← volver", on_click = pag_inicio)
        b_calcular = ft.ElevatedButton("calcular", on_click = calcular)

        page.add(proposicion, valores, b_calcular, b_volver)

    pag_inicio()
    #page.update() <- esto era para eventos

# p→q,p∧r,¬q∨r
# r

ft.app(target=main)

