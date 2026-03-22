import flet as ft

def table_AND():
    return ft.DataTable(
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
    
def table_OR():
    return ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("P")),
                    ft.DataColumn(ft.Text("Q")),
                    ft.DataColumn(ft.Text("P ∨ Q")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("T"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F"))]),
                ],
            )
    
def table_NOT():
    return ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("P")),
                    ft.DataColumn(ft.Text("¬P")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F"))]),
                ],
            )
    
def table_CONDITIONAL():
    return ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("P")),
                    ft.DataColumn(ft.Text("Q")),
                    ft.DataColumn(ft.Text("P → Q")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("T"))]),
                ],
            )
    
def table_BICONDITIONAL():
    return ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("P")),
                    ft.DataColumn(ft.Text("Q")),
                    ft.DataColumn(ft.Text("P ↔ Q")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("T"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("T")), ft.DataCell(ft.Text("F"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("F")), ft.DataCell(ft.Text("T"))]),
                ],
            )