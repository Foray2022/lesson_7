# Задание
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

# Решение
from abc import ABC, abstractmethod
# анотация типа Any совместимого со всеми другими типами
from typing import Any


# определим общий интерфейс для набора подклассов.
class AbstractClothes(ABC):

    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, size: Any):
        self.name = name
        self._size = size
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:  # Расход ткани

        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def size(self) -> Any:  # указать размер
        return self._size

    @size.setter
    def size(self, size: Any):  # Установить новый размер пальто

        self._size = size
        self._tissue_required = None

    @property
    def total_tissue_required(self):  # расход ткани на всю одежду
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):

    def _calc_tissue_required(self):  # расчет расхода ткани для пальто
        self._tissue_required = round(self.size / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:  # размер пальто
        return self.size

    @V.setter
    def V(self, size: Any):  # Установить новый размер пальто

        self.size = size

    def __str__(self):  # вывод расчетных величин
        return f"For sewing coats {self.size} size, required {self.tissue_required} square meters of fabric"


# для Костюма
class Suit(Clothes):

    def _calc_tissue_required(self):  # расчет расхода ткани для костюма
        self._tissue_required = round(2 * self.size * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        return self.size

    @H.setter  # новый размер костюма
    def H(self, height: Any):
        self.size = height

    def __str__(self):
        return f"For sewing a suit for height {self.size} cm. required {self.tissue_required} square meters of fabric"

if __name__ == '__main__':
    coat = Coat('Пальто', 3)
    print(f'1:{coat}')
    coat.V = 10
    print(f'2:{coat}')

    suit = Suit('Костюм', 168)
    print(f'1:{suit}')
    suit.H = 180
    print(f'2:{suit}')

    print(f'1:Total fabric consumption:{coat.total_tissue_required}')
    print(f'2:Total fabric consumption:{suit.total_tissue_required}')
