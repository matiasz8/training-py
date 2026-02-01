#!/usr/bin/env python3
"""
Actualiza todas las referencias/links.md con contenido real.
"""

from pathlib import Path
import re

def generate_references(topic_name: str, module_name: str) -> str:
    """Genera contenido de referencias basado en tema y módulo."""
    
    clean_name = re.sub(r'^\d+_', '', topic_name).replace('_', ' ').title()
    topic_slug = topic_name.lower().replace('_', '-')
    
    # Detectar categoría del módulo
    if "fundamentos" in module_name or "intermedio" in module_name:
        return f"""# Referencias: {clean_name}

## Documentación Oficial de Python
- [Tutorial de Python](https://docs.python.org/es/3/tutorial/index.html)
- [Python Documentation](https://docs.python.org/3/)
- [Python Library Reference](https://docs.python.org/3/library/index.html)

## Tutoriales Recomendados
- [Real Python](https://realpython.com/) - Tutoriales de calidad
- [Python.org Beginners Guide](https://wiki.python.org/moin/BeginnersGuide)
- [W3Schools Python](https://www.w3schools.com/python/)

## Libros Recomendados
- "Python Crash Course" by Eric Matthes
- "Automate the Boring Stuff with Python" by Al Sweigart
- "Fluent Python" by Luciano Ramalho

## Videos y Cursos
- [Python para Todos (Coursera)](https://www.coursera.org/specializations/python)
- [Corey Schafer - Python Tutorials](https://www.youtube.com/user/schafer5)
- [sentdex - Python Programming](https://www.youtube.com/user/sentdex)

## Recursos Interactivos
- [Python Tutor](http://pythontutor.com/) - Visualiza ejecución
- [Exercism Python Track](https://exercism.org/tracks/python)
- [HackerRank Python](https://www.hackerrank.com/domains/python)

## Comunidad
- [r/learnpython](https://www.reddit.com/r/learnpython/)
- [Python Discord](https://discord.gg/python)
- [Stack Overflow - Python Tag](https://stackoverflow.com/questions/tagged/python)
"""
    
    elif "poo" in module_name or "oop" in module_name:
        return f"""# Referencias: {clean_name}

## Documentación Oficial
- [Python Classes Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Python OOP](https://docs.python.org/3/tutorial/classes.html)

## Artículos Técnicos
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
- [Python's super() Explained](https://realpython.com/python-super/)

## Libros
- "Object-Oriented Python" by Irv Kalb
- "Python 3 Object-Oriented Programming" by Dusty Phillips
- "Fluent Python" - Capítulos de OOP

## Videos
- [Corey Schafer - OOP Series](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [PyCon talks sobre OOP](https://www.youtube.com/results?search_query=pycon+oop+python)

## Patrones de Diseño
- [Refactoring Guru](https://refactoring.guru/design-patterns/python)
- [Python Patterns](https://python-patterns.guide/)
"""

    elif "cpython" in module_name or "internals" in module_name:
        return f"""# Referencias: {clean_name}

## Documentación Oficial
- [CPython Internals](https://devguide.python.org/internals/)
- [Python C API](https://docs.python.org/3/c-api/index.html)
- [Python Enhancement Proposals (PEPs)](https://peps.python.org/)

## PEPs Relevantes
- [PEP 703 - Free-threading CPython](https://peps.python.org/pep-0703/)
- [PEP 684 - Per-Interpreter GIL](https://peps.python.org/pep-0684/)
- [PEP 683 - Immortal Objects](https://peps.python.org/pep-0683/)

## Libros Especializados
- "CPython Internals" by Anthony Shaw
- "Python Under the Hood"
- "High Performance Python" by Gorelick & Ozsvald

## Artículos Técnicos
- [Real Python: CPython Internals](https://realpython.com/cpython-source-code-guide/)
- [Python Behind the Scenes](https://tenthousandmeters.com/tag/python-behind-the-scenes/)
- [Understanding GIL](https://realpython.com/python-gil/)

## Código Fuente
- [CPython GitHub](https://github.com/python/cpython)
- [Python Dev Guide](https://devguide.python.org/)

## Videos
- [PyCon: CPython Internals](https://www.youtube.com/results?search_query=pycon+cpython+internals)
- [David Beazley talks](https://www.youtube.com/results?search_query=david+beazley+python)
"""

    elif "concurrencia" in module_name or "async" in module_name:
        return f"""# Referencias: {clean_name}

## Documentación Oficial
- [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [threading Module](https://docs.python.org/3/library/threading.html)
- [multiprocessing Module](https://docs.python.org/3/library/multiprocessing.html)
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)

## PEPs
- [PEP 492 - Coroutines](https://peps.python.org/pep-0492/)
- [PEP 3156 - asyncio](https://peps.python.org/pep-3156/)

## Libros
- "Using Asyncio in Python" by Caleb Hattingh
- "Python Concurrency with asyncio" by Matthew Fowler
- "High Performance Python" - Capítulos de concurrencia

## Artículos
- [Real Python: Async IO](https://realpython.com/async-io-python/)
- [Understanding asyncio](https://realpython.com/python-async-features/)
- [Threading vs Multiprocessing](https://realpython.com/python-concurrency/)

## Videos
- [David Beazley - Python Concurrency](https://www.youtube.com/results?search_query=david+beazley+concurrency)
- [Łukasz Langa - AsyncIO](https://www.youtube.com/results?search_query=lukasz+langa+asyncio)

## Herramientas
- [aiohttp](https://docs.aiohttp.org/)
- [httpx](https://www.python-httpx.org/)
- [trio](https://trio.readthedocs.io/)
"""

    elif "tipado" in module_name or "typing" in module_name:
        return f"""# Referencias: {clean_name}

## Documentación Oficial
- [typing Module](https://docs.python.org/3/library/typing.html)
- [Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## PEPs Fundamentales
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [PEP 544 - Protocols](https://peps.python.org/pep-0544/)
- [PEP 589 - TypedDict](https://peps.python.org/pep-0589/)
- [PEP 585 - Type Hinting Generics](https://peps.python.org/pep-0585/)
- [PEP 604 - Union Operator](https://peps.python.org/pep-0604/)

## Type Checkers
- [mypy Documentation](https://mypy.readthedocs.io/)
- [Pyright](https://github.com/microsoft/pyright)
- [BasedPyright](https://github.com/DetachHead/basedpyright)
- [Pyre](https://pyre-check.org/)

## Artículos
- [Real Python: Type Checking](https://realpython.com/python-type-checking/)
- [Ultimate Guide to Python Type Hints](https://realpython.com/lessons/type-hinting/)

## Libros
- "Fluent Python" - Capítulos sobre typing
- "Robust Python" by Patrick Viafore

## Repos de Ejemplo
- [typeshed](https://github.com/python/typeshed) - Type stubs
- [Awesome Python Typing](https://github.com/typeddjango/awesome-python-typing)
"""

    elif "tooling" in module_name:
        return f"""# Referencias: {clean_name}

## Herramientas Modernas
- [uv](https://github.com/astral-sh/uv) - Package manager ultrarrápido
- [Ruff](https://docs.astral.sh/ruff/) - Linter/formatter en Rust
- [BasedPyright](https://github.com/DetachHead/basedpyright) - Type checker

## Documentación
- [uv Guide](https://github.com/astral-sh/uv/tree/main/docs)
- [Ruff Rules](https://docs.astral.sh/ruff/rules/)
- [pytest Documentation](https://docs.pytest.org/)

## Artículos
- [Astral Blog](https://astral.sh/blog)
- [Python Packaging User Guide](https://packaging.python.org/)

## Comparaciones
- [uv vs pip vs poetry](https://astral.sh/blog/uv)
- [Ruff vs Black vs Pylint](https://docs.astral.sh/ruff/faq/#how-does-ruff-compare-to-black-and-other-formatters)

## Videos
- [Modern Python Tooling](https://www.youtube.com/results?search_query=python+modern+tooling)
- [Charlie Marsh on Ruff & uv](https://www.youtube.com/results?search_query=charlie+marsh+ruff)
"""

    elif "fastapi" in module_name:
        return f"""# Referencias: {clean_name}

## Documentación Oficial
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic V2](https://docs.pydantic.dev/)
- [Starlette](https://www.starlette.io/)
- [Uvicorn](https://www.uvicorn.org/)

## Tutoriales
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Real Python: FastAPI](https://realpython.com/fastapi-python-web-apis/)

## Ejemplos y Templates
- [FastAPI Examples](https://github.com/tiangolo/fastapi/tree/master/docs_src)
- [Full Stack FastAPI Template](https://github.com/tiangolo/full-stack-fastapi-template)

## Artículos
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [Production FastAPI](https://www.youtube.com/results?search_query=fastapi+production)

## Comunidad
- [FastAPI Discussions](https://github.com/tiangolo/fastapi/discussions)
- [FastAPI Discord](https://discord.gg/fastapi)
"""

    elif "patrones" in module_name or "patterns" in module_name:
        return f"""# Referencias: {clean_name}

## Libros Clásicos
- "Design Patterns" - Gang of Four
- "Head First Design Patterns"
- "Python Design Patterns and Best Practices"

## Sitios Web
- [Refactoring Guru](https://refactoring.guru/design-patterns)
- [Python Patterns Guide](https://python-patterns.guide/)
- [SourceMaking](https://sourcemaking.com/design_patterns)

## Implementaciones Python
- [python-patterns](https://github.com/faif/python-patterns)
- [Design Patterns in Python](https://github.com/PacktPublishing/Mastering-Python-Design-Patterns-Second-Edition)

## Artículos
- [Real Python: Design Patterns](https://realpython.com/factory-method-python/)
- Python design patterns en blogs técnicos

## Videos
- [PyCon: Design Patterns](https://www.youtube.com/results?search_query=pycon+design+patterns)
- [ArjanCodes](https://www.youtube.com/c/ArjanCodes) - Patterns y arquitectura
"""

    elif "security" in module_name:
        return f"""# Referencias: {clean_name}

## Estándares
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

## Herramientas
- [Sigstore](https://www.sigstore.dev/)
- [SOPS](https://github.com/mozilla/sops)
- [HashiCorp Vault](https://www.vaultproject.io/)
- [Trivy](https://github.com/aquasecurity/trivy)
- [Bandit](https://bandit.readthedocs.io/)

## Documentación
- [Python Security](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [OWASP Python Security Project](https://owasp.org/www-project-python-security/)

## Artículos
- [Real Python: Security](https://realpython.com/tutorials/security/)
- [Snyk Learn Python Security](https://learn.snyk.io/catalog/?type=security-rules&languages=python)

## Comunidad
- [r/netsec](https://www.reddit.com/r/netsec/)
- [OWASP Slack](https://owasp.org/slack/invite)
"""

    elif "avanzado" in module_name or "pyo3" in topic_name:
        return f"""# Referencias: {clean_name}

## PyO3 y Rust
- [PyO3 Guide](https://pyo3.rs/)
- [Maturin](https://maturin.rs/)
- [The Rust Book](https://doc.rust-lang.org/book/)

## AI/LLM Development
- [LangChain](https://python.langchain.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [OpenAI Cookbook](https://cookbook.openai.com/)

## Artículos
- [Rust + Python](https://blog.logrocket.com/rust-and-python-interoperability-pyo3/)
- [Building Python Extensions in Rust](https://depth-first.com/articles/2020/08/10/python-extensions-in-pure-rust-with-pyo3/)

## Videos
- [PyO3 tutorials](https://www.youtube.com/results?search_query=pyo3+rust+python)
- [LangChain tutorials](https://www.youtube.com/c/LangChain)
"""

    else:
        # Generic template
        return f"""# Referencias: {clean_name}

## Documentación Oficial de Python
- [Python Documentation](https://docs.python.org/3/)
- [Python HOWTOs](https://docs.python.org/3/howto/index.html)
- [Python FAQs](https://docs.python.org/3/faq/index.html)

## Tutoriales
- [Real Python](https://realpython.com/)
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)

## Libros Recomendados
- "Fluent Python" by Luciano Ramalho
- "Effective Python" by Brett Slatkin
- "Python Cookbook" by David Beazley

## Videos
- [PyCon Talks](https://www.youtube.com/results?search_query=pycon+{topic_slug})
- [Talk Python Podcast](https://talkpython.fm/)

## Comunidad
- [r/Python](https://www.reddit.com/r/Python/)
- [Python Discord](https://discord.gg/python)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
"""


