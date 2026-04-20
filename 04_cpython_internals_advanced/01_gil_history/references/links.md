# Referencias y Enlaces - Historia del GIL

## Documentación Oficial de Python

### CPython Documentation

- [Python 3.13 What's New](https://docs.python.org/3.13/whatsnew/3.13.html) - Free-threading y cambios del GIL
- [Python C API: Thread State and the GIL](https://docs.python.org/3/c-api/init.html#thread-state-and-the-global-interpreter-lock)
- [Python C API: Releasing the GIL](https://docs.python.org/3/c-api/init.html#releasing-the-gil-from-extension-code)
- [threading — Thread-based parallelism](https://docs.python.org/3/library/threading.html)
- [multiprocessing — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html)

### PEPs Relacionados

- [PEP 703 – Making the Global Interpreter Lock Optional](https://peps.python.org/pep-0703/) - **Fundamental**
- [PEP 684 – A Per-Interpreter GIL](https://peps.python.org/pep-0684/)
- [PEP 683 – Immortal Objects](https://peps.python.org/pep-0683/)
- [PEP 554 – Multiple Interpreters in the Stdlib](https://peps.python.org/pep-0554/)

## Artículos y Tutoriales

### Real Python

- [What is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)
- [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)
- [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)

### David Beazley (GIL Expert)

- [Understanding the Python GIL (2010)](http://www.dabeaz.com/GIL/)
- [Inside the Python GIL (Slides)](http://www.dabeaz.com/python/UnderstandingGIL.pdf) - **Lectura esencial**
- [GIL Visualization](http://www.dabeaz.com/python/GIL.pdf)

### Sam Gross (nogil/PEP 703 Author)

- [nogil - A free-threaded Python](https://github.com/colesbury/nogil)
- [Python without the GIL (PyCon US 2023)](https://www.youtube.com/watch?v=HcGlf85rr2w)
- [PEP 703 Discussion Thread](https://discuss.python.org/t/pep-703-making-the-global-interpreter-lock-optional/21444)

### Larry Hastings (Gilectomy)

- [The Gilectomy - Removing the GIL](https://lwn.net/Articles/689548/)
- [Gilectomy GitHub Repository](https://github.com/larryhastings/gilectomy)

## Libros

### CPython Internals

- [CPython Internals by Anthony Shaw](https://realpython.com/products/cpython-internals-book/)
- [High Performance Python by Micha Gorelick & Ian Ozsvald](https://www.oreilly.com/library/view/high-performance-python/9781492055013/)
- [Fluent Python by Luciano Ramalho](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) - Chapter sobre Concurrency

## Papers Académicos

### Investigación Original

- Beazley, D. (2010). "Understanding the Python GIL". PyCon 2010.
- Gross, S. (2023). "Making the Global Interpreter Lock Optional in CPython". PEP 703.

### Concurrencia y Paralelismo

- Herlihy, M., & Shavit, N. (2008). "The Art of Multiprocessor Programming"
- Sutter, H. (2005). "The Free Lunch Is Over: A Fundamental Turn Toward Concurrency"

## Videos y Conferencias

### PyCon Talks

- [David Beazley - Understanding the Python GIL (PyCon 2010)](https://www.youtube.com/watch?v=Obt-vMVdM8s) - **Clásico**
- [Sam Gross - Python without the GIL (PyCon US 2023)](https://www.youtube.com/watch?v=HcGlf85rr2w)
- [Larry Hastings - Gilectomy (PyCon 2016)](https://www.youtube.com/watch?v=pLqv11ScGsQ)

### Otros Videos Educativos

- [ArjanCodes - Python GIL Explained](https://www.youtube.com/watch?v=XVcRQ6T9RHo)
- [mCoding - The Python GIL, Subinterpreters, and Free-Threading](https://www.youtube.com/watch?v=7RNbIEJvjUA)

## Repositorios GitHub

### CPython

- [python/cpython](https://github.com/python/cpython) - Código fuente oficial
- [python/cpython - Include/internal/pycore_gil.h](https://github.com/python/cpython/blob/main/Include/internal/pycore_gil.h)

### Implementaciones Alternativas

- [colesbury/nogil](https://github.com/colesbury/nogil) - Fork free-threaded de Sam Gross
- [larryhastings/gilectomy](https://github.com/larryhastings/gilectomy) - Intento de remover GIL
- [pypy/pypy](https://github.com/pypy/pypy) - PyPy sin GIL tradicional
- [IronLanguages/ironpython3](https://github.com/IronLanguages/ironpython3) - IronPython sin GIL

## Blogs y Artículos Técnicos

### Análisis Profundos

- [Python Core Developers Blog - PEP 703 Acceptance](https://pyfound.blogspot.com/2023/10/python-37-has-been-released.html)
- [LWN.net - Articles about Python GIL](https://lwn.net/Kernel/Index/#Python-Global_interpreter_lock)
- [Instagram Engineering - Dismissing Python Garbage Collection](https://instagram-engineering.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172)

### Comparaciones de Rendimiento

- [Python Speed - GIL Impact Benchmarks](https://speed.python.org/)
- [PyPerformance Benchmark Suite](https://github.com/python/pyperformance)

## Herramientas y Debugging

### Profiling y Análisis

- [py-spy](https://github.com/benfred/py-spy) - Sampling profiler que puede visualizar GIL contention
- [Austin](https://github.com/P403n1x87/austin) - Frame stack sampler
- [GIL Load](https://github.com/vstinner/gilectomy) - Herramienta para medir GIL load

### Testing

- [ThreadSanitizer (TSan)](https://github.com/google/sanitizers/wiki/ThreadSanitizerCppManual)
- [pytest-timeout](https://github.com/pytest-dev/pytest-timeout) - Para detectar deadlocks en tests

## Comunidad y Discusión

### Forums

- [Python Discourse - PEP 703 Discussion](https://discuss.python.org/t/pep-703-making-the-global-interpreter-lock-optional/)
- [Python Core Developers Mailing List](https://mail.python.org/archives/list/python-dev@python.org/)
- [Reddit - r/Python GIL Discussions](https://www.reddit.com/r/Python/search?q=GIL)

### Stack Overflow

- [Tagged: python-gil](https://stackoverflow.com/questions/tagged/python-gil)
- [What is the GIL?](https://stackoverflow.com/questions/1294382/what-is-a-global-interpreter-lock-gil)

## Recursos Adicionales

### Implementaciones sin GIL

- [Jython](https://www.jython.org/) - Python sobre JVM (sin GIL tradicional)
- [IronPython](https://ironpython.net/) - Python sobre .NET (sin GIL tradicional)
- [GraalPy](https://www.graalvm.org/python/) - Python sobre GraalVM

### Alternativas de Concurrencia

- [asyncio](https://docs.python.org/3/library/asyncio.html) - Asynchronous I/O
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) - Executor APIs
- [Celery](https://docs.celeryproject.org/) - Distributed task queue

## Notas de Estudio

### Para Profundizar

1. Leer PEP 703 completo (1-2 horas)
1. Ver talk de David Beazley sobre GIL (1 hora)
1. Estudiar código fuente de CPython: `Python/ceval_gil.c`
1. Experimentar con nogil fork

### Ejercicios Recomendados

1. Replicar experimentos de David Beazley con GIL visualization
1. Comparar rendimiento: CPython vs PyPy vs nogil
1. Implementar GIL-like mutex para entender el diseño

______________________________________________________________________

**Última actualización**: Enero 2026
**Mantenido por**: py-erudito

**Nota**: Esta lista se actualizará conforme se publiquen nuevos recursos sobre Python 3.13+ free-threading.
