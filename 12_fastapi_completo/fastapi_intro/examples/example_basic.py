"""
Ejemplo básico: Introducción a FastAPI
=======================================

FastAPI es un framework web moderno y de alto rendimiento para construir APIs
con Python 3.7+ basado en type hints estándar.

Este ejemplo demuestra:
1. Crear una aplicación FastAPI básica
2. Definir rutas con diferentes métodos HTTP
3. Path parameters y query parameters
4. Request body con modelos Pydantic
5. Respuestas con status codes
6. Documentación automática

Instalación requerida:
    pip install fastapi uvicorn[standard]

Ejecutar:
    uvicorn example_basic:app --reload
    
    Luego visitar:
    - http://localhost:8000/docs (Swagger UI)
    - http://localhost:8000/redoc (ReDoc)
"""

from fastapi import FastAPI, HTTPException, Query, Path, Body, status
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum


# =============================================================================
# CREAR APLICACIÓN FASTAPI
# =============================================================================

app = FastAPI(
    title="Mi Primera API con FastAPI",
    description="API de ejemplo para aprender FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


# =============================================================================
# MODELOS PYDANTIC (Request/Response)
# =============================================================================

class ItemCategory(str, Enum):
    """Categorías de items (Enum)."""
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    FOOD = "food"
    BOOKS = "books"


class Item(BaseModel):
    """Modelo para un item."""
    name: str = Field(..., min_length=1, max_length=100, description="Nombre del item")
    description: Optional[str] = Field(None, max_length=500, description="Descripción del item")
    price: float = Field(..., gt=0, description="Precio del item (debe ser > 0)")
    category: ItemCategory = Field(..., description="Categoría del item")
    in_stock: bool = Field(True, description="Si el item está en stock")
    tags: List[str] = Field(default_factory=list, description="Tags del item")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Laptop HP",
                "description": "Laptop de 15 pulgadas con 16GB RAM",
                "price": 799.99,
                "category": "electronics",
                "in_stock": True,
                "tags": ["computadora", "tecnología"]
            }
        }


class User(BaseModel):
    """Modelo para un usuario."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None
    disabled: bool = False


class ItemResponse(BaseModel):
    """Respuesta al crear/obtener un item."""
    id: int
    item: Item
    created_at: datetime
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "name": "Laptop HP",
                    "description": "Laptop de 15 pulgadas",
                    "price": 799.99,
                    "category": "electronics",
                    "in_stock": True,
                    "tags": ["computadora"]
                },
                "created_at": "2026-01-31T10:30:00"
            }
        }


# =============================================================================
# BASE DE DATOS SIMULADA (en memoria)
# =============================================================================

# Simular una base de datos en memoria
items_db: dict[int, ItemResponse] = {}
users_db: dict[str, User] = {}
next_item_id = 1


# =============================================================================
# RUTAS - GET REQUESTS
# =============================================================================

@app.get("/")
async def root():
    """
    Ruta raíz - Health check.
    
    Returns:
        Mensaje de bienvenida
    """
    return {
        "message": "¡Bienvenido a FastAPI!",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health_check():
    """Verificación de salud del servicio."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/items", response_model=List[ItemResponse])
