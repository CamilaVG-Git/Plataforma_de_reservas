import reflex as rx

# ─────────────────────────────────────────────
#  PALETA Y ESTILOS GLOBALES
# ─────────────────────────────────────────────
AZUL_MAR   = "#0A4D68"
TURQUESA   = "#05BFDB"
ARENA      = "#FFF8EE"
CORAL      = "#FF6B35"
GRIS_TEXTO = "#3D3D3D"
BLANCO     = "#FFFFFF"

FONT_HEADING = "Playfair Display"
FONT_BODY    = "DM Sans"

GOOGLE_FONTS = (
    "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900"
    "&family=DM+Sans:wght@300;400;500;600&display=swap"
)

card_style = {
    "background": BLANCO,
    "border_radius": "16px",
    "overflow": "hidden",
    "box_shadow": "0 4px 24px rgba(10,77,104,0.10)",
    "transition": "transform 0.25s ease, box_shadow 0.25s ease",
    "_hover": {
        "transform": "translateY(-6px)",
        "box_shadow": "0 12px 36px rgba(10,77,104,0.18)",
    },
    "width": "300px",
}

btn_primary = {
    "background": CORAL,
    "color": BLANCO,
    "font_family": FONT_BODY,
    "font_weight": "600",
    "border_radius": "8px",
    "padding": "0.65em 1.6em",
    "cursor": "pointer",
    "transition": "background 0.2s",
    "_hover": {"background": "#e05522"},
}

input_style = {
    "border": f"1.5px solid #C9E8F0",
    "border_radius": "8px",
    "padding": "0.7em 1em",
    "font_family": FONT_BODY,
    "width": "100%",
    "background": BLANCO,
    "_focus": {"border_color": TURQUESA, "outline": "none"},
}


# ─────────────────────────────────────────────
#  NAVBAR
# ─────────────────────────────────────────────
def navbar():
    return rx.box(
        rx.hstack(
            # Logo
            rx.hstack(
                rx.icon("palmtree", color=TURQUESA, size=28),
                rx.text(
                    "Tu",
                    font_family=FONT_HEADING,
                    font_size="1.5rem",
                    font_weight="900",
                    color=BLANCO,
                ),
                rx.text(
                    "Reserva",
                    font_family=FONT_HEADING,
                    font_size="1.5rem",
                    font_weight="900",
                    color=TURQUESA,
                ),
                spacing="1",
                align="center",
            ),
            rx.spacer(),
            # Links
            rx.hstack(
                rx.link(
                    "Inicio",
                    href="/",
                    color=BLANCO,
                    font_family=FONT_BODY,
                    font_weight="500",
                    _hover={"color": TURQUESA},
                    transition="color 0.2s",
                ),
                rx.link(
                    "Descripción",
                    href="/descripcion",
                    color=BLANCO,
                    font_family=FONT_BODY,
                    font_weight="500",
                    _hover={"color": TURQUESA},
                    transition="color 0.2s",
                ),
                rx.link(
                    "Reservas",
                    href="/reservas",
                    color=BLANCO,
                    font_family=FONT_BODY,
                    font_weight="500",
                    _hover={"color": TURQUESA},
                    transition="color 0.2s",
                ),
                rx.link(
                    rx.button("Reservar ahora", **btn_primary),
                    href="/reservas",
                ),
                spacing="6",
                align="center",
            ),
            align="center",
            width="100%",
            padding_x="2em",
        ),
        background=AZUL_MAR,
        padding_y="1em",
        position="sticky",
        top="0",
        z_index="100",
        box_shadow="0 2px 12px rgba(0,0,0,0.15)",
    )


