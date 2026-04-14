"""Ejemplo funcional de variables y tipos de datos."""

from typing import TypedDict


class Profile(TypedDict):
    """Estructura tipada para un perfil simple."""

    name: str
    age: int
    active: bool
    skills: list[str]
    score: float


def build_profile(name: str, age: int, active: bool) -> Profile:
    """Construye un perfil simple usando tipos basicos de Python."""
    return {
        "name": name,
        "age": age,
        "active": active,
        "skills": ["python", "testing", "automation"],
        "score": 9.5,
    }


def describe_profile(profile: Profile) -> str:
    """Resume el contenido del perfil y los tipos involucrados."""
    skills = ", ".join(profile["skills"])
    return (
        f"{profile['name']} ({profile['age']} anios) | "
        f"activo={profile['active']} | score={profile['score']} | skills={skills}"
    )


def main() -> None:
    profile = build_profile("Ada", 32, True)
    print(describe_profile(profile))
    print({key: type(value).__name__ for key, value in profile.items()})


if __name__ == "__main__":
    main()