async def get_items(
    skip: int = Query(0, ge=0, description="Número de items a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Máximo número de items a retornar"),
    category: Optional[ItemCategory] = Query(None, description="Filtrar por categoría"),
    in_stock: Optional[bool] = Query(None, description="Filtrar por disponibilidad")
):
    """
    Obtener lista de items con paginación y filtros.
    
    Query parameters:
        - skip: Offset para paginación
        - limit: Límite de items a retornar
        - category: Filtrar por categoría
        - in_stock: Filtrar por disponibilidad
    
    Returns:
        Lista de items
    """
    items = list(items_db.values())
    
    # Aplicar filtros
    if category is not None:
        items = [item for item in items if item.item.category == category]
    
    if in_stock is not None:
        items = [item for item in items if item.item.in_stock == in_stock]
    
    # Aplicar paginación
    return items[skip : skip + limit]


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(
    item_id: int = Path(..., ge=1, description="ID del item a obtener")
):
    """
    Obtener un item por su ID.
    
    Path parameters:
        - item_id: ID del item
    
    Returns:
        Item solicitado
    
    Raises:
        HTTPException 404: Si el item no existe
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item con ID {item_id} no encontrado"
        )
    
    return items_db[item_id]


# =============================================================================
# RUTAS - POST REQUESTS
# =============================================================================

@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    """
    Crear un nuevo item.
    
    Request body:
        - item: Datos del item a crear
    
    Returns:
        Item creado con su ID
    """
    global next_item_id
    
    item_response = ItemResponse(
        id=next_item_id,
        item=item,
        created_at=datetime.now()
    )
    
    items_db[next_item_id] = item_response
    next_item_id += 1
    
    return item_response


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    """
    Crear un nuevo usuario.
    
    Returns:
        Usuario creado
    
    Raises:
        HTTPException 400: Si el usuario ya existe
    """
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Usuario {user.username} ya existe"
        )
    
    users_db[user.username] = user
    return user


# =============================================================================
# RUTAS - PUT/PATCH REQUESTS
# =============================================================================

@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: int = Path(..., ge=1),
    item: Item = Body(...)
):
    """
    Actualizar un item existente (reemplazo completo).
    
    Returns:
        Item actualizado
    
    Raises:
        HTTPException 404: Si el item no existe
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item con ID {item_id} no encontrado"
        )
    
    items_db[item_id].item = item
    return items_db[item_id]


@app.patch("/items/{item_id}/stock", response_model=ItemResponse)
async def update_item_stock(
    item_id: int = Path(..., ge=1),
    in_stock: bool = Body(..., embed=True)
):
    """
    Actualizar solo el stock de un item (actualización parcial).
    
    Returns:
        Item actualizado
    
    Raises:
        HTTPException 404: Si el item no existe
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item con ID {item_id} no encontrado"
        )
    
    items_db[item_id].item.in_stock = in_stock
    return items_db[item_id]


# =============================================================================
# RUTAS - DELETE REQUESTS
# =============================================================================

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int = Path(..., ge=1)):
    """
    Eliminar un item.
    
    Returns:
        Status 204 No Content
    
    Raises:
        HTTPException 404: Si el item no existe
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item con ID {item_id} no encontrado"
        )
    
    del items_db[item_id]
    return None


# =============================================================================
# INFORMACIÓN ADICIONAL
# =============================================================================

@app.get("/stats")
async def get_stats():
    """Obtener estadísticas de la API."""
    return {
        "total_items": len(items_db),
        "total_users": len(users_db),
        "items_by_category": {
            category: len([
                item for item in items_db.values() 
                if item.item.category == category
            ])
            for category in ItemCategory
        }
    }


# =============================================================================
# SCRIPT DE PRUEBA (ejecutar con: python example_basic.py)
# =============================================================================

def print_instructions():
    """Imprime instrucciones para usar la API."""
    print("=" * 70)
    print("FASTAPI - EJEMPLO BÁSICO")
    print("=" * 70)
    print("\n📦 Para ejecutar el servidor:\n")
    print("    uvicorn example_basic:app --reload")
    print("\n🌐 URLs importantes:")
    print("    • API: http://localhost:8000")
    print("    • Docs (Swagger): http://localhost:8000/docs")
    print("    • ReDoc: http://localhost:8000/redoc")
    print("\n📝 Endpoints disponibles:")
    print("    • GET    /              - Health check")
    print("    • GET    /items         - Listar items")
    print("    • GET    /items/{id}    - Obtener item")
    print("    • POST   /items         - Crear item")
    print("    • PUT    /items/{id}    - Actualizar item")
    print("    • PATCH  /items/{id}/stock - Actualizar stock")
    print("    • DELETE /items/{id}    - Eliminar item")
    print("    • POST   /users         - Crear usuario")
    print("    • GET    /stats         - Estadísticas")
    print("\n🧪 Ejemplo de request con curl:")
    print("""
    curl -X POST "http://localhost:8000/items" \\
         -H "Content-Type: application/json" \\
         -d '{
             "name": "Laptop HP",
             "description": "Laptop de 15 pulgadas",
             "price": 799.99,
             "category": "electronics",
             "in_stock": true,
             "tags": ["computadora", "tecnología"]
         }'
    """)
    print("=" * 70)


if __name__ == "__main__":
    print_instructions()