# ─────────────────────────────────────────────
#  TARJETA DE OFERTA
# ─────────────────────────────────────────────
def oferta_card(nombre, descripcion, precio, imagen, duracion):
    return rx.link(
        rx.box(
            rx.image(
                src=imagen,
                width="100%",
                height="200px",
                object_fit="cover",
            ),
            rx.box(
                rx.hstack(
                    rx.badge(
                        duracion,
                        color_scheme="blue",
                        border_radius="20px",
                        font_size="0.75rem",
                    ),
                    rx.spacer(),
                    rx.text(
                        precio,
                        font_family=FONT_HEADING,
                        font_size="1.2rem",
                        font_weight="700",
                        color=CORAL,
                    ),
                    width="100%",
                    margin_bottom="0.5em",
                ),
                rx.heading(
                    nombre,
                    size="4",
                    font_family=FONT_HEADING,
                    color=AZUL_MAR,
                    margin_bottom="0.3em",
                ),
                rx.text(
                    descripcion,
                    font_family=FONT_BODY,
                    font_size="0.9rem",
                    color=GRIS_TEXTO,
                    line_height="1.5",
                ),
                rx.hstack(
                    rx.text(
                        "Ver más →",
                        color=TURQUESA,
                        font_family=FONT_BODY,
                        font_weight="600",
                        font_size="0.9rem",
                    ),
                    margin_top="1em",
                ),
                padding="1.2em",
            ),
            **card_style,
        ),
        href="/descripcion",
        text_decoration="none",
    )


# ─────────────────────────────────────────────
#  PÁGINA DE INICIO
# ─────────────────────────────────────────────
def home():
    # TODO: API — reemplazar las tarjetas estáticas con datos del endpoint GET /ofertas
    return rx.box(
        rx.el.link(rel="stylesheet", href=GOOGLE_FONTS),
        navbar(),

        # ── Hero ──────────────────────────────
        rx.box(
            rx.box(
                rx.text(
                    "REPÚBLICA DOMINICANA",
                    font_family=FONT_BODY,
                    font_size="0.85rem",
                    font_weight="600",
                    letter_spacing="3px",
                    color=TURQUESA,
                    margin_bottom="0.5em",
                ),
                rx.heading(
                    "Descubre el paraíso que siempre soñaste",
                    font_family=FONT_HEADING,
                    font_size="clamp(2rem, 5vw, 3.5rem)",
                    font_weight="900",
                    color=BLANCO,
                    line_height="1.15",
                    max_width="650px",
                    margin_bottom="1em",
                ),
                rx.text(
                    "Tours, excursiones y experiencias únicas. Reserva en minutos y vive momentos inolvidables.",
                    font_family=FONT_BODY,
                    color="rgba(255,255,255,0.85)",
                    font_size="1.05rem",
                    max_width="500px",
                    margin_bottom="2em",
                    line_height="1.6",
                ),
                # Buscador
                rx.box(
                    rx.hstack(
                        rx.input(
                            placeholder="🔍  Buscar destino o actividad...",
                            **input_style,
                        ),
                        rx.button("Buscar", **btn_primary),
                        spacing="3",
                        width="100%",
                    ),
                    background="rgba(255,255,255,0.12)",
                    backdrop_filter="blur(8px)",
                    border_radius="12px",
                    padding="1em",
                    max_width="560px",
                ),
                padding="4em 2em 4em 2em",
                max_width="750px",
            ),
            background=f"linear-gradient(135deg, {AZUL_MAR} 0%, #0D7DA6 60%, {TURQUESA} 100%)",
            min_height="480px",
            display="flex",
            align_items="center",
        ),

        # ── Estadísticas rápidas ──────────────
        rx.hstack(
            _stat("500+", "Viajeros felices"),
            _stat("20+", "Destinos únicos"),
            _stat("5★", "Calificación promedio"),
            _stat("24/7", "Atención al cliente"),
            justify="center",
            spacing="8",
            padding="2.5em 2em",
            background=AZUL_MAR,
            flex_wrap="wrap",
        ),

        # ── Ofertas turísticas ────────────────
        rx.box(
            rx.heading(
                "Ofertas Turísticas",
                font_family=FONT_HEADING,
                size="7",
                color=AZUL_MAR,
                margin_bottom="0.3em",
            ),
            rx.text(
                "Experiencias cuidadosamente seleccionadas para ti",
                font_family=FONT_BODY,
                color=GRIS_TEXTO,
                margin_bottom="2em",
            ),
            rx.hstack(
                # TODO: API — estos datos vendrán de GET /api/ofertas
                oferta_card(
                    "Isla Saona",
                    "Excursión de día completo a la paradisíaca Isla Saona, con catamaran, snorkel y almuerzo incluido.",
                    "US$50",
                    "/isla_saona.jpg",
                    "8 horas",
                ),
                oferta_card(
                    "Los Haitises",
                    "Tour ecológico por el Parque Nacional Los Haitises: manglares, cuevas y aves exóticas.",
                    "US$40",
                    "/los_haitises.jpg",
                    "7 horas",
                ),
                oferta_card(
                    "Punta Cana Aventura",
                    "Buggy, tirolesas y cenote en la selva tropical. Adrenalina pura con guías expertos.",
                    "US$65",
                    "/punta_cana.jpg",
                    "5 horas",
                ),
                spacing="6",
                flex_wrap="wrap",
                justify="center",
            ),
            padding="3em 2em",
            background=ARENA,
            text_align="center",
        ),

        # ── Contacto ──────────────────────────
        rx.box(
            rx.heading(
                "Contáctanos",
                font_family=FONT_HEADING,
                size="6",
                color=BLANCO,
                margin_bottom="1.5em",
            ),
            rx.hstack(
                _contacto_item("📧", "Email", "info@tureserva.com"),
                _contacto_item("📞", "Teléfono", "(809) 555-1234"),
                _contacto_item("📍", "Ubicación", "Higüey, La Altagracia"),
                _contacto_item("🕐", "Horario", "Lun–Dom 8am–8pm"),
                spacing="8",
                flex_wrap="wrap",
                justify="center",
            ),
            background=AZUL_MAR,
            padding="3em 2em",
            text_align="center",
        ),

        # Footer
        rx.box(
            rx.text(
                "© 2025 TuReserva · República Dominicana",
                font_family=FONT_BODY,
                font_size="0.85rem",
                color="rgba(255,255,255,0.5)",
            ),
            background="#061E2A",
            padding="1.2em",
            text_align="center",
        ),

        background=ARENA,
        font_family=FONT_BODY,
    )


