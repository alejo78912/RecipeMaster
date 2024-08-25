# RecipeMaster

**RecipeMaster** es una aplicación diseñada para ayudar a los usuarios a organizar sus recetas de cocina, planificar menús semanales, generar listas de compras basadas en las recetas seleccionadas y sugerir recetas según los ingredientes disponibles en su inventario.

## Arquitectura

- **Contenerización:** La aplicación está completamente contenerizada utilizando Docker, lo que facilita su despliegue y escalabilidad.
- **Backend:** Desarrollado en Python utilizando FastAPI para un rendimiento óptimo y facilidad de integración.
- **Base de Datos:** Utiliza MySQL para gestionar y almacenar de forma eficiente la información de usuarios, recetas, menús y más.
- **Frontend:** Desarrollado en Angular, proporcionando una interfaz de usuario moderna, interactiva y responsiva.
- **Infraestructura en la Nube:** AWS se utiliza para algunas funciones clave, optimizando la disponibilidad y el rendimiento de la aplicación.



## Microservicios Principales

### 1. Gestión de Usuarios
- **Funciones:** Registro, autenticación, y gestión de perfiles de usuarios.
- **Características:** 
  - Registro y autenticación de usuarios (JWT o OAuth2).
  - Gestión de perfiles, roles y permisos, incluyendo cuentas familiares o grupales.

### 2. Gestión de Recetas
- **Funciones:** Crear, editar, y buscar recetas con ingredientes, instrucciones y datos nutricionales.
- **Características:**
  - Categorización de recetas (tipo de comida, dificultad, etc.).
  - Búsqueda y filtrado de recetas.
  - Compartir recetas y gestionar su visibilidad (públicas/privadas).

### 3. Planificación de Menús
- **Funciones:** Ayudar en la planificación de comidas diarias o semanales.
- **Características:**
  - Selección de recetas para días específicos.
  - Creación de menús recurrentes.
  - Visualización de menús en un calendario y notificaciones.

### 4. Generación de Listas de Compras
- **Funciones:** Crear listas de compras basadas en los ingredientes de las recetas seleccionadas.
- **Características:**
  - Compilación automática y categorización de ingredientes.
  - Integración con servicios de compra en línea.
  - Marcar ingredientes como comprados o disponibles en la despensa.

### 5. Notificaciones
- **Funciones:** Enviar notificaciones relacionadas con menús, listas de compras, y recordatorios.
- **Características:**
  - Recordatorios de compras y preparación de comidas.
  - Alertas sobre la caducidad de productos en la despensa.

### 6. Gestión de Despensa
- **Funciones:** Mantener un inventario de los ingredientes disponibles en casa.
- **Características:**
  - Registro y seguimiento de productos en la despensa.
  - Sugerencias automáticas de recetas basadas en los ingredientes disponibles.

### 7. Sugerencias de Recetas Basadas en Ingredientes Disponibles
- **Funciones:** Sugerir recetas que se pueden preparar con los ingredientes disponibles en el inventario.
- **Características:**
  - Filtrado de recetas por categoría, tipo de comida, y tiempo de preparación.
  - Indicaciones de ingredientes faltantes y opción de marcar recetas favoritas.

## Escenarios de Uso

- **Agregar Ingredientes al Inventario:** Los usuarios pueden registrar los ingredientes que tienen en casa, incluyendo cantidades.
- **Buscar Recetas:** Consultar recetas que se pueden preparar con los ingredientes disponibles, con la opción de filtrar por diferentes criterios.
- **Planificación de Menú:** Planificar menús semanales utilizando las recetas sugeridas y generar listas de compras para los ingredientes faltantes.
## Tech Stack

**Client:** Angular

**Server:** Python, FastAPI

**Database:** MySQL

**Infrastructure:** Docker, AWS
