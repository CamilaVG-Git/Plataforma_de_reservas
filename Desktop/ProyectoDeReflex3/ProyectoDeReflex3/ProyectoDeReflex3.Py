import reflex as rx

class Estado(rx.State):
    # El texto que cambiará al interactuar
    bienvenida: str = "¡Hola! Bienvenido a mi página."

    def actualizar_saludo(self):
        self.bienvenida = "¡El botón funciona! Gracias por visitar. ✨"

def index():
    return rx.center(
        rx.vstack(
            # 1. Título principal
            rx.heading("Mi Primera Página Web", size="9"),
            
            # 2. Texto de bienvenida 
            rx.text(Estado.bienvenida, font_size="1.5em"),
            
            # 3. Botón interactivo
            rx.button(
                "Presionar para interactuar", 
                on_click=Estado.actualizar_saludo,
                color_scheme="grass", # Un color 
                cursor="pointer"
            ),
            spacing="6",
            align="center",
        ),
        width="100%",
        height="100vh",
    )

app = rx.App()
app.add_page(index)