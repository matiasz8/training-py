# Type Hints Básicos - Referencias y Recursos

## Documentación Oficial

### Python Docs

- [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
- [Type Hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Annotations Best Practices](https://docs.python.org/3/howto/annotations.html)

### PEPs (Python Enhancement Proposals)

- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/) - Propuesta original de type hints
- [PEP 526 – Syntax for Variable Annotations](https://peps.python.org/pep-0526/) - Anotaciones de variables
- [PEP 585 – Type Hinting Generics In Standard Collections](https://peps.python.org/pep-0585/) - `list[int]` en lugar de `List[int]`
- [PEP 604 – Allow writing union types as X | Y](https://peps.python.org/pep-0604/) - Sintaxis de union con `|`
- [PEP 612 – Parameter Specification Variables](https://peps.python.org/pep-0612/) - ParamSpec para decoradores
- [PEP 613 – Explicit Type Aliases](https://peps.python.org/pep-0613/) - TypeAlias explícito

## Type Checkers

### mypy

- [mypy Documentation](http://mypy-lang.org/)
- [mypy GitHub Repository](https://github.com/python/mypy)
- [Getting Started with mypy](https://mypy.readthedocs.io/en/stable/getting_started.html)
- [Common Issues and Solutions](https://mypy.readthedocs.io/en/stable/common_issues.html)

### Pyright / Pylance

- [Pyright GitHub](https://github.com/microsoft/pyright)
- [Pyright Documentation](https://microsoft.github.io/pyright/)
- [Pylance VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

### basedpyright

- [basedpyright GitHub](https://github.com/DetachHead/basedpyright)
- Community fork con features adicionales

## Artículos y Tutoriales

### Real Python

- [Python Type Checking (Guide)](https://realpython.com/python-type-checking/)
- [Type Hinting in Python](https://realpython.com/lessons/type-hinting/)
- [Protocols and Structural Subtyping](https://realpython.com/python-protocols/)

### Blogs Técnicos

- [Dropbox - Our journey to type checking 4 million lines of Python](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python)
- [Instagram - Static Analysis at Scale](https://instagram-engineering.com/static-analysis-at-scale-an-instagram-story-8f498ab71a0c)
- [Microsoft - Python Type Hints](https://devblogs.microsoft.com/python/python-type-hints-in-visual-studio-code/)

## Videos y Talks

### PyCon Talks

- Carl Meyer - Type-checked Python in the Real World (PyCon 2018)
- Łukasz Langa - Let's Talk About Type Hints (PyCon 2019)
- Shannon Zhu - Type Hints: The Series (PyCon 2020)

## Repositorios de Ejemplo

### Proyectos que usan type hints extensivamente

- [FastAPI](https://github.com/tiangolo/fastapi) - Framework web moderno con type hints en el core
- [Pydantic](https://github.com/pydantic/pydantic) - Validación de datos basada en type hints
- [SQLModel](https://github.com/tiangolo/sqlmodel) - ORM que combina SQLAlchemy y Pydantic
- [returns](https://github.com/dry-python/returns) - Programación funcional con types fuertes
- [typeshed](https://github.com/python/typeshed) - Stubs de type hints para la stdlib

### Herramientas útiles

- [monkeytype](https://github.com/Instagram/MonkeyType) - Genera type hints automáticamente desde código en ejecución
- [pytype](https://github.com/google/pytype) - Type checker de Google con inferencia de tipos
- [pyre-check](https://github.com/facebook/pyre-check) - Type checker de Facebook
