import reflex as rx

AZUL        = "#1565C0"
AZUL_MEDIO  = "#1976D2"
AZUL_CLARO  = "#E3F2FD"
AZUL_BORDE  = "#90CAF9"
GRIS        = "#546E7A"
GRIS_OSCURO = "#263238"
BLANCO      = "#ffffff"
ROJO        = "#E53935"
VERDE       = "#2E7D32"
FONDO       = "#F5F9FF"


# ── Datos de los tours ───────────────────────
TOURS = [
    {
        "nombre": "Isla Saona 🏝️",
        "descripcion": "Catamarán, snorkel y almuerzo incluido. ¡Un día increíble!",
        "precio": "US$50 / persona",
        "imagen": "/isla_saona.jpg",
        "href": "/descripcion/saona",
        "tags": ["saona", "isla", "snorkel", "catamarán", "playa"],
    },
    {
        "nombre": "Los Haitises 🦜",
        "descripcion": "Tour ecológico por manglares, cuevas y aves del Parque Nacional.",
        "precio": "US$40 / persona",
        "imagen": "/los_haitises.jpg",
        "href": "/descripcion/haitises",
        "tags": ["haitises", "ecológico", "manglar", "cuevas", "naturaleza"],
    },
    {
        "nombre": "Punta Cana 🌿",
        "descripcion": "Buggy, tirolesas y cenote en la selva tropical.",
        "precio": "US$65 / persona",
        "imagen": "/punta_cana.jpg",
        "href": "/descripcion/puntacana",
        "tags": ["punta cana", "aventura", "buggy", "tirolesa", "cenote"],
    },
]


# ── State ────────────────────────────────────
class BuscadorState(rx.State):
    busqueda: str = ""

    def set_busqueda(self, valor: str):
        self.busqueda = valor.lower()

    @rx.var
    def tours_filtrados(self) -> list[dict]:
        if self.busqueda.strip() == "":
            return TOURS
        return [
            t for t in TOURS
            if self.busqueda in t["nombre"].lower()
            or self.busqueda in t["descripcion"].lower()
            or any(self.busqueda in tag for tag in t["tags"])
        ]


# ── Navbar ───────────────────────────────────
def navbar():
    return rx.hstack(
        rx.heading("🌴 TuReserva", size="5", color=BLANCO),
        rx.spacer(),
        rx.link("Inicio",   href="/",        color=BLANCO, margin_right="15px"),
        rx.link("Reservas", href="/reservas", color=BLANCO),
        width="100%",
        padding="15px 20px",
        background=AZUL,
    )


# ── Tarjeta de oferta ────────────────────────
def oferta_card(tour: dict):
    return rx.box(
        rx.image(src=tour["imagen"], width="100%", height="160px", object_fit="cover"),
        rx.box(
            rx.heading(tour["nombre"], size="4", color=GRIS_OSCURO),
            rx.text(tour["descripcion"], color=GRIS, font_size="14px", margin_y="6px"),
            rx.text(tour["precio"], color=ROJO, font_size="17px", font_weight="bold"),
            rx.link(
                rx.button("Ver más", background=AZUL, color=BLANCO, margin_top="8px"),
                href=tour["href"],
            ),
            padding="12px",
        ),
        border="2px solid " + AZUL_BORDE,
        border_radius="6px",
        background=BLANCO,
        width="270px",
        overflow="hidden",
        margin="10px",
    )


