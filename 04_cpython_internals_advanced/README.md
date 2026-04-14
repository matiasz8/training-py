# Módulo 04 - CPython Internals Avanzado

## Descripción General

Este módulo profundiza en los aspectos más avanzados de CPython, enfocándose en la evolución del Global Interpreter Lock (GIL), la nueva arquitectura free-threading introducida en Python 3.13 (PEP 703), subinterpreters (PEP 684), y el manejo interno de memoria y objetos.

## Objetivos de Aprendizaje

- Comprender la historia y limitaciones del GIL
- Dominar la nueva arquitectura free-threading de Python 3.13+
- Trabajar con subinterpreters y aislamiento de memoria
- Entender el reference counting y garbage collection thread-safe
- Implementar código thread-safe en entornos sin GIL
- Conocer la estructura interna de PyObject y optimizaciones de memoria

## Estructura del Módulo

### Sección 1: Global Interpreter Lock (GIL)
1. [Historia del GIL](01_gil_history/)
2. [Limitaciones del GIL tradicional](02_gil_limitations/)

### Sección 2: Free-Threading (PEP 703)
3. [PEP 703: Free-Threading Python 3.13+](03_pep_703_free_threading/)
4. [Activación de free-threading](04_free_threading_activation/)
5. [Arquitectura interna sin GIL](05_gil_free_architecture/)
6. [Biased reference counting](06_biased_reference_counting/)
7. [Garbage collector thread-safe](07_gc_thread_safe/)
8. [Performance benchmarks: GIL vs No-GIL](08_performance_benchmarks/)
9. [Compatibilidad de extensiones C](09_c_extensions_compatibility/)

### Sección 3: Subinterpreters (PEP 684)
10. [Subinterpreters - Introducción](10_subinterpreters_intro/)
11. [API C de subinterpreters](11_api_c_subinterpreters/)
12. [API Python de subinterpreters](12_api_python_subinterpreters/)
13. [Per-interpreter GIL vs No-GIL](13_per_interpreter_gil/)
14. [Aislamiento de memoria](14_memory_isolation/)
15. [Canales de comunicación](15_communication_channels/)

### Sección 4: Thread-Safety
16. [Operaciones atómicas](16_atomic_operations/)
17. [Data races y race conditions](17_data_races/)
18. [Locks y sincronización](18_locks_synchronization/)
19. [Threading.local y TLS](19_threading_local/)
20. [Estructuras thread-safe](20_thread_safe_structures/)

### Sección 5: Internals de Objetos
21. [PyObject: estructura interna](21_pyobject_structure/)
22. [Reference counting avanzado](22_reference_counting/)
23. [Immortal objects (PEP 683)](23_immortal_objects/)
24. [Caching y interning](24_caching_interning/)
25. [Memory layout y compaction](25_memory_layout/)

### Sección 6: Migración y Testing
26. [Estrategias de migración](26_migration_strategies/)
27. [Testing de thread-safety](27_testing_thread_safety/)

## Requisitos Previos

- Python 3.13+ compilado con free-threading
- Conocimiento de threading en Python
- Familiaridad con C/C++ (básico)
- Experiencia con pytest

## Tiempo Estimado

⏱️ **Total: 80-110 horas** (aproximadamente 3-4 horas por tema)

## Referencias Principales

- [PEP 703 – Making the Global Interpreter Lock Optional](https://peps.python.org/pep-0703/)
- [PEP 684 – A Per-Interpreter GIL](https://peps.python.org/pep-0684/)
- [PEP 683 – Immortal Objects](https://peps.python.org/pep-0683/)
- [Python 3.13 Free-Threading Documentation](https://docs.python.org/3.13/howto/free-threading-python.html)
- [CPython Internals Book](https://realpython.com/products/cpython-internals-book/)
