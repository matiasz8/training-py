"""
Ejemplo básico: Patrón Singleton en Python
===========================================

El patrón Singleton asegura que una clase tenga solo una instancia
y proporciona un punto de acceso global a ella.

Este ejemplo muestra:
1. Implementación básica con __new__
2. Implementación thread-safe
3. Singleton como decorator
4. Singleton con metaclase
5. Casos de uso prácticos
"""

import threading
from typing import Any, Dict, Optional
from functools import wraps


# =============================================================================
# IMPLEMENTACIÓN 1: Singleton Básico con __new__
# =============================================================================

class DatabaseConnection:
    """
    Singleton básico usando __new__.
    
    Solo puede existir una instancia de esta clase.
    """
    _instance: Optional['DatabaseConnection'] = None
    
    def __new__(cls):
        if cls._instance is None:
            print("🔨 Creando nueva instancia de DatabaseConnection")
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        # Solo inicializar una vez
        if not self._initialized:
            print("⚙️  Inicializando DatabaseConnection")
            self.connection_string = "postgresql://localhost:5432/mydb"
            self.pool_size = 10
            self._initialized = True
    
    def execute_query(self, query: str) -> str:
        """Ejecuta una query en la base de datos."""
        return f"Executing: {query}"


# =============================================================================
# IMPLEMENTACIÓN 2: Singleton Thread-Safe
# =============================================================================

class Logger:
    """
    Singleton thread-safe para logging.
    
    Usa un lock para garantizar que solo un thread cree la instancia.
    """
    _instance: Optional['Logger'] = None
    _lock: threading.Lock = threading.Lock()
    
    def __new__(cls):
        # Double-checked locking
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print("🔒 Creando Logger thread-safe")
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.logs: list[str] = []
            self.log_level = "INFO"
            self._initialized = True
    
    def log(self, message: str, level: str = "INFO") -> None:
        """Registra un mensaje."""
        log_entry = f"[{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self) -> list[str]:
        """Retorna todos los logs."""
        return self.logs.copy()


# =============================================================================
# IMPLEMENTACIÓN 3: Singleton como Decorator
# =============================================================================

def singleton(cls):
    """
    Decorator que convierte cualquier clase en Singleton.
    
    Uso:
        @singleton
        class MyClass:
            pass
    """
    instances = {}
    lock = threading.Lock()
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton
class ConfigManager:
    """Gestor de configuración usando decorator singleton."""
    
    def __init__(self):
        print("📋 Inicializando ConfigManager")
        self.config: Dict[str, Any] = {
            "app_name": "MyApp",
            "version": "1.0.0",
            "debug": False
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Obtiene un valor de configuración."""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Establece un valor de configuración."""
        self.config[key] = value


# =============================================================================
# IMPLEMENTACIÓN 4: Singleton con Metaclase
# =============================================================================

class SingletonMeta(type):
    """
    Metaclase que implementa Singleton.
    
    Las clases que usan esta metaclase son automáticamente Singleton.
    """
    _instances: Dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class CacheManager(metaclass=SingletonMeta):
    """Gestor de caché usando metaclase singleton."""
    
    def __init__(self):
        print("💾 Inicializando CacheManager")
        self.cache: Dict[str, Any] = {}
    
    def get(self, key: str) -> Optional[Any]:
        """Obtiene un valor del caché."""
        return self.cache.get(key)
    
    def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        """Establece un valor en el caché."""
        self.cache[key] = value
        print(f"✓ Cached: {key} = {value}")
    
    def clear(self) -> None:
        """Limpia el caché."""
        self.cache.clear()
        print("🗑️  Cache cleared")


# =============================================================================
# CASO DE USO REAL: Application State
# =============================================================================

class ApplicationState(metaclass=SingletonMeta):
    """
    Estado global de la aplicación (Singleton).
    
    Útil para mantener estado compartido en toda la aplicación.
    """
    
    def __init__(self):
        self.is_authenticated = False
        self.current_user: Optional[str] = None
        self.session_data: Dict[str, Any] = {}
    
    def login(self, username: str) -> None:
        """Iniciar sesión."""
        self.is_authenticated = True
        self.current_user = username
        print(f"✅ Usuario {username} autenticado")
    
    def logout(self) -> None:
        """Cerrar sesión."""
        self.is_authenticated = False
        self.current_user = None
        self.session_data.clear()
        print("👋 Sesión cerrada")
    
    def get_current_user(self) -> Optional[str]:
        """Obtiene el usuario actual."""
        return self.current_user


# =============================================================================
# FUNCIONES DE DEMOSTRACIÓN
# =============================================================================

def demonstrate_basic_singleton():
    """Demuestra singleton básico."""
    print("\n🔹 EJEMPLO 1: Singleton Básico")
    print("=" * 60)
    
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"\ndb1 is db2: {db1 is db2}")
    print(f"id(db1): {id(db1)}")
    print(f"id(db2): {id(db2)}")
    print("✓ Ambas variables apuntan a la misma instancia")