# ── Página de Inicio ─────────────────────────
def home():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("¡Bienvenido a TuReserva! 🎉", size="7", color=BLANCO),
                rx.text(
                    "Las mejores ofertas turísticas de República Dominicana",
                    color="#BBDEFB",
                    font_size="16px",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="¿A dónde quieres ir?",
                        width="250px",
                        background=BLANCO,
                        on_change=BuscadorState.set_busqueda,
                    ),
                    rx.button(
                        "Buscar 🔍",
                        background=VERDE,
                        color=BLANCO,
                        on_click=BuscadorState.set_busqueda(BuscadorState.busqueda),
                    ),
                    margin_top="10px",
                ),
                align="center",
                spacing="3",
            ),
            width="100%",
            padding="50px 20px",
            background=AZUL,
        ),
        rx.divider(),
        rx.center(
            rx.vstack(
                rx.heading("🏖️ Nuestros Tours", size="6", color=GRIS_OSCURO),
                rx.text("¡Elige tu aventura favorita!", color=GRIS, margin_bottom="10px"),

                # Resultado de búsqueda o mensaje vacío
                rx.cond(
                    BuscadorState.tours_filtrados.length() == 0,
                    rx.box(
                        rx.text(
                            "😅 No encontramos tours con ese nombre. ¡Intenta con otra búsqueda!",
                            color=GRIS,
                            font_size="15px",
                        ),
                        padding="20px",
                    ),
                    rx.hstack(
                        rx.foreach(BuscadorState.tours_filtrados, oferta_card),
                        flex_wrap="wrap",
                        justify="center",
                    ),
                ),

                align="center",
                width="100%",
            ),
            width="100%",
            padding="30px 20px",
            background=FONDO,
        ),
        rx.divider(),
        rx.center(
            rx.vstack(
                rx.heading("📬 Contáctanos", size="5", color=GRIS_OSCURO),
                rx.box(
                    rx.text("📧 info@tureserva.com",                         color=GRIS_OSCURO),
                    rx.text("📞 (809) 555-1234",                              color=GRIS_OSCURO),
                    rx.text("📍 Higüey, La Altagracia, República Dominicana", color=GRIS_OSCURO),
                    rx.text("🕐 Lunes a Domingo, 8:00 AM – 8:00 PM",         color=GRIS_OSCURO),
                    background=BLANCO,
                    border="1px solid " + AZUL_BORDE,
                    border_radius="6px",
                    padding="15px 20px",
                    max_width="400px",
                ),
                align="center",
                spacing="3",
            ),
            width="100%",
            padding="30px 20px",
            background=AZUL_CLARO,
        ),
        rx.center(
            rx.text(
                "© 2025 TuReserva — Hecho con ❤️ en República Dominicana",
                color=BLANCO,
                font_size="13px",
            ),
            width="100%",
            padding="15px",
            background=AZUL,
        ),
        background=FONDO,
    )


# ── Páginas de descripción ───────────────────
def pagina_descripcion(titulo, subtitulo, imagen, detalles, descripcion_texto, itinerario):
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.link("← Volver al inicio", href="/", color=AZUL_MEDIO, font_size="14px"),
                rx.divider(margin_y="15px"),
                rx.heading(titulo, size="7", color=GRIS_OSCURO),
                rx.text(subtitulo, color=GRIS, margin_bottom="15px"),
                rx.image(
                    src=imagen,
                    width="100%",
                    max_width="650px",
                    height="300px",
                    object_fit="cover",
                    border_radius="6px",
                    border="2px solid " + AZUL_BORDE,
                    margin_bottom="20px",
                ),
                rx.heading("¿Qué incluye?", size="5", color=GRIS_OSCURO, margin_bottom="10px"),
                rx.box(
                    *[rx.text(d, color=GRIS_OSCURO) for d in detalles],
                    background=AZUL_CLARO,
                    border="1px solid " + AZUL_BORDE,
                    border_radius="6px",
                    padding="15px",
                    width="100%",
                    max_width="500px",
                    margin_bottom="20px",
                ),
                rx.heading("Descripción", size="5", color=GRIS_OSCURO, margin_bottom="10px"),
                rx.text(
                    descripcion_texto,
                    color=GRIS,
                    max_width="650px",
                    line_height="1.7",
                    margin_bottom="20px",
                ),
                rx.heading("Itinerario del día", size="5", color=GRIS_OSCURO, margin_bottom="10px"),
                rx.box(
                    *[rx.text(i, color=GRIS_OSCURO) for i in itinerario],
                    border="1px solid " + AZUL_BORDE,
                    border_radius="6px",
                    padding="15px",
                    width="100%",
                    max_width="500px",
                    margin_bottom="25px",
                ),
                rx.hstack(
                    rx.link(rx.button("← Volver", variant="outline"), href="/"),
                    rx.link(
                        rx.button("¡Reservar ahora! 🎉", background=VERDE, color=BLANCO),
                        href="/reservas",
                    ),
                    spacing="3",
                ),
                align="center",
                width="100%",
                max_width="700px",
                padding="25px 20px",
            ),
            width="100%",
        ),
        background=FONDO,
    )