def _stat(valor, label):
    return rx.box(
        rx.text(valor, font_family=FONT_HEADING, font_size="1.8rem", font_weight="700", color=TURQUESA),
        rx.text(label, font_family=FONT_BODY, font_size="0.85rem", color="rgba(255,255,255,0.7)"),
        text_align="center",
    )


def _contacto_item(icono, titulo, valor):
    return rx.box(
        rx.text(icono, font_size="1.8rem", margin_bottom="0.3em"),
        rx.text(titulo, font_family=FONT_BODY, font_weight="600", color=TURQUESA, font_size="0.85rem"),
        rx.text(valor, font_family=FONT_BODY, color=BLANCO, font_size="0.95rem"),
        text_align="center",
    )


# ─────────────────────────────────────────────
#  PÁGINA DE DESCRIPCIÓN
# ─────────────────────────────────────────────
def descripcion():
    # TODO: API — recibir id del destino y hacer GET /api/ofertas/{id}
    return rx.box(
        rx.el.link(rel="stylesheet", href=GOOGLE_FONTS),
        navbar(),

        rx.box(
            # Encabezado con imagen de fondo
            rx.box(
                rx.text(
                    "EXCURSIÓN DESTACADA",
                    font_family=FONT_BODY,
                    font_size="0.8rem",
                    font_weight="600",
                    letter_spacing="3px",
                    color=TURQUESA,
                    margin_bottom="0.5em",
                ),
                rx.heading(
                    "Isla Saona",          # TODO: API — nombre dinámico
                    font_family=FONT_HEADING,
                    font_size="clamp(2.2rem, 4vw, 3rem)",
                    font_weight="900",
                    color=BLANCO,
                    margin_bottom="0.5em",
                ),
                rx.hstack(
                    rx.badge("8 horas", color_scheme="blue"),
                    rx.badge("Incluye almuerzo", color_scheme="green"),
                    rx.badge("Transporte incluido", color_scheme="orange"),
                    spacing="2",
                    flex_wrap="wrap",
                ),
                padding="3em 2em",
                background=f"linear-gradient(135deg, {AZUL_MAR} 0%, #0D7DA6 100%)",
            ),

            rx.box(
                # Imagen principal
                rx.image(
                    src="/isla_saona.jpg",   # TODO: API — imagen dinámica
                    width="100%",
                    max_width="800px",
                    height="420px",
                    object_fit="cover",
                    border_radius="16px",
                    box_shadow="0 8px 32px rgba(10,77,104,0.2)",
                    display="block",
                    margin="0 auto 2em auto",
                ),

                # Descripción general
                rx.box(
                    rx.heading(
                        "Descripción General",
                        font_family=FONT_HEADING,
                        size="5",
                        color=AZUL_MAR,
                        margin_bottom="0.8em",
                    ),
                    rx.text(
                        # TODO: API — texto dinámico del destino
                        "La Isla Saona es una de las joyas naturales de la República Dominicana. "
                        "Ubicada en el extremo sureste del país, forma parte del Parque Nacional del Este "
                        "y es conocida por sus playas de arena blanca, aguas cristalinas color turquesa y "
                        "una flora y fauna únicas. Durante esta excursión de día completo, disfrutarás de "
                        "un recorrido en catamarán con música y bebidas, snorkel en arrecifes de coral, "
                        "tiempo libre en la playa y un delicioso almuerzo caribeño.",
                        font_family=FONT_BODY,
                        color=GRIS_TEXTO,
                        line_height="1.8",
                        font_size="1rem",
                    ),
                    margin_bottom="2em",
                ),

                # Detalles
                rx.box(
                    rx.heading(
                        "Detalles del Tour",
                        font_family=FONT_HEADING,
                        size="5",
                        color=AZUL_MAR,
                        margin_bottom="1em",
                    ),
                    rx.hstack(
                        _detalle_card("⏱️", "Duración", "8 horas"),
                        _detalle_card("👥", "Grupo", "Máx. 20 personas"),
                        _detalle_card("🌡️", "Dificultad", "Fácil"),
                        _detalle_card("💵", "Precio", "US$50 / persona"),
                        spacing="4",
                        flex_wrap="wrap",
                        justify="start",
                    ),
                    rx.heading(
                        "¿Qué incluye?",
                        font_family=FONT_HEADING,
                        size="4",
                        color=AZUL_MAR,
                        margin_top="1.5em",
                        margin_bottom="0.8em",
                    ),
                    rx.hstack(
                        rx.vstack(
                            _check_item("✓  Transporte de ida y vuelta"),
                            _check_item("✓  Recorrido en catamarán"),
                            _check_item("✓  Equipo de snorkel"),
                            align="start",
                        ),
                        rx.vstack(
                            _check_item("✓  Almuerzo caribeño"),
                            _check_item("✓  Bebidas ilimitadas"),
                            _check_item("✓  Guía bilingüe"),
                            align="start",
                        ),
                        spacing="8",
                        flex_wrap="wrap",
                    ),
                    background=BLANCO,
                    border_radius="12px",
                    padding="1.5em",
                    box_shadow="0 2px 12px rgba(10,77,104,0.08)",
                    margin_bottom="2em",
                ),

                # Itinerario
                rx.box(
                    rx.heading(
                        "Itinerario",
                        font_family=FONT_HEADING,
                        size="5",
                        color=AZUL_MAR,
                        margin_bottom="1em",
                    ),
                    rx.vstack(
                        # TODO: API — itinerario dinámico
                        _itinerario_item("08:00 AM", "Punto de encuentro", "Recogida en hotel y traslado al puerto."),
                        _itinerario_item("09:30 AM", "Abordaje del catamarán", "Bienvenida con bebidas y música tropical."),
                        _itinerario_item("10:30 AM", "Parada de snorkel", "30 minutos explorando arrecifes de coral."),
                        _itinerario_item("12:00 PM", "Llegada a Isla Saona", "Tiempo libre en la playa y almuerzo."),
                        _itinerario_item("03:00 PM", "Regreso", "Viaje de vuelta en lancha rápida."),
                        _itinerario_item("04:30 PM", "Llegada al hotel", "Fin del tour."),
                        align="start",
                        spacing="0",
                    ),
                    background=BLANCO,
                    border_radius="12px",
                    padding="1.5em",
                    box_shadow="0 2px 12px rgba(10,77,104,0.08)",
                    margin_bottom="2em",
                ),

                rx.hstack(
                    rx.link(
                        rx.button("← Volver", variant="outline", border_color=AZUL_MAR, color=AZUL_MAR, font_family=FONT_BODY),
                        href="/",
                    ),
                    rx.link(
                        rx.button("Reservar este tour", **btn_primary),
                        href="/reservas",
                    ),
                    spacing="4",
                ),

                padding="2em",
                max_width="900px",
                margin="0 auto",
            ),

            background=ARENA,
            min_height="100vh",
        ),
        font_family=FONT_BODY,
    )