def demonstrate_thread_safe_singleton():
    """Demuestra singleton thread-safe."""
    print("\n🔹 EJEMPLO 2: Singleton Thread-Safe")
    print("=" * 60)
    
    logger1 = Logger()
    logger2 = Logger()
    
    logger1.log("Mensaje desde logger1", "INFO")
    logger2.log("Mensaje desde logger2", "WARNING")
    
    print(f"\nlogger1 is logger2: {logger1 is logger2}")
    print(f"Logs en logger1: {len(logger1.get_logs())}")
    print(f"Logs en logger2: {len(logger2.get_logs())}")


def demonstrate_decorator_singleton():
    """Demuestra singleton con decorator."""
    print("\n🔹 EJEMPLO 3: Singleton con Decorator")
    print("=" * 60)
    
    config1 = ConfigManager()
    config2 = ConfigManager()
    
    config1.set("theme", "dark")
    print(f"\nconfig2.get('theme'): {config2.get('theme')}")
    print(f"config1 is config2: {config1 is config2}")


def demonstrate_metaclass_singleton():
    """Demuestra singleton con metaclase."""
    print("\n🔹 EJEMPLO 4: Singleton con Metaclase")
    print("=" * 60)
    
    cache1 = CacheManager()
    cache2 = CacheManager()
    
    cache1.set("user:123", {"name": "Alice", "age": 30})
    cached_value = cache2.get("user:123")
    
    print(f"\nValor en cache2: {cached_value}")
    print(f"cache1 is cache2: {cache1 is cache2}")


def demonstrate_real_world_usage():
    """Demuestra caso de uso real."""
    print("\n🔹 EJEMPLO 5: Caso de Uso Real - Application State")
    print("=" * 60)
    
    # En diferentes partes de la aplicación
    state1 = ApplicationState()
    state1.login("alice@example.com")
    
    # En otra parte del código
    state2 = ApplicationState()
    current_user = state2.get_current_user()
    
    print(f"\n✓ Usuario actual: {current_user}")
    print(f"✓ Autenticado: {state2.is_authenticated}")
    print(f"✓ state1 is state2: {state1 is state2}")


def main():
    """Función principal de demostración."""
    print("=" * 60)
    print("PATRÓN SINGLETON - EJEMPLOS COMPLETOS")
    print("=" * 60)
    
    demonstrate_basic_singleton()
    demonstrate_thread_safe_singleton()
    demonstrate_decorator_singleton()
    demonstrate_metaclass_singleton()
    demonstrate_real_world_usage()
    
    print("\n" + "=" * 60)
    print("🎓 CONCEPTOS CLAVE:")
    print("=" * 60)
    print("1. Singleton asegura una sola instancia de una clase")
    print("2. Útil para recursos compartidos (DB, config, cache)")
    print("3. Implementaciones: __new__, decorator, metaclase")
    print("4. Thread-safety es importante en aplicaciones concurrentes")
    print("5. ⚠️  Usar con moderación - puede dificultar testing")
    print("=" * 60)


if __name__ == "__main__":
    main()
