#!/usr/bin/env python3
"""
Servidor de Herramientas MCP para la ECI

Este módulo crea un servidor MCP con herramientas para consultar información
sobre los cursos de la Escuela Complutense de Informática (ECI) 2025
y las expone a través de la interfaz HTTP de streaming de FastMCP en localhost:8080/mcp
"""

import asyncio
from typing import Any, Literal
from fastmcp import FastMCP
from pydantic import BaseModel
import uvicorn


# Datos de los cursos ECI 2025
CURSOS_ECI_2025 = {
    "M1": {
        "titulo": "Análisis Probabilístico de Algoritmos",
        "instructor": "Pablo Rotondo",
        "horario": "Mañana (9 a 12 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso sobre análisis probabilístico de algoritmos destinado a estudiantes y profesionales de carreras informáticas."
    },
    "M2": {
        "titulo": "The Evolution of Blockchain Technologies",
        "instructor": "Andrea Vitaletti",
        "horario": "Mañana (9 a 12 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso sobre la evolución de las tecnologías blockchain y sus aplicaciones."
    },
    "M3": {
        "titulo": "Modelos generativos de imágenes basados en redes profundas",
        "instructor": "Pablo Musé",
        "horario": "Mañana (9 a 12 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso sobre modelos generativos para crear imágenes usando redes neuronales profundas."
    },
    "T1": {
        "titulo": "Interactive theorem provers: theory and practice",
        "instructor": "Paige Randall North",
        "horario": "Tarde (13:30 a 16:30 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso sobre demostradores de teoremas interactivos, teoría y práctica."
    },
    "T2": {
        "titulo": "Introducción a la computación cuántica",
        "instructor": "Rolando Somma",
        "horario": "Tarde (13:30 a 16:30 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso introductorio a los conceptos fundamentales de la computación cuántica."
    },
    "T3": {
        "titulo": "Procesamiento de imágenes con aplicación a la biomedicina",
        "instructor": "Federico Lecumberry",
        "horario": "Tarde (13:30 a 16:30 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso sobre técnicas de procesamiento de imágenes aplicadas al campo biomédico."
    },
    "N1": {
        "titulo": "Introduction to Column Generation and VRPSolver",
        "instructor": "Teobaldo Bulhões",
        "horario": "Noche (18 a 21 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso sobre generación de columnas y el solver VRP para problemas de optimización."
    },
    "N2": {
        "titulo": "De la planificación no determinista a la síntesis y planificación generalizada",
        "instructor": "Sebastián Sardina",
        "horario": "Noche (18 a 21 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso sobre planificación no determinista y técnicas de síntesis en inteligencia artificial."
    },
    "N3": {
        "titulo": "AI for Immersive Technologies: Enhancing Virtual and Augmented Realities",
        "instructor": "Francesco Strada",
        "horario": "Noche (18 a 21 hs)",
        "periodo": "del lunes 28 de julio al viernes 1 de agosto",
        "descripcion": "Curso sobre inteligencia artificial aplicada a tecnologías inmersivas, realidad virtual y aumentada."
    }
}


# Crear instancia del servidor FastMCP
mcp = FastMCP("herramientas-eci-mcp")


@mcp.tool
def listar_cursos_eci() -> str:
    """Listar todos los cursos disponibles en la ECI 2025."""
    resultado = "📚 CURSOS ECI 2025\n"
    resultado += "=" * 50 + "\n"
    resultado += "Período: del lunes 28 de julio al viernes 1 de agosto\n"
    resultado += "Destinados a estudiantes y profesionales de carreras informáticas y afines.\n\n"
    
    # Agrupar por horario
    horarios = {}
    for codigo, curso in CURSOS_ECI_2025.items():
        horario = curso["horario"]
        if horario not in horarios:
            horarios[horario] = []
        horarios[horario].append((codigo, curso))
    
    for horario, cursos in horarios.items():
        resultado += f"🕐 {horario}\n"
        resultado += "-" * 30 + "\n"
        for codigo, curso in cursos:
            resultado += f"• {curso['titulo']} ({codigo})\n"
            resultado += f"  Instructor: {curso['instructor']}\n\n"
    
    resultado += "💡 Usa 'obtener_detalle_curso' con el código para más información sobre un curso específico."
    return resultado


@mcp.tool
def obtener_detalle_curso(codigo_curso: str) -> str:
    """Obtener detalles específicos de un curso de la ECI 2025."""
    if codigo_curso not in CURSOS_ECI_2025:
        cursos_disponibles = ", ".join(CURSOS_ECI_2025.keys())
        return f"Error: Curso '{codigo_curso}' no encontrado.\n\nCursos disponibles: {cursos_disponibles}"
    
    curso = CURSOS_ECI_2025[codigo_curso]
    resultado = f"📖 DETALLE DEL CURSO\n"
    resultado += "=" * 40 + "\n"
    resultado += f"Título: {curso['titulo']} ({codigo_curso})\n"
    resultado += f"Instructor: {curso['instructor']}\n"
    resultado += f"Horario: {curso['horario']}\n"
    resultado += f"Período: {curso['periodo']}\n\n"
    resultado += f"Descripción:\n{curso['descripcion']}\n\n"
    resultado += "📍 Más información: https://eci.dc.uba.ar/cursos-eci/"
    
    return resultado


async def main():
    """Función principal para ejecutar el servidor."""
    print("🚀 Iniciando Servidor de Herramientas MCP para la ECI")
    print("📡 El servidor estará disponible en: http://localhost:8080/mcp")
    print("🛠️  Herramientas disponibles:")
    print("   • listar_cursos_eci: Lista todos los cursos ECI 2025")
    print("   • obtener_detalle_curso: Obtiene detalles de un curso específico")
    print("⏹️  Presiona Ctrl+C para detener el servidor")
    
    # Ejecutar el servidor usando HTTP de streaming
    await mcp.run_http_async(
        host="localhost",
        port=8080,
        path="/mcp"
    )


if __name__ == "__main__":
    asyncio.run(main())