def _detalle_card(icono, titulo, valor):
    return rx.box(
        rx.text(icono, font_size="1.6rem"),
        rx.text(titulo, font_size="0.75rem", font_weight="600", color=GRIS_TEXTO, letter_spacing="1px"),
        rx.text(valor, font_family=FONT_HEADING, font_size="1rem", font_weight="700", color=AZUL_MAR),
        background=ARENA,
        border_radius="10px",
        padding="1em 1.3em",
        text_align="center",
        border=f"1px solid #C9E8F0",
        min_width="130px",
    )


def _check_item(texto):
    return rx.text(texto, font_family=FONT_BODY, color=GRIS_TEXTO, margin_bottom="0.4em")


def _itinerario_item(hora, titulo, descripcion_texto):
    return rx.hstack(
        rx.box(
            rx.text(hora, font_family=FONT_BODY, font_size="0.8rem", font_weight="600", color=TURQUESA, white_space="nowrap"),
            min_width="90px",
        ),
        rx.box(
            width="2px",
            background=f"linear-gradient({TURQUESA}, {AZUL_MAR})",
            align_self="stretch",
            margin_x="0.8em",
            min_height="50px",
        ),
        rx.box(
            rx.text(titulo, font_weight="600", color=AZUL_MAR, font_family=FONT_BODY, margin_bottom="0.2em"),
            rx.text(descripcion_texto, font_size="0.88rem", color=GRIS_TEXTO, font_family=FONT_BODY),
            padding_bottom="1em",
        ),
        align="start",
        width="100%",
    )


