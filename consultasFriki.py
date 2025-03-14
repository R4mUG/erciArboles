import flet as ft
import juegosddbb

def main(page: ft.Page):
    page.title = "Consultas"

    # Consultar y cargar todos los arboles
    def consultar_juegos():
        juegos = juegosddbb.consultar_juegos() # Esto son los datos
        cargar_tabla(juegos)
        page.update()


    # Datos es la lista de arboles
    def cargar_tabla(datos):
        tabla.rows = []
        for fila in datos:
            tabla.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))), #ID
                ft.DataCell(ft.Text((fila[1]))), #Empresa
                ft.DataCell(ft.Text((fila[2]))), #Nombre
                ft.DataCell(ft.Text((fila[3]))), #Tipo
                ft.DataCell(ft.Text(str(fila[4]))), #Precio
            ]))

    def buscar_juegos(e):
        lista_juegos = juegosddbb.consultar_juegos_por_empresa(empresa_tf.value)
        cargar_tabla(lista_juegos)
        page.update()

    #OBJETOS
    empresa_tf = ft.TextField(label="Empresa", width=300)
    buscar_btn = ft.ElevatedButton("Buscar", width=300, on_click=buscar_juegos)
    tabla = ft.DataTable(bgcolor="green",
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Empresa")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Precio")),
        ]
    )


    columna_datos = ft.Column(
        controls=[
            ft.Text("CONSULTAS", size=40),
            empresa_tf,
            buscar_btn,
            tabla
        ]
    )


    page.add(columna_datos)
    consultar_juegos()


if __name__ == '__main__':
    ft.app(target=main)