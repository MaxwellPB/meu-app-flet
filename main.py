import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.spacing = 20

    # 1. Elemento Gráfico: Header com Avatar e Saudação
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column([
                    ft.Text("Olá, Desenvolvedor!", size=24, weight="bold", color="white"),
                    ft.Text("Confira o status dos seus registros hoje.", size=14, color="grey"),
                ], expand=True),
                ft.CircleAvatar(
                    content=ft.Icon(ft.icons.PERSON),
                    bgcolor=ft.colors.BLUE_700,
                    radius=25,
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        margin=ft.margin.only(bottom=10)
    )

    # 2. Elemento Gráfico: Mini Dashboard (Indicadores)
    stats_row = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.AUTO_GRAPH, color=ft.colors.GREEN_400),
                    ft.Text("Atividade", size=12),
                    ft.Text("85%", size=18, weight="bold")
                ]),
                padding=15,
                bgcolor=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                border_radius=15,
                expand=True
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.LAYERS, color=ft.colors.BLUE_400),
                    ft.Text("Registros", size=12),
                    ft.Text("124", size=18, weight="bold")
                ]),
                padding=15,
                bgcolor=ft.colors.with_opacity(0.1, ft.colors.WHITE),
                border_radius=15,
                expand=True
            ),
        ],
        spacing=15
    )

    # 3. Card de Registro Refinado (Sem retângulos pesados)
    def create_card(titulo, subtitulo):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    width=5, height=40, bgcolor=ft.colors.BLUE_ACCENT, border_radius=10
                ),
                ft.Column([
                    ft.Text(titulo, weight="bold", size=16),
                    ft.Text(subtitulo, size=13, color="grey"),
                ], tight=True, expand=True),
                ft.IconButton(icon=ft.icons.MORE_VERT, icon_color="grey")
            ]),
            padding=15,
            bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=12,
            # Sombra suave para profundidade
            shadow=ft.BoxShadow(
                spread_radius=1, blur_radius=10, 
                color=ft.colors.with_opacity(0.2, ft.colors.BLACK)
            )
        )

    # Lista de Registros
    lista_registros = ft.Column(
        controls=[
            create_card("Relatório Mensal", "Atualizado há 2 horas"),
            create_card("Backup de Dados", "Concluído com sucesso"),
            create_card("Configurações de UI", "Pendente de revisão"),
        ],
        spacing=10,
        scroll=ft.ScrollMode.ADAPTIVE # Garante que não corte no mobile
    )

    # Adicionando tudo à página
    page.add(
        header,
        stats_row,
        ft.Text("Registros Recentes", size=18, weight="w600", margin=ft.margin.only(top=10)),
        lista_registros
    )

ft.app(target=main)

