#!/usr/bin/env python3
"""
Script para generar estructura básica de módulos y temas.

Este script crea la estructura de carpetas y archivos README básicos
para todos los módulos del proyecto Python Erudito.
"""

from pathlib import Path
from typing import List, Dict

# Definición de todos los módulos y sus temas
MODULES = {
    "01_fundamentos_python": {
        "description": "Fundamentos de Python",
        "topics": [
            "variables_tipos_datos_optional",
            "operadores_expresiones_optional",
            "estructuras_control",
            "listas_tuplas",
            "diccionarios_sets",
            "funciones_basicas",
            "comprehensions",
            "strings_avanzado",
            "input_output_optional",
            "importaciones_modulos",
            "manejo_errores_basico",
            "debugging_basico_optional",
        ]
    },
    "02_python_intermedio": {
        "description": "Python Intermedio",
        "topics": [
            "funciones_avanzadas",
            "decoradores_basicos",
            "closures",
            "manejo_archivos_texto",
            "csv_json",
            "manejo_excepciones",
            "context_managers_basicos",
            "iteradores_basicos",
            "generadores",
            "modulos_paquetes",
            "pathlib",
            "datetime_time",
            "collections_module",
            "itertools",
            "regex_optional",
        ]
    },
    "03_poo_basica_intermedia": {
        "description": "POO Básica e Intermedia",
        "topics": [
            "clases_objetos",
            "atributos_metodos",
            "init_self",
            "herencia_basica",
            "herencia_multiple",
            "polimorfismo",
            "encapsulacion",
            "metodos_especiales",
            "properties",
            "descriptores_basicos",
            "composicion_vs_herencia",
            "dataclasses_optional",
        ]
    },
    "05_concurrencia_moderna": {
        "description": "Concurrencia y Paralelismo Moderno",
        "topics": [
            "modelos_concurrencia",
            "threading_basico",
            "threading_freethreading",
            "thread_pools",
            "locks_semaphores",
            "barriers_events",
            "subinterpreters_uso",
            "comunicacion_subinterpreters",
            "multiprocessing_basico",
            "shared_memory",
            "process_pools",
            "asyncio_fundamentos",
            "event_loop_internals",
            "coroutines_async_await",
            "asyncio_patterns",
            "taskgroups",
            "asyncio_streams",
            "aiohttp_httpx",
            "asyncio_debugging",
            "producer_consumer",
            "pipeline_paralelo",
            "map_reduce",
            "actor_model",
            "race_detection",
            "profiling_concurrent",
        ]
    },
    "06_tipado_metaprogramacion": {
        "description": "Tipado Estático y Metaprogramación",
        "topics": [
            "type_hints_basicos",
            "typing_avanzado",
            "generics_typevar",
            "protocol_structural_typing",
            "typeddict_namedtuple",
            "union_optional",
            "literal_types",
            "overload",
            "mypy_basico",
            "runtime_type_checking",
            "metaclases_intro",
            "metaclases_avanzadas",
            "init_subclass",
            "set_name_descriptor",
            "descriptores_avanzados",
            "abstract_base_classes",
            "class_decorators",
            "dynamic_classes",
            "introspection_inspect",
            "ast_basics",
            "ast_manipulation",
            "exec_eval_compile",
        ]
    },
    "08_arquitectura_aplicaciones": {
        "description": "Arquitectura de Aplicaciones",
        "topics": [
            "solid_principles",
            "single_responsibility",
            "open_closed",
            "liskov_substitution",
            "interface_segregation",
            "dependency_inversion",
            "dependency_injection",
            "inversion_control",
            "ddd_intro",
            "entities_value_objects",
            "repositories",
            "services_uow",
            "hexagonal_architecture",
            "ports_adapters",
            "event_driven_arch",
            "cqrs_pattern",
            "logging_estructurado",
            "observabilidad",
        ]
    },
    "09_testing_qa": {
        "description": "Testing y Quality Assurance",
        "topics": [
            "pytest_fundamentos",
            "fixtures",
            "parametrize",
            "mocking_unittest",
            "pytest_mock",
            "coverage_analysis",
            "hypothesis_intro",
            "property_based_testing",
            "mutation_testing",
            "pytest_asyncio",
            "integration_testing",
            "contract_testing",
            "tdd_basics",
            "bdd_behave_optional",
            "test_organization",
            "ci_testing",
        ]
    },
    "10_performance_optimizacion": {
        "description": "Performance y Optimización",
        "topics": [
            "profiling_cprofile",
            "line_profiler",
            "pyspy_profiling",
            "benchmarking_timeit",
            "pytest_benchmark",
            "optimization_techniques",
            "cython_basics",
            "numpy_vectorization",
            "numba_jit",
            "pypy_intro",
            "lazy_evaluation",
            "caching_lru",
            "memory_optimization",
            "algorithmic_complexity",
        ]
    },
    "12_fastapi_completo": {
        "description": "FastAPI Completo",
        "topics": [
            "fastapi_intro",
            "routing",
            "path_query_params",
            "request_body",
            "pydantic_models",
            "dependency_injection",
            "response_models",
            "file_uploads",
            "background_tasks",
            "websockets",
            "middleware",
            "cors",
            "authentication_jwt",
            "oauth2",
            "security_best_practices",
            "openapi_customization",
            "testing_fastapi",
            "sqlalchemy_integration",
            "async_databases",
            "alembic_migrations",
            "fastapi_performance",
            "uvicorn_gunicorn",
            "rate_limiting",
            "redis_caching",
            "logging_monitoring",
            "error_handling",
            "graphql_optional",
            "deployment",
        ]
    },
    "13_ecosistema_backend": {
        "description": "Ecosistema Backend Moderno",
        "topics": [
            "sqlalchemy_2_intro",
            "sqlalchemy_async",
            "postgresql_advanced",
            "redis_basics",
            "redis_patterns",
            "redis_pubsub",
            "rabbitmq_basics",
            "kafka_basics",
            "celery_intro",
            "arq_async_tasks",
            "grpc_intro",
            "protobuf",
            "rest_api_design",
            "api_versioning",
            "configuration_management",
            "structured_logging",
            "opentelemetry",
            "prometheus_metrics",
            "elasticsearch_optional",
            "graphql_schemas_optional",
        ]
    },
    "15_data_science_basico": {
        "description": "Data Science Básico",
        "topics": [
            "numpy_basics",
            "pandas_intro",
            "pandas_operations",
            "matplotlib_basics",
            "seaborn_viz",
            "data_cleaning",
            "exploratory_analysis",
            "jupyter_notebooks_optional",
            "pandas_performance",
            "polars_intro",
        ]
    },
}


