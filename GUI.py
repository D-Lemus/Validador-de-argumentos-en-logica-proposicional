import flet as ft
import shunting_yard as log
import truth_tables as TV


# Iniciar Ventana
def main(page: ft.Page):
    'abre ventana'
    page.title = "Validador de Argumentos" #título de la pag

    #alinear y dar tamaño a la pag en el monitor
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 700
    page.window.width = 600
    #page.theme_mode = ft.ThemeMode.DARK


    def pag_inicio(e=None):
        'acomodo de pag inicio'
        page.clean() #limpia todo lo que haya antes en la pag

        #variables para textos simples (con tamaño, negritas y alineación)
        bienvenida = ft.Text("BIENVENIDX!",
                             size = 30,
                             weight = ft.FontWeight.BOLD,
                             text_align = ft.TextAlign.CENTER
                             )
        subsaludo = ft.Text("a tu validador de argumentos",
                            size = 15,
                            text_align = ft.TextAlign.CENTER
                            )
        
        #variables para botones con sombra ("texto dentro del botón", evento = función)
        b_empezar = ft.ElevatedButton("empezar", on_click = pag_argumentos)
        b_tablas = ft.ElevatedButton("tablas", on_click = pag_tablas)
        b_calculadora = ft.ElevatedButton("calculadora", on_click = pag_calculadora)

        #agregar todas las variables (texto y botones) a la pag
        page.add(bienvenida, subsaludo, b_empezar, b_tablas, b_calculadora)
            

    def pag_argumentos(e=None):
        'acomodo pag de argumentos'
        # p→q,p∧r,¬q∨r
        # r
        page.clean() #limpia pag

        #inputs
        argumentos = ft.TextField(label="argumentos")
        conclu = ft.TextField(label="conclusion")

        #botones para simbolos
        """def agregar_simbolo(e):
            'agrega el texto del botón a input de argumentos'
            argumentos.value += e.control.text
            page.update()

        b_simbolos = ft.Row(
            controls=[
                ft.ElevatedButton("¬", on_click=agregar_simbolo),
                ft.ElevatedButton("∧", on_click=agregar_simbolo),
                ft.ElevatedButton("∨", on_click=agregar_simbolo),
                ft.ElevatedButton("→", on_click=agregar_simbolo),
                ft.ElevatedButton("↔", on_click=agregar_simbolo)
                ]
                )"""
        

        def validar_argumento(e):
            'conecta archivo truth_tables.py a GUI'

            #capta lo de los input (+ hace una lista separada por las comas del input)
            premises = argumentos.value.split(",")
            conclusion = conclu.value.strip()

            #usa función de truth_tables.py. Todavía no funciona 
            valor, df = TV.generateTruthTable(premises, conclusion)

            #debug: print(valor, df)

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
        b_volver = ft.ElevatedButton("Volver", on_click = pag_inicio)
        b_validar = ft.ElevatedButton("validar", on_click = validar_argumento)

        #agregar todas las variables (botones) a la pag. Todavía no están los inputs
        page.add(argumentos, conclu, b_validar, b_volver)


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
        b_volver = ft.ElevatedButton("Volver", on_click = pag_inicio)

        page.add(b_volver)

    #Pagina de calculadora. Prueba para conectar lógica con GUI usando flet
    def pag_calculadora(e=None):
        page.clean()

        proposicion = ft.TextField(label="proposicion")
        b_volver = ft.ElevatedButton("Volver", on_click = pag_inicio)

        page.add(proposicion, b_volver)

        def calcular():
            input = proposicion.value
            paso1 = ft.Text(f"Input: {input}\n",
                            size = 15,
                            text_align = ft.TextAlign.CENTER
                            )
            #print(f"Input: {input}\n")
            shunt = log.shuntingYard(input)
            boolShunt = log.applyBooleanValues(shunt)
            result = log.performCalculation(boolShunt)
            paso2 = ft.Text(f"Resultado: {result}\n",
                            size = 15,
                            text_align = ft.TextAlign.CENTER
                            )
            page.add(paso1, paso2)
            #print(f"Resultado: {result}\n")

        b_prueba = ft.ElevatedButton("calcular", on_click = calcular)
        page.add(b_prueba)

    pag_inicio()
    #page.update() <- esto era para eventos

ft.app(target=main)