# ─────────────────────────────────────────────
#  PÁGINA DE RESERVAS
# ─────────────────────────────────────────────
def reservas():
    # TODO: API — al hacer submit, enviar POST /api/reservas con los datos del formulario
    return rx.box(
        rx.el.link(rel="stylesheet", href=GOOGLE_FONTS),
        navbar(),

        # Header
        rx.box(
            rx.text(
                "RESERVA TU EXPERIENCIA",
                font_family=FONT_BODY,
                font_size="0.8rem",
                font_weight="600",
                letter_spacing="3px",
                color=TURQUESA,
                margin_bottom="0.5em",
            ),
            rx.heading(
                "Completa tu reserva",
                font_family=FONT_HEADING,
                font_size="2.5rem",
                font_weight="900",
                color=BLANCO,
            ),
            rx.text(
                "Confirma los detalles y asegura tu lugar en minutos.",
                font_family=FONT_BODY,
                color="rgba(255,255,255,0.75)",
                margin_top="0.5em",
            ),
            background=f"linear-gradient(135deg, {AZUL_MAR} 0%, #0D7DA6 100%)",
            padding="2.5em 2em",
        ),

        rx.box(
            rx.hstack(
                # ── Formulario principal ──────────────────────
                rx.box(

                    # Datos de contacto
                    _form_section(
                        "1",
                        "Datos de Contacto",
                        rx.vstack(
                            _form_field("Nombre completo *", rx.input(placeholder="Ej. María García", **input_style)),
                            _form_field("Correo electrónico *", rx.input(placeholder="ejemplo@correo.com", type="email", **input_style)),
                            _form_field("Teléfono / WhatsApp *", rx.input(placeholder="(809) 000-0000", type="tel", **input_style)),
                            _form_field("Nacionalidad", rx.input(placeholder="Dominicana", **input_style)),
                            spacing="4",
                            width="100%",
                        ),
                    ),

                    # Detalles de la actividad
                    _form_section(
                        "2",
                        "Detalles de la Actividad",
                        rx.vstack(
                            _form_field(
                                "Tour seleccionado *",
                                rx.select(
                                    # TODO: API — poblar con GET /api/ofertas
                                    ["Isla Saona – US$50", "Los Haitises – US$40", "Punta Cana Aventura – US$65"],
                                    placeholder="Selecciona un tour...",
                                    **input_style,
                                ),
                            ),
                            rx.hstack(
                                _form_field(
                                    "Fecha *",
                                    rx.input(type="date", **input_style),
                                    flex="1",
                                ),
                                _form_field(
                                    "N.° de personas *",
                                    rx.input(placeholder="1", type="number", min="1", max="20", **input_style),
                                    flex="1",
                                ),
                                spacing="4",
                                width="100%",
                            ),
                            _form_field(
                                "Solicitudes especiales",
                                rx.text_area(
                                    placeholder="Alergias, necesidades especiales, celebraciones...",
                                    rows="3",
                                    **{**input_style, "resize": "vertical"},
                                ),
                            ),
                            spacing="4",
                            width="100%",
                        ),
                    ),

                    # Pago
                    _form_section(
                        "3",
                        "Información de Pago",
                        rx.vstack(
                            rx.text(
                                "Selecciona tu método de pago preferido:",
                                font_family=FONT_BODY,
                                font_size="0.9rem",
                                color=GRIS_TEXTO,
                                margin_bottom="0.5em",
                            ),
                            rx.hstack(
                                _pago_opcion("💳", "Tarjeta de crédito / débito"),
                                _pago_opcion("📱", "Transferencia bancaria"),
                                _pago_opcion("💵", "Efectivo (en destino)"),
                                spacing="3",
                                flex_wrap="wrap",
                            ),
                            rx.box(
                                rx.text(
                                    "🔒  Tus datos están protegidos con cifrado SSL.",
                                    font_family=FONT_BODY,
                                    font_size="0.85rem",
                                    color=GRIS_TEXTO,
                                ),
                                background="#E8F8F5",
                                border_radius="8px",
                                padding="0.8em 1em",
                                border_left=f"4px solid {TURQUESA}",
                                width="100%",
                                margin_top="0.5em",
                            ),
                            spacing="3",
                            width="100%",
                        ),
                    ),

                    rx.button(
                        "Confirmar Reserva →",
                        width="100%",
                        padding_y="1em",
                        font_size="1rem",
                        **btn_primary,
                        # TODO: API — on_click conectar con POST /api/reservas
                    ),
                    rx.text(
                        "Al reservar aceptas nuestros términos y condiciones. Recibirás una confirmación por email.",
                        font_family=FONT_BODY,
                        font_size="0.8rem",
                        color=GRIS_TEXTO,
                        text_align="center",
                        margin_top="0.8em",
                    ),

                    flex="2",
                    min_width="300px",
                ),

                # ── Panel resumen ─────────────────────────────
                rx.box(
                    rx.heading(
                        "Resumen del Tour",
                        font_family=FONT_HEADING,
                        size="4",
                        color=AZUL_MAR,
                        margin_bottom="1em",
                    ),
                    rx.image(
                        src="/isla_saona.jpg",   # TODO: API — imagen dinámica según tour
                        width="100%",
                        height="160px",
                        object_fit="cover",
                        border_radius="10px",
                        margin_bottom="1em",
                    ),
                    # TODO: API — mostrar detalles dinámicos según tour seleccionado
                    _resumen_row("🏝️  Tour", "Isla Saona"),
                    _resumen_row("⏱️  Duración", "8 horas"),
                    _resumen_row("👥  Personas", "—"),
                    _resumen_row("📅  Fecha", "—"),
                    rx.divider(margin_y="1em", border_color="#C9E8F0"),
                    _resumen_row("💵  Precio por persona", "US$50"),
                    _resumen_row("🧮  Total estimado", "US$50", bold=True, color=CORAL),
                    rx.box(
                        rx.text("¿Preguntas?", font_weight="600", font_family=FONT_BODY, color=AZUL_MAR),
                        rx.text("📞 (809) 555-1234", font_family=FONT_BODY, font_size="0.9rem", color=GRIS_TEXTO),
                        rx.text("📧 info@tureserva.com", font_family=FONT_BODY, font_size="0.9rem", color=GRIS_TEXTO),
                        background=ARENA,
                        border_radius="8px",
                        padding="1em",
                        margin_top="1.2em",
                    ),
                    background=BLANCO,
                    border_radius="14px",
                    padding="1.5em",
                    box_shadow="0 4px 20px rgba(10,77,104,0.1)",
                    flex="1",
                    min_width="250px",
                    align_self="start",
                    position="sticky",
                    top="80px",
                ),

                spacing="6",
                align="start",
                flex_wrap="wrap",
            ),
            padding="2em",
            max_width="1100px",
            margin="0 auto",
        ),

        background=ARENA,
        font_family=FONT_BODY,
        padding_bottom="3em",
    )


