import abc
from dataclasses import dataclass

from django.db import transaction

from .rules import check_rules


@dataclass()
class BaseUseCase(abc.ABC):
    """Описание бизнес-логики."""

    # TODO: Можно добавить инициатора (текущего пользователя) для проверки прав

    # Список Permissions (бизнес-права)
    def permissions(self) -> list:
        return []

    # Список Rules (бизнес-правила)
    def rules(self) -> list:
        """Возвращает бизнес-правила, необходимые для проверки возможности
        выполнения бизнес-сценария."""
        return []

    @abc.abstractmethod
    def action(self) -> None:
        """Выполняет непосредственные действия сценария.

        Например, создать/изменить/удалить объект.

        """

        raise NotImplementedError

    @transaction.atomic
    def execute(self):
        """Выполняет проверку прав и валидацию правил бизнес-логики.

        Если проверки прошли, то выполняет сценарий. Иными словами
        данный метод вызывает по порядку все методы описанные выше.

        """

        check_rules(self.permissions())
        check_rules(self.rules())

        return self.action()
