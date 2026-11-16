import flet as ft

def main(page: ft.Page):
    page.title = "Edufort International School (EPS)"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    # Replace with your actual live cPanel portal login URL
    portal_url = "https://edufortschools.com/epsportal/login.php"

    # UI Design
    page.add(
        ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=["#1e1b4b", "#312e81"], # Deep indigo matching your web portal
            ),
            expand=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("EDUFORT", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text("International School Portal", size=16, color=ft.Colors.INDIGO_200),
                    ft.Container(height=30),
                    
                    ft.Button(
                        content="Access Portal Login",
                        icon=ft.Icons.LOGIN_ROUNDED,
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.INDIGO_600,
                        style=ft.ButtonStyle(
                            padding=ft.Padding.symmetric(horizontal=30, vertical=20),
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        # FIXED: Removed on_click and replaced with the native Flet 1.0+ action launcher
                        action=ft.OpenUrl(portal_url, target=ft.UrlTarget.BLANK),
                    ),
                    
                    ft.Container(height=20),
                    ft.Text("Tap above to open the secure school portal", size=12, color=ft.Colors.WHITE),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main)