def _form_section(numero, titulo, contenido):
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(numero, color=BLANCO, font_weight="700", font_size="0.9rem"),
                background=AZUL_MAR,
                border_radius="50%",
                width="28px",
                height="28px",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.heading(titulo, size="4", font_family=FONT_HEADING, color=AZUL_MAR),
            align="center",
            spacing="3",
            margin_bottom="1em",
        ),
        contenido,
        background=BLANCO,
        border_radius="12px",
        padding="1.5em",
        box_shadow="0 2px 12px rgba(10,77,104,0.07)",
        margin_bottom="1.5em",
        width="100%",
    )


def _form_field(label, campo, **kwargs):
    return rx.box(
        rx.text(label, font_family=FONT_BODY, font_size="0.85rem", font_weight="500", color=GRIS_TEXTO, margin_bottom="0.4em"),
        campo,
        width="100%",
        **kwargs,
    )


def _pago_opcion(icono, texto):
    return rx.box(
        rx.text(icono, font_size="1.5rem"),
        rx.text(texto, font_family=FONT_BODY, font_size="0.8rem", color=GRIS_TEXTO, text_align="center"),
        border=f"1.5px solid #C9E8F0",
        border_radius="10px",
        padding="0.8em",
        text_align="center",
        cursor="pointer",
        transition="all 0.2s",
        _hover={"border_color": TURQUESA, "background": "#E8F8FC"},
        min_width="130px",
    )


def _resumen_row(label, valor, bold=False, color=GRIS_TEXTO):
    return rx.hstack(
        rx.text(label, font_family=FONT_BODY, font_size="0.88rem", color=GRIS_TEXTO),
        rx.spacer(),
        rx.text(
            valor,
            font_family=FONT_BODY,
            font_size="0.88rem",
            font_weight="700" if bold else "400",
            color=color,
        ),
        width="100%",
        margin_bottom="0.5em",
    )


# ─────────────────────────────────────────────
#  APP
# ─────────────────────────────────────────────
app = rx.App(
    stylesheets=[GOOGLE_FONTS],
)
app.add_page(home,        route="/")
app.add_page(descripcion, route="/descripcion")
app.add_page(reservas,    route="/reservas")