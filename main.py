import flet as ft

def main(page: ft.Page):
    # Configurações essenciais para evitar erros de renderização
    page.title = "Teste de Interface"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 15
    # O scroll deve estar na página ou em um container pai
    page.scroll = ft.ScrollMode.ADAPTIVE 

    # 1. Header Simples (Sem muitos elementos)
    header = ft.Text(
        "Painel de Controle",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_500
    )

    # 2. Elemento Gráfico: Barra de progresso (Visual e leve)
    # Isso ajuda a ver se a interface está "viva"
    progress_section = ft.Column([
        ft.Text("Capacidade do Sistema", size=14, color=ft.colors.GREY_400),
        ft.ProgressBar(value=0.6, color=ft.colors.BLUE_ACCENT, bgcolor=ft.colors.GREY_800),
    ], spacing=5)

    # 3. Card de Registro (Simplificado e com cores sólidas)
    # Evitamos sombras complexas no primeiro teste de APK
    def create_simple_card(titulo, status):
        return ft.Container(
            content=ft.ListTile(
                leading=ft.Icon(ft.icons.REORDER, color=ft.colors.BLUE_200),
                title=ft.Text(titulo, size=16, weight="bold"),
                subtitle=ft.Text(status, size=13, color=ft.colors.GREY_400),
                trailing=ft.Icon(ft.icons.CHEVRON_RIGHT),
            ),
            bgcolor=ft.colors.GREY_900,
            border_radius=10,
            border=ft.border.all(1, ft.colors.GREY_800),
            margin=ft.margin.only(bottom=10)
        )

    # Lista de elementos
    registros = ft.Column([
        create_simple_card("Registro de Entrada", "Processado"),
        create_simple_card("Configuração de Rede", "Ativo"),
        create_simple_card("Banco de Dados", "Sincronizado"),
    ])

    # Adicionando de forma limpa
    page.add(
        header,
        ft.Divider(height=20, color="transparent"),
        progress_section,
        ft.Divider(height=20, color="transparent"),
        ft.Text("Últimas Atividades", size=16, weight="w500"),
        registros
    )

    page.update()

# Importante para o build do Flet:
if __name__ == "__main__":
    ft.app(target=main)
