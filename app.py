import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Cargar las variables desde el archivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SSL_CA_PATH = os.getenv("SSL_CA")

try:
    print("Conectando a la base de datos en Aiven...")
    
    # Configuramos el motor pasándole el certificado de forma explícita
    engine = create_engine(
        DATABASE_URL,
        connect_args={"ssl": {"ca": SSL_CA_PATH}}
    )

    print("Leyendo el archivo setup_db.sql...")
    with open("setup_db.sql", "r", encoding="utf-8") as archivo_sql:
        script_sql = archivo_sql.read()

    with engine.connect() as conn:
        print("Inyectando tablas y datos de prueba...")
        # Separamos los comandos por punto y coma ';'
        comandos = script_sql.split(";")
        for comando in comandos:
            comando_limpio = comando.strip()
            if comando_limpio:
                conn.execute(text(comando_limpio))
        
        # Guardar cambios
        conn.commit()
        
    print("\n============== RESULTS ==============")
    print("✅ ¡Tablas creadas y datos insertados con éxito!")
    print("=====================================")

except Exception as e:
    print("\n❌ Error durante el proceso:")
    print(e)