def update_references(base_path: Path):
    """Actualiza todos los archivos references/links.md."""
    
    updated = 0
    modules = sorted([d for d in base_path.iterdir() if d.is_dir() and d.name[0].isdigit()])
    
    for module in modules:
        module_name = module.name
        
        # Patrones tiene subcategorías
        if "patrones" in module_name:
            subcats = [d for d in module.iterdir() if d.is_dir()]
            for subcat in subcats:
                topics = [t for t in subcat.iterdir() if t.is_dir()]
                for topic in topics:
                    refs_file = topic / "references" / "links.md"
                    if refs_file.exists():
                        content = refs_file.read_text()
                        if "*[Por añadir]*" in content or "Por añadir" in content:
                            new_content = generate_references(topic.name, module_name)
                            refs_file.write_text(new_content)
                            updated += 1
                            print(f"✓ {module.name}/{subcat.name}/{topic.name}")
        else:
            topics = [t for t in module.iterdir() if t.is_dir()]
            for topic in topics:
                refs_file = topic / "references" / "links.md"
                if refs_file.exists():
                    content = refs_file.read_text()
                    if "*[Por añadir]*" in content or "Por añadir" in content:
                        new_content = generate_references(topic.name, module_name)
                        refs_file.write_text(new_content)
                        updated += 1
                        print(f"✓ {module.name}/{topic.name}")
    
    return updated


def main():
    base = Path(__file__).parent.parent
    print("📚 Actualizando referencias...")
    updated = update_references(base)
    print(f"\n✅ {updated} archivos de referencias actualizados")


if __name__ == "__main__":
    main()
