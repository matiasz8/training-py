"""Ejemplo funcional de diccionarios y sets."""


def count_statuses(statuses: list[str]) -> dict[str, int]:
    """Cuenta ocurrencias de estados usando un diccionario."""
    result: dict[str, int] = {}
    for status in statuses:
        result[status] = result.get(status, 0) + 1
    return result


def unique_languages(teams: dict[str, set[str]]) -> set[str]:
    """Une todos los lenguajes declarados por los equipos."""
    languages: set[str] = set()
    for values in teams.values():
        languages.update(values)
    return languages


def main() -> None:
    print(count_statuses(["todo", "done", "todo", "review"]))
    print(unique_languages({"backend": {"python", "sql"}, "data": {"python", "rust"}}))


if __name__ == "__main__":
    main()
