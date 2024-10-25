from dataclasses import fields


class FromDictMixin:
    """Mixin для преобразования словаря в датакласс и игнора лишних аргументов."""

    @classmethod
    def from_dict(cls, data: dict | None = None):
        if data is None:
            data = dict()

        class_fields = {f.name for f in fields(cls)}
        return cls(
            **{field: value for field, value in data.items() if field in class_fields},
        )
