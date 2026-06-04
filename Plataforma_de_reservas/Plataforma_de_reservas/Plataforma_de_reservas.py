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
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Saona_Island_December_2020.jpg",
        "href": "/descripcion/saona",
        "tags": ["saona", "isla", "snorkel", "catamarán", "playa"],
    },
    {
        "nombre": "Los Haitises 🦜",
        "descripcion": "Tour ecológico por manglares, cuevas y aves del Parque Nacional.",
        "precio": "US$40 / persona",
        "imagen": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/03/c6/b8/los-haitises.jpg?w=1200&h=-1&s=1",
        "href": "/descripcion/haitises",
        "tags": ["haitises", "ecológico", "manglar", "cuevas", "naturaleza"],
    },
    {
        "nombre": "Punta Cana 🌿",
        "descripcion": "Buggy, tirolesas y cenote en la selva tropical.",
        "precio": "US$65 / persona",
        "imagen": "https://media.staticontent.com/media/pictures/83239c0a-50e5-44c5-bbb2-bea8292543e4",
        "href": "/descripcion/puntacana",
        "tags": ["punta cana", "aventura", "buggy", "tirolesa", "cenote"],
    },
    {
        "nombre": "Santo Domingo 🏙️",
        "descripcion": "Recorre la capital dominicana, su historia y cultura única.",
        "precio": "US$35 / persona",
        "imagen": "https://www.visitcentroamerica.com/wp-content/uploads/2025/04/Santo-Domingo-Boardwalk-Dominican-Republic-05.webp",
        "href": "/descripcion/santodomingo",
        "tags": ["santo domingo", "capital", "ciudad", "historia", "cultura"],
    },
    {
        "nombre": "Los Tres Ojos 👁️",
        "descripcion": "Lagunas subterráneas dentro de un parque natural único en el Caribe.",
        "precio": "US$25 / persona",
        "imagen": "https://www.viajesyfotografia.com/wp-content/uploads/2015/09/parque-de-los-tres-ojos-santo-domingo.jpg",
        "href": "/descripcion/tresojos",
        "tags": ["tres ojos", "lagunas", "parque", "cueva", "naturaleza"],
    },
    {
        "nombre": "Cayo Levantado 🌴",
        "descripcion": "La famosa isla del ron Barceló. Playas paradisíacas en Samaná.",
        "precio": "US$55 / persona",
        "imagen": "https://www.colonialtours.com/images/1cayo-levantadoislandcolonial2.jpg",
        "href": "/descripcion/cayolevantado",
        "tags": ["cayo levantado", "isla", "playa", "samaná", "barceló"],
    },
    {
        "nombre": "Ciudad Colonial 🏛️",
        "descripcion": "Patrimonio de la Humanidad. Paseo por la primera ciudad del Nuevo Mundo.",
        "precio": "US$30 / persona",
        "imagen": "https://www.lopesancostabavaro.com/wp-content/uploads/2021/03/6.jpg",
        "href": "/descripcion/ciudadcolonial",
        "tags": ["ciudad colonial", "patrimonio", "historia", "ozama", "colonial"],
    },
    {
        "nombre": "Umbrella Street ☂️",
        "descripcion": "La calle más colorida y fotogénica de Puerto Plata. ¡Perfecta para fotos!",
        "precio": "US$20 / persona",
        "imagen": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/ce/f6/4b/caption.jpg?w=900&h=500&s=1",
        "href": "/descripcion/umbrellastreet",
        "tags": ["umbrella street", "puerto plata", "colorida", "fotos", "turismo"],
    },
    {
        "nombre": "Samaná 🐳",
        "descripcion": "Avistamiento de ballenas jorobadas y paisajes naturales impresionantes.",
        "precio": "US$60 / persona",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/4/41/Santa_Barbara_de_Saman%C3%A1_%28Dominican_Republic%29.jpeg",
        "href": "/descripcion/samana",
        "tags": ["samaná", "ballenas", "naturaleza", "mar", "ecoturismo"],
    },
    {
        "nombre": "Jarabacoa 🏔️",
        "descripcion": "Rafting, cascadas y montañas. La ciudad de la eterna primavera.",
        "precio": "US$55 / persona",
        "imagen": "https://www.colonialtours.com/1rjarabariverclubp.jpg",
        "href": "/descripcion/jarabacoa",
        "tags": ["jarabacoa", "montaña", "rafting", "cascada", "aventura"],
    },
    {
        "nombre": "Lago Enriquillo 🦎",
        "descripcion": "El lago salado más grande del Caribe. Hogar de cocodrilos e iguanas.",
        "precio": "US$45 / persona",
        "imagen": "https://img.mmc.com.do/elcaribe-bucket/uploads/2023/10/whatsapp-image-2023-10-13-at-444.jpg.webp",
        "href": "/descripcion/lagoenriquillo",
        "tags": ["lago enriquillo", "cocodrilos", "iguanas", "lago", "naturaleza"],
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


# ── Función reutilizable de descripción ──────
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


# ── Páginas individuales ─────────────────────
def desc_saona():
    return pagina_descripcion(
        titulo="🏝️ Isla Saona",
        subtitulo="Excursión de día completo",
        imagen="https://upload.wikimedia.org/wikipedia/commons/f/f0/Saona_Island_December_2020.jpg",
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
        imagen="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/03/c6/b8/los-haitises.jpg?w=1200&h=-1&s=1",
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
        imagen="https://media.staticontent.com/media/pictures/83239c0a-50e5-44c5-bbb2-bea8292543e4",
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


def desc_santodomingo():
    return pagina_descripcion(
        titulo="🏙️ Santo Domingo",
        subtitulo="Tour por la capital dominicana",
        imagen="https://www.visitcentroamerica.com/wp-content/uploads/2025/04/Santo-Domingo-Boardwalk-Dominican-Republic-05.webp",
        detalles=[
            "✅ Duración: 6 horas",
            "✅ Grupo máximo: 20 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Visita al Malecón y el Faro a Colón",
            "✅ Recorrido por la Ciudad Colonial",
            "✅ Guía bilingüe (español / inglés)",
            "💵 Precio: US$35 por persona",
        ],
        descripcion_texto=(
            "Santo Domingo, la primera ciudad europea del Nuevo Mundo, es un destino lleno de historia "
            "y vida. Recorre su famoso Malecón, visita el imponente Faro a Colón y sumérgete en la "
            "vibrante cultura dominicana. ¡Una experiencia que mezcla pasado y presente!"
        ),
        itinerario=[
            "🕘 09:00 AM — Recogida en el hotel",
            "🌊 10:00 AM — Paseo por el Malecón",
            "🏛️ 11:00 AM — Visita al Faro a Colón",
            "🍽️ 12:30 PM — Almuerzo en restaurante local",
            "🏙️ 02:00 PM — Recorrido por la Ciudad Colonial",
            "🏨 04:00 PM — Regreso al hotel",
        ],
    )


def desc_tresojos():
    return pagina_descripcion(
        titulo="👁️ Parque Nacional Los Tres Ojos",
        subtitulo="Lagunas subterráneas en el corazón de Santo Domingo",
        imagen="https://www.viajesyfotografia.com/wp-content/uploads/2015/09/parque-de-los-tres-ojos-santo-domingo.jpg",
        detalles=[
            "✅ Duración: 3 horas",
            "✅ Grupo máximo: 15 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Entrada al parque incluida",
            "✅ Recorrido en bote por las lagunas",
            "✅ Guía experto en geología",
            "💵 Precio: US$25 por persona",
        ],
        descripcion_texto=(
            "Los Tres Ojos es un parque nacional único formado por tres lagunas subterráneas dentro "
            "de una cueva de piedra caliza. Sus aguas de colores verdes y azules y la vegetación "
            "tropical que lo rodea lo convierten en uno de los paisajes más sorprendentes del Caribe."
        ),
        itinerario=[
            "🕘 09:00 AM — Recogida en el hotel",
            "🚌 09:45 AM — Llegada al parque",
            "🚶 10:00 AM — Recorrido por las cuevas",
            "🚤 10:45 AM — Paseo en bote entre lagunas",
            "📸 11:30 AM — Tiempo libre para fotos",
            "🏨 12:30 PM — Regreso al hotel",
        ],
    )


def desc_cayolevantado():
    return pagina_descripcion(
        titulo="🌴 Cayo Levantado",
        subtitulo="La isla del ron Barceló en Samaná",
        imagen="https://www.colonialtours.com/images/1cayo-levantadoislandcolonial2.jpg",
        detalles=[
            "✅ Duración: 8 horas",
            "✅ Grupo máximo: 20 personas",
            "✅ Transporte y lancha incluidos",
            "✅ Almuerzo buffet en la isla",
            "✅ Acceso a playas privadas",
            "✅ Guía bilingüe (español / inglés)",
            "💵 Precio: US$55 por persona",
        ],
        descripcion_texto=(
            "Cayo Levantado, también conocida como la isla del ron Barceló, es una pequeña joya "
            "rodeada de aguas turquesas en la bahía de Samaná. Sus playas de arena blanca y su "
            "ambiente tranquilo la convierten en el escape perfecto para un día de relax total."
        ),
        itinerario=[
            "🕗 07:30 AM — Recogida en el hotel",
            "🚌 09:00 AM — Llegada al puerto de Samaná",
            "🚤 09:30 AM — Lancha hacia Cayo Levantado",
            "🏖️ 10:00 AM — Tiempo libre en la playa",
            "🍽️ 12:30 PM — Almuerzo buffet",
            "🌅 03:00 PM — Regreso al puerto",
            "🏨 04:30 PM — Llegada al hotel",
        ],
    )


def desc_ciudadcolonial():
    return pagina_descripcion(
        titulo="🏛️ Ciudad Colonial",
        subtitulo="Patrimonio de la Humanidad — UNESCO",
        imagen="https://www.lopesancostabavaro.com/wp-content/uploads/2021/03/6.jpg",
        detalles=[
            "✅ Duración: 4 horas",
            "✅ Grupo máximo: 15 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Visita al Alcázar de Colón",
            "✅ Recorrido por la Calle Las Damas",
            "✅ Guía histórico certificado",
            "💵 Precio: US$30 por persona",
        ],
        descripcion_texto=(
            "La Ciudad Colonial de Santo Domingo es el primer asentamiento europeo permanente "
            "del Nuevo Mundo y Patrimonio de la Humanidad por la UNESCO. Sus calles empedradas, "
            "fortalezas y catedrales del siglo XVI te transportan directamente a la época de la conquista."
        ),
        itinerario=[
            "🕘 09:00 AM — Recogida en el hotel",
            "⛪ 09:45 AM — Visita a la Catedral Primada de América",
            "🏰 10:30 AM — Alcázar de Colón",
            "🚶 11:30 AM — Paseo por la Calle Las Damas",
            "🍽️ 12:30 PM — Almuerzo en restaurante colonial",
            "🏨 01:30 PM — Regreso al hotel",
        ],
    )


def desc_umbrellastreet():
    return pagina_descripcion(
        titulo="☂️ Umbrella Street",
        subtitulo="La calle más colorida de Puerto Plata",
        imagen="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/28/ce/f6/4b/caption.jpg?w=900&h=500&s=1",
        detalles=[
            "✅ Duración: 5 horas",
            "✅ Grupo máximo: 20 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Recorrido por el centro de Puerto Plata",
            "✅ Visita al Teleférico del Pico Isabel",
            "✅ Guía local experto",
            "💵 Precio: US$20 por persona",
        ],
        descripcion_texto=(
            "Umbrella Street es la calle más instagrameable de Puerto Plata, decorada con cientos "
            "de paraguas de colores que crean un techo vibrante y único. Perfecta para fotografías "
            "y para descubrir el encanto colonial y caribeño del norte dominicano."
        ),
        itinerario=[
            "🕘 09:00 AM — Recogida en el hotel",
            "🚌 10:00 AM — Llegada a Puerto Plata",
            "☂️ 10:30 AM — Recorrido por Umbrella Street",
            "📸 11:00 AM — Tiempo libre para fotos",
            "🚡 12:00 PM — Visita al Teleférico",
            "🏨 02:00 PM — Regreso al hotel",
        ],
    )


def desc_samana():
    return pagina_descripcion(
        titulo="🐳 Samaná",
        subtitulo="Avistamiento de ballenas jorobadas",
        imagen="https://upload.wikimedia.org/wikipedia/commons/4/41/Santa_Barbara_de_Saman%C3%A1_%28Dominican_Republic%29.jpeg",
        detalles=[
            "✅ Duración: 8 horas",
            "✅ Grupo máximo: 15 personas",
            "✅ Transporte y lancha incluidos",
            "✅ Avistamiento de ballenas (enero–marzo)",
            "✅ Visita a la cascada El Limón",
            "✅ Guía marino certificado",
            "💵 Precio: US$60 / persona",
        ],
        descripcion_texto=(
            "Samaná es uno de los mejores lugares del mundo para avistar ballenas jorobadas. "
            "Entre enero y marzo, miles de ballenas llegan a sus aguas a aparearse y dar a luz. "
            "Además, la impresionante cascada El Limón y sus playas vírgenes hacen de Samaná "
            "un destino imperdible durante todo el año."
        ),
        itinerario=[
            "🕗 07:00 AM — Recogida en el hotel",
            "🚌 08:30 AM — Llegada a Samaná",
            "🐳 09:00 AM — Tour de avistamiento de ballenas",
            "🍽️ 12:00 PM — Almuerzo en restaurante local",
            "💧 01:30 PM — Visita a la cascada El Limón",
            "🏨 05:00 PM — Regreso al hotel",
        ],
    )


def desc_jarabacoa():
    return pagina_descripcion(
        titulo="🏔️ Jarabacoa",
        subtitulo="La ciudad de la eterna primavera",
        imagen="https://www.colonialtours.com/1rjarabariverclubp.jpg",
        detalles=[
            "✅ Duración: 9 horas",
            "✅ Grupo máximo: 15 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Rafting en el río Yaque del Norte",
            "✅ Visita a la cascada Jimenoa",
            "✅ Almuerzo incluido",
            "💵 Precio: US$55 / persona",
        ],
        descripcion_texto=(
            "Jarabacoa es el paraíso de la aventura en las montañas dominicanas. Con un clima "
            "fresco y agradable durante todo el año, ofrece rafting en ríos de aguas bravas, "
            "cascadas impresionantes y senderos rodeados de pinos. ¡La escapada perfecta de la ciudad!"
        ),
        itinerario=[
            "🕖 06:30 AM — Recogida en el hotel",
            "🚌 08:30 AM — Llegada a Jarabacoa",
            "🌊 09:00 AM — Rafting en el río Yaque del Norte",
            "🍽️ 12:00 PM — Almuerzo típico dominicano",
            "💧 01:30 PM — Visita a la cascada Jimenoa",
            "🏨 05:30 PM — Regreso al hotel",
        ],
    )


def desc_lagoenriquillo():
    return pagina_descripcion(
        titulo="🦎 Lago Enriquillo",
        subtitulo="El lago salado más grande del Caribe",
        imagen="https://img.mmc.com.do/elcaribe-bucket/uploads/2023/10/whatsapp-image-2023-10-13-at-444.jpg.webp",
        detalles=[
            "✅ Duración: 8 horas",
            "✅ Grupo máximo: 12 personas",
            "✅ Transporte de ida y vuelta",
            "✅ Tour en bote por el lago",
            "✅ Avistamiento de cocodrilos e iguanas",
            "✅ Visita a la Isla Cabritos",
            "💵 Precio: US$45 / persona",
        ],
        descripcion_texto=(
            "El Lago Enriquillo es el lago más grande del Caribe y está ubicado por debajo del "
            "nivel del mar. Es hogar de cocodrilos americanos, iguanas rinocerontes y flamencos. "
            "Un destino fascinante para los amantes de la naturaleza y la fauna salvaje dominicana."
        ),
        itinerario=[
            "🕖 06:00 AM — Recogida en el hotel",
            "🚌 08:30 AM — Llegada al lago",
            "🚤 09:00 AM — Tour en bote por el lago",
            "🦎 10:00 AM — Avistamiento de fauna en Isla Cabritos",
            "🍽️ 12:00 PM — Almuerzo en La Descubierta",
            "🏨 04:00 PM — Regreso al hotel",
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
                        [t["nombre"] + " — " + t["precio"] for t in TOURS],
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
app.add_page(home,                route="/")
app.add_page(desc_saona,          route="/descripcion/saona")
app.add_page(desc_haitises,       route="/descripcion/haitises")
app.add_page(desc_puntacana,      route="/descripcion/puntacana")
app.add_page(desc_santodomingo,   route="/descripcion/santodomingo")
app.add_page(desc_tresojos,       route="/descripcion/tresojos")
app.add_page(desc_cayolevantado,  route="/descripcion/cayolevantado")
app.add_page(desc_ciudadcolonial, route="/descripcion/ciudadcolonial")
app.add_page(desc_umbrellastreet, route="/descripcion/umbrellastreet")
app.add_page(desc_samana,         route="/descripcion/samana")
app.add_page(desc_jarabacoa,      route="/descripcion/jarabacoa")
app.add_page(desc_lagoenriquillo, route="/descripcion/lagoenriquillo")
app.add_page(reservas,            route="/reservas")