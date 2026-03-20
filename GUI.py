import flet as ft
import shunting_yard as log
import truth_tables as TV


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
                             weight = ft.FontWeight.BOLD,
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
                                      style=ft.ButtonStyle(text_style=ft.TextStyle(
                                             size=28,
                                             weight=ft.FontWeight.BOLD,
                                             ))
                                             )
        b_tablas = ft.IconButton(icon=ft.Icons.TABLE_CHART,
                                 icon_color=ft.Colors.BLACK,
                                 icon_size=80,
                                 bgcolor=ft.Colors.SECONDARY,
                                 on_click = pag_tablas,
                                 width=100, height=100,
                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
                                 )
        b_calculadora = ft.IconButton(icon=ft.Icons.CALCULATE,
                                      icon_color=ft.Colors.BLACK,
                                      icon_size=80,
                                      bgcolor=ft.Colors.SECONDARY,
                                      on_click = pag_calculadora,
                                      width=100, height=100,
                                      style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
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
        # p→q,p∧r,¬q∨r
        # r
        page.clean() #limpia pag

        #inputs
        argumentos = ft.TextField(label="argumentos", autofocus=True)
        conclu = ft.TextField(label="conclusion")

        #botones para simbolos
        def agregar_simbolo(e):
            'agrega el texto del botón a input de argumentos'
            argumentos.value += e.control.data #agrega el contenido 'data' de cada botón al textfield de 'argumentos'
            page.update()

        b_simbolos = ft.Row(
            controls=[
                ft.ElevatedButton("¬", data="¬", on_click=agregar_simbolo),
                ft.ElevatedButton("∧", data="∧", on_click=agregar_simbolo),
                ft.ElevatedButton("∨", data="∨",on_click=agregar_simbolo),
                ft.ElevatedButton("→", data="→", on_click=agregar_simbolo),
                ft.ElevatedButton("↔", data="↔", on_click=agregar_simbolo)
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                #spacing = 10
                )
        

        def validar_argumento(e):
            'conecta archivo truth_tables.py a GUI'

            #capta lo de los input (+ hace una lista separada por las comas del input)
            premises = argumentos.value.split(",")
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
                               scroll=ft.ScrollMode.AUTO))
            page.update()

        # botones para usar funciones
        b_volver = ft.ElevatedButton("← volver", on_click = pag_inicio)
        b_validar = ft.ElevatedButton("validar", on_click = validar_argumento)

        #agregar todas las variables (botones) a la pag. Todavía no están los inputs
        page.add(argumentos, b_simbolos, conclu, b_validar, b_volver)


    # Acomodar página tablas
    def pag_tablas(e=None):
        page.clean()

        #agrega tabla de prueba
        page.add(
        ft.DataTable( 
            columns=[ #títulos de columnas
                ft.DataColumn(ft.Text("P")),
                ft.DataColumn(ft.Text("Q")),
                ft.DataColumn(ft.Text("P ∧ Q")),
            ],
            rows=[ #lineas creadas celda por celda
                ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T"))]),
                ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F"))]),
                ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F"))]),
                ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F"))]),
            ],
        )
    )
        # boton para volver a pag inicial
        b_volver = ft.ElevatedButton("← volver", on_click = pag_inicio)

        page.add(b_volver)

    #Pagina de calculadora. Prueba para conectar lógica con GUI usando flet
    def pag_calculadora(e=None):
        page.clean()

        def calcular():
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
        
        proposicion = ft.TextField(label="Proposicion")
        valores = ft.TextField(label="Valores de las Variables")
        b_volver = ft.ElevatedButton("← volver", on_click = pag_inicio)
        b_calcular = ft.ElevatedButton("calcular", on_click = calcular)

        page.add(proposicion, valores, b_calcular, b_volver)

    pag_inicio()
    #page.update() <- esto era para eventos

ft.app(target=main)