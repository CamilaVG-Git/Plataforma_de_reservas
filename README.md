 Documentación Técnica: Configuración e Inyección de la Base de Datos
**Proyecto:** Plataforma de Reservas y Ofertas Turísticas (TureservaAPP)  
**Entorno de Servidor:** Aiven Cloud (MySQL)  
**Tecnologías:** Python, SQLAlchemy, PyMySQL, MySQL Workbench  

---

## 1. Arquitectura de Conexión y Credenciales
Se estableció una conexión segura a través de internet utilizando un certificado de seguridad SSL obligatorio (`ca (1).pem`) provisto por Aiven. La cadena de conexión mapeada dentro del archivo de configuración `.env` quedó estructurada bajo el dialecto de SQLAlchemy y el driver `pymysql` con los siguientes parámetros reales:

* **Host:** `mysql-8366427-proyectoturismo.i.aivencloud.com`
* **Puerto:** `24178`
* **Usuario:** `avnadmin`
* **Base de Datos por Defecto:** `defaultdb`
* **Esquema del Proyecto:** `TureservaBD_db`
* **Modo SSL:** `REQUIRED`

---

## 2. Definición del Esquema SQL (`setup_db.sql`)
Se diseñó e implementó un script SQL robusto estructurado para soportar el ciclo de vida de desarrollo. Este incluye la limpieza previa de entidades (controlando la restricción de claves foráneas) y la codificación de caracteres `utf8mb4` para la correcta inserción de textos en español (acentos, eñes).

### Estructura de Tablas Creadas:

1. **`tours`**: Almacena los paquetes o actividades turísticas disponibles.
   * `id` (INT, Clave Primaria, Auto-incremental)
   * `nombre` (VARCHAR(200), Requerido)
   * `descripcion` (TEXT, Opcional)
   * `precio` (DECIMAL(10,2), Requerido)
   * `activo` (TINYINT(1), Predeterminado 1)
   * `creado_en` (DATETIME, Fecha automática del sistema)

2. **`clientes`**: Registra la información de contacto de los usuarios que realizan transacciones.
   * `id` (INT, Clave Primaria, Auto-incremental)
   * `nombre_completo` (VARCHAR(150), Requerido)
   * `correo` (VARCHAR(150), Requerido, Único)
   * `telefono` (VARCHAR(20), Requerido)
   * `nacionalidad` (VARCHAR(100), Opcional)
   * `creado_en` (DATETIME, Fecha automática)

3. **`reservas`**: Entidad relacional pivote que conecta los clientes con las actividades deseadas.
   * `id` (INT, Clave Primaria, Auto-incremental)
   * `cliente_id` (INT, Clave Foránea referenciando a `clientes(id)` con eliminación en cascada)
   * `tour_id` (INT, Clave Foránea referenciando a `tours(id)` con eliminación en cascada)
   * `fecha_tour` (DATE, Requerido)
   * `num_personas` (INT, Predeterminado 1)
   * `metodo_pago` (VARCHAR(50), Requerido)
   * `total` (DECIMAL(10,2), Calculado)
   * `estado` (ENUM('pendiente', 'confirmada', 'cancelada'), Predeterminado 'pendiente')
   * `creado_en` (DATETIME, Fecha automática)

---

## 3. Datos de Prueba Insertados (Seeders)
Como parte de la inyección exitosa de datos para validar el funcionamiento del Backend, se poblaron las tablas con registros reales orientados al sector turístico dominicano:

* **Tours Inyectados:**
  * *Ciudad Colonial*: Recorrido histórico por la Zona Colonial de Santo Domingo.
  * *Isla Saona*: Excursión en catamarán a la paradisíaca Isla Saona con almuerzo incluido.
  * *Cuevas de las Maravillas*: Tour a las cuevas con pinturas rupestres taínas en La Romana.
* **Clientes Iniciales:** Registros de prueba correspondientes a usuarios locales e internacionales (`Pedro Pérez`, `María García`).
* **Reservas Iniciales:** Transacciones de prueba vinculando a los clientes con los tours de la Isla Saona y Ciudad Colonial, computando sus respectivos totales económicos, fechas específicas de ejecución y métodos de pago (`efectivo`, `tarjeta`).

---

## 4. Automatización e Inyección desde Python (`app.py`)
Para asegurar la reproducibilidad del esquema sin depender de herramientas visuales externas, se desarrolló un script en Python que interactúa directamente con el clúster en la nube. 

El script realiza de manera secuencial los siguientes pasos:
1. Instancia las variables de entorno mediante `load_dotenv()`.
2. Configura el motor de base de datos (`create_engine`) inyectando dinámicamente el certificado físico `ca (1).pem` a los argumentos de conexión de la librería subyacente.
3. Abre el archivo de texto estructurado `setup_db.sql` con codificación universal `utf-8`.
4. Segmenta el script secuencialmente utilizando el delimitador de instrucciones de control (`;`).
5. Limpia espacios en blanco, ejecuta cada comando atómicamente dentro de un bloque transaccional seguro y efectúa el `commit()` final en el servidor remoto.
