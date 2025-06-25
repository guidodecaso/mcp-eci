# Herramientas MCP para la ECI

Este proyecto proporciona herramientas MCP (Protocolo de Contexto de Modelo) para consultar información sobre los cursos de la Escuela Complutense de Informática (ECI) 2025, usando el SDK oficial de Python y exponiéndolas a través de la interfaz HTTP de streaming de FastMCP.

## Características

- **Herramientas ECI 2025**: Consulta información completa sobre los cursos de la ECI
  - Lista todos los cursos organizados por horario
  - Obtiene detalles específicos de cada curso
- Streaming HTTP vía FastMCP en `localhost:8080/mcp`
- Gestión de proyecto Python basada en UV
- Datos de cursos actualizados para la edición 2025

## Configuración

1. Instalar dependencias:
```bash
uv sync
```

2. Ejecutar el servidor:
```bash
uv run python main.py
```

3. Acceder a las herramientas MCP vía HTTP en `http://localhost:8080/mcp`

## Uso

El servidor expone herramientas MCP que pueden ser accedidas por clientes MCP a través de la interfaz de streaming HTTP. Las herramientas están disponibles en el endpoint `/mcp` en el puerto 8080.

## Herramientas Disponibles

### ECI 2025
- `listar_cursos_eci`: Lista todos los cursos disponibles en la ECI 2025, organizados por horario
- `obtener_detalle_curso`: Obtiene información detallada de un curso específico usando su código (M1, M2, M3, T1, T2, T3, N1, N2, N3)

## Cursos ECI 2025

Los cursos se realizan **del lunes 28 de julio al viernes 1 de agosto**, destinados a estudiantes y profesionales de carreras informáticas y afines.

### Horarios y Códigos
- **Mañana (9 a 12 hs)**: M1, M2, M3
- **Tarde (13:30 a 16:30 hs)**: T1, T2, T3  
- **Noche (18 a 21 hs)**: N1, N2, N3

### Temas Incluidos
- Análisis probabilístico de algoritmos
- Tecnologías blockchain
- Modelos generativos de imágenes
- Demostradores de teoremas interactivos
- Computación cuántica
- Procesamiento de imágenes biomédicas
- Generación de columnas y optimización
- Planificación no determinista
- IA para tecnologías inmersivas (VR/AR)

Para más información oficial: https://eci.dc.uba.ar/cursos-eci/
