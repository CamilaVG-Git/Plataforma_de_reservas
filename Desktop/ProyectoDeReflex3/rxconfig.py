import reflex as rx

config = rx.Config(
    app_name="ProyectoDeReflex3",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)