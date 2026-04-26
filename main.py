import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Usando componentes básicos para garantir o carregamento
    page.add(
        ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, color=ft.colors.GREEN, size=50),
        ft.Text("App Carregado com Sucesso!", size=20, weight="bold"),
        ft.Text("A interface moderna está pronta para os testes.", color=ft.colors.GREY_400)
    )
    page.update()

if __name__ == "__main__":
    # O parâmetro view é essencial para alguns ambientes mobile
    ft.app(target=main)
