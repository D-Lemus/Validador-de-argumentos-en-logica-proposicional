import flet as ft
"""import truth_tables as tb"""

def main(page: ft.Page):
    "AB"
    page.title = "Validador de Argumentos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 500
    page.window.width = 700
    page.theme_mode = ft.ThemeMode.DARK

    def pag_inicio():
        page.clean()
        bienvenida = ft.Text("BIENVENIDX!",
                             size = 30,
                             weight = ft.FontWeight.BOLD,
                             text_align = ft.TextAlign.CENTER
                             )
        subsaludo = ft.Text("a tu validador de argumentos",
                            size = 15,
                            text_align = ft.TextAlign.CENTER
                            )
        b_empezar = ft.ElevatedButton("empezar", on_click = lambda e: pag_argumentos())
        b_tablas = ft.ElevatedButton("tablas", on_click = lambda e: pag_tablas())
        b_calculadora = ft.ElevatedButton("calculadora", on_click = lambda e: pag_calculadora())

        page.add(
            ft.Column(
                [bienvenida, subsaludo, b_empezar, 
                 ft.Row(
                     [b_tablas, b_calculadora],
                     alignment = ft.MainAxisAlignment.CENTER)
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER
            )
        )
      
    def pag_argumentos():
        page.clean()
        chat = ft.Column()
        argumento = ft.TextField(label="argumento",
                                 on_submit = lambda e: send_click(e)) #on_submit es para que se ejecute la función al presionar enter
        conclusion = ft.TextField(label="conclusion",
                                  on_submit = lambda e: send_click(e)) #on_submit es para que se ejecute la función al presionar enter

        def send_click(e):
            chat.controls.append(ft.Text(argumento.value))
            argumento.value = ""
            chat.controls.append(ft.Text(conclusion.value))
            conclusion.value = ""

        page.add(
            chat,
            ft.Row(controls = [ argumento,
                                ft.Button("Send", on_click = send_click) ],
                                alignment= ft.MainAxisAlignment.CENTER ),
            ft.Row(controls = [ conclusion,
                               ft.Button("Send", on_click = send_click) ],
                               alignment= ft.MainAxisAlignment.CENTER )
        )

        b_volver = ft.Button("Volver", on_click = lambda e: pag_inicio())

        page.add( b_volver)


    def pag_tablas():
        page.clean()

        page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("P")),
                ft.DataColumn(ft.Text("Q")),
                ft.DataColumn(ft.Text("P ∧ Q")),
            ],
            rows=[
                ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T"))]),
                ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F"))]),
                ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F"))]),
                ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F"))]),
            ],
        )
    )
        b_volver = ft.ElevatedButton("Volver", on_click = lambda e: pag_inicio())

        page.add(b_volver)

    def pag_calculadora():
        
        page.clean()

        proposicion = ft.TextField(label="proposicion")
        b_volver = ft.ElevatedButton("Volver", on_click = lambda e: pag_inicio())

        page.add(proposicion, b_volver)

        """def calcular():
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

        b_prueba = ft.ElevatedButton("calcular", on_click = lambda e: calcular())
        
        page.add(b_prueba)"""

    pag_inicio()

    #page.update()

ft.app(target=main)