def desc_saona():
    return pagina_descripcion(
        titulo="🏝️ Isla Saona",
        subtitulo="Excursión de día completo",
        imagen="/isla_saona.jpg",
        detalles=[
            "✅ Duración: 8 horas",
            "✅ Grupo máximo: 20 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Almuerzo caribeño",
            "✅ Equipo de snorkel",
            "✅ Guía bilingüe (español / inglés)",
            "💵 Precio: US$50 por persona",
        ],
        descripcion_texto=(
            "La Isla Saona es una de las joyas naturales de la República Dominicana. "
            "Ubicada en el extremo sureste del país, es conocida por sus playas de arena blanca, "
            "aguas cristalinas y una flora y fauna únicas. ¡No te lo puedes perder!"
        ),
        itinerario=[
            "🕗 08:00 AM — Recogida en el hotel",
            "🚢 09:30 AM — Abordaje del catamarán",
            "🤿 10:30 AM — Parada de snorkel",
            "🍽️ 12:00 PM — Llegada a Isla Saona y almuerzo",
            "🏃 03:00 PM — Regreso en lancha rápida",
            "🏨 04:30 PM — Llegada al hotel",
        ],
    )


def desc_haitises():
    return pagina_descripcion(
        titulo="🦜 Los Haitises",
        subtitulo="Tour ecológico por el Parque Nacional",
        imagen="/los_haitises.jpg",
        detalles=[
            "✅ Duración: 7 horas",
            "✅ Grupo máximo: 15 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Recorrido en lancha por manglares",
            "✅ Visita a cuevas con pinturas taínas",
            "✅ Guía bilingüe (español / inglés)",
            "💵 Precio: US$40 por persona",
        ],
        descripcion_texto=(
            "El Parque Nacional Los Haitises es un paraíso ecológico al noreste de República Dominicana. "
            "Sus manglares, cuevas con arte rupestre taíno y una increíble variedad de aves lo hacen "
            "uno de los destinos más especiales del Caribe. ¡Una experiencia única en la naturaleza!"
        ),
        itinerario=[
            "🕗 07:30 AM — Recogida en el hotel",
            "🚌 09:00 AM — Llegada al embarcadero",
            "🚤 09:30 AM — Recorrido por manglares en lancha",
            "🗿 11:00 AM — Visita a cuevas taínas",
            "🍽️ 12:30 PM — Almuerzo en restaurante local",
            "🏨 02:30 PM — Regreso al hotel",
        ],
    )


def desc_puntacana():
    return pagina_descripcion(
        titulo="🌿 Punta Cana Aventura",
        subtitulo="Buggy, tirolesas y cenote en la selva",
        imagen="/punta_cana.jpg",
        detalles=[
            "✅ Duración: 6 horas",
            "✅ Grupo máximo: 25 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Recorrido en buggy por la selva",
            "✅ Tirolesas y cenote natural",
            "✅ Guías expertos certificados",
            "💵 Precio: US$65 por persona",
        ],
        descripcion_texto=(
            "Una aventura llena de adrenalina en la selva tropical de Punta Cana. "
            "Conduce tu propio buggy por caminos de tierra, vuela en tirolesas entre los árboles "
            "y refréscate en un cenote natural. ¡La experiencia perfecta para los amantes de la aventura!"
        ),
        itinerario=[
            "🕘 09:00 AM — Recogida en el hotel",
            "🏁 10:00 AM — Bienvenida y briefing de seguridad",
            "🚙 10:30 AM — Recorrido en buggy por la selva",
            "🪂 12:00 PM — Tirolesas",
            "💧 01:00 PM — Baño en cenote natural",
            "🏨 03:00 PM — Regreso al hotel",
        ],
    )