def create_topic_structure(base_path: Path, topic_name: str) -> None:
    """Crea estructura de carpetas para un tema."""
    topic_path = base_path / topic_name
    topic_path.mkdir(parents=True, exist_ok=True)
    
    # Crear subcarpetas
    (topic_path / "examples").mkdir(exist_ok=True)
    (topic_path / "exercises").mkdir(exist_ok=True)
    (topic_path / "tests").mkdir(exist_ok=True)
    (topic_path / "my_solution").mkdir(exist_ok=True)
    (topic_path / "references").mkdir(exist_ok=True)
    
    # Crear README básico
    readme_content = f"""# {topic_name.replace('_', ' ').title()}

⏱️ **Tiempo estimado: 2-3 horas**

## 1. 📚 Definición

*[Por completar: 200-300 palabras explicando el concepto técnicamente]*

## 2. 💡 Aplicación Práctica

### Casos de Uso

1. **Caso 1**: 
2. **Caso 2**: 
3. **Caso 3**: 

### Código Ejemplo

```python
# TODO: Añadir ejemplo
```

## 3. 🤔 ¿Por Qué Es Importante?

*[Por completar: Problema que resuelve, historia, inspiración]*

## 4. 🔗 Referencias

- [Documentación oficial de Python](https://docs.python.org/)
- [PEP relevante]()
- [Artículo técnico]()

## 5. ✏️ Tarea de Práctica

### Nivel Básico
*[Por completar]*

### Nivel Intermedio
*[Por completar]*

### Nivel Avanzado
*[Por completar]*

## 6. 📝 Summary

- Punto clave 1
- Punto clave 2
- Punto clave 3

## 7. 🧠 Mi Análisis Personal

> ✍️ **Espacio para tu reflexión**
>
> Escribe aquí tus observaciones, dudas y conclusiones después de completar este tema...
"""
    
    readme_path = topic_path / "README.md"
    if not readme_path.exists():
        readme_path.write_text(readme_content)
    
    # Crear archivo de referencias básico
    links_content = f"""# Referencias: {topic_name.replace('_', ' ').title()}

## Documentación Oficial
- [Python Docs](https://docs.python.org/)

## Artículos
- *[Por añadir]*

## Videos
- *[Por añadir]*

## Repositorios de Ejemplo
- *[Por añadir]*
"""
    
    links_path = topic_path / "references" / "links.md"
    if not links_path.exists():
        links_path.write_text(links_content)


def create_module(base_path: Path, module_name: str, module_info: Dict) -> None:
    """Crea estructura completa de un módulo."""
    module_path = base_path / module_name
    module_path.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Creando módulo: {module_name}")
    
    # Crear README del módulo
    readme_content = f"""# Módulo: {module_info['description']}

## 📋 Descripción

*[Por completar: Descripción general del módulo]*

## 🎯 Objetivos de Aprendizaje

- Objetivo 1
- Objetivo 2
- Objetivo 3

## 📚 Contenido ({len(module_info['topics'])} Temas)

"""
    
    for i, topic in enumerate(module_info['topics'], 1):
        topic_title = topic.replace('_', ' ').title()
        readme_content += f"{i}. [{topic_title}]({topic}/)\n"
    
    readme_content += f"""
## ⏱️ Tiempo Estimado Total

**{len(module_info['topics']) * 2}-{len(module_info['topics']) * 3} horas**

## 🚀 Orden Recomendado

Seguir el orden numérico para una progresión lógica.
"""
    
    readme_path = module_path / "README.md"
    if not readme_path.exists():
        readme_path.write_text(readme_content)
    
    # Crear cada tema
    for topic in module_info['topics']:
        create_topic_structure(module_path, topic)
        print(f"  ✓ {topic}")


def main():
    """Genera estructura completa del proyecto."""
    base_path = Path(__file__).parent.parent
    
    print("🚀 Generando estructura de módulos...")
    print()
    
    for module_name, module_info in MODULES.items():
        create_module(base_path, module_name, module_info)
        print()
    
    print("✅ Estructura generada exitosamente!")
    print()
    print("📝 Próximos pasos:")
    print("   1. Revisa los módulos creados")
    print("   2. Completa los READMEs con contenido")
    print("   3. Añade ejemplos y ejercicios")
    print("   4. Ejecuta: uv run scripts/progress.py")


if __name__ == "__main__":
    main()