# ── Página de Reservas ───────────────────────
def reservas():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("📋 Formulario de Reserva", size="6", color=GRIS_OSCURO),
                rx.text(
                    "¡Llena todos los campos para asegurar tu lugar! 😊",
                    color=GRIS,
                    margin_bottom="20px",
                ),
                rx.box(
                    rx.heading("👤 Tus datos", size="5", color=GRIS_OSCURO, margin_bottom="12px"),
                    rx.text("Nombre completo *",     color=GRIS_OSCURO),
                    rx.input(placeholder="Ej: María García",   width="100%", margin_bottom="12px"),
                    rx.text("Correo electrónico *",  color=GRIS_OSCURO),
                    rx.input(placeholder="ejemplo@correo.com", type="email", width="100%", margin_bottom="12px"),
                    rx.text("Teléfono / WhatsApp *", color=GRIS_OSCURO),
                    rx.input(placeholder="(809) 000-0000",     type="tel",   width="100%", margin_bottom="12px"),
                    rx.text("Nacionalidad",          color=GRIS_OSCURO),
                    rx.input(placeholder="Ej: Dominicana",     width="100%"),
                    border="1px solid " + AZUL_BORDE,
                    border_radius="6px",
                    background=AZUL_CLARO,
                    padding="15px",
                    width="100%",
                    max_width="520px",
                    margin_bottom="20px",
                ),
                rx.box(
                    rx.heading("🏖️ Detalles del tour", size="5", color=GRIS_OSCURO, margin_bottom="12px"),
                    rx.text("Tour que quieres reservar *", color=GRIS_OSCURO),
                    rx.select(
                        ["Isla Saona – US$50", "Los Haitises – US$40", "Punta Cana Aventura – US$65"],
                        placeholder="-- Elige un tour --",
                        width="100%",
                        margin_bottom="12px",
                    ),
                    rx.text("Fecha del tour *",            color=GRIS_OSCURO),
                    rx.input(type="date", width="100%",    margin_bottom="12px"),
                    rx.text("¿Cuántas personas van? *",    color=GRIS_OSCURO),
                    rx.input(placeholder="1", type="number", width="100%", margin_bottom="12px"),
                    rx.text("¿Alguna solicitud especial?", color=GRIS_OSCURO),
                    rx.text_area(
                        placeholder="Alergias, cumpleaños, necesidades especiales...",
                        rows="3",
                        width="100%",
                    ),
                    border="1px solid " + AZUL_BORDE,
                    border_radius="6px",
                    background=AZUL_CLARO,
                    padding="15px",
                    width="100%",
                    max_width="520px",
                    margin_bottom="20px",
                ),
                rx.box(
                    rx.heading("💳 Método de pago", size="5", color=GRIS_OSCURO, margin_bottom="12px"),
                    rx.text("Selecciona cómo quieres pagar:", color=GRIS_OSCURO, margin_bottom="8px"),
                    rx.vstack(
                        rx.hstack(rx.text("💳"), rx.text("Tarjeta de crédito / débito", color=GRIS_OSCURO), spacing="2"),
                        rx.hstack(rx.text("📱"), rx.text("Transferencia bancaria",       color=GRIS_OSCURO), spacing="2"),
                        rx.hstack(rx.text("💵"), rx.text("Efectivo (pago en destino)",   color=GRIS_OSCURO), spacing="2"),
                        align="start",
                        spacing="2",
                        margin_bottom="12px",
                    ),
                    rx.text("🔒 Tus datos están seguros con nosotros.", color=GRIS, font_size="13px"),
                    border="1px solid " + AZUL_BORDE,
                    border_radius="6px",
                    background=AZUL_CLARO,
                    padding="15px",
                    width="100%",
                    max_width="520px",
                    margin_bottom="25px",
                ),
                rx.button(
                    "✅ Confirmar mi Reserva",
                    background=VERDE,
                    color=BLANCO,
                    padding="10px 25px",
                    font_size="16px",
                ),
                rx.text(
                    "Al reservar aceptas nuestros términos y condiciones.",
                    color=GRIS,
                    font_size="12px",
                    margin_top="8px",
                ),
                align="center",
                width="100%",
                max_width="560px",
                padding="30px 20px",
            ),
            width="100%",
        ),
        background=FONDO,
    )


# ── App ──────────────────────────────────────
app = rx.App()
app.add_page(home,           route="/")
app.add_page(desc_saona,     route="/descripcion/saona")
app.add_page(desc_haitises,  route="/descripcion/haitises")
app.add_page(desc_puntacana, route="/descripcion/puntacana")
app.add_page(reservas,       route="/reservas")