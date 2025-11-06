"""Классы для оценки хода выполнения задания.

from mgimo.utils.logging import Mark, Transcript
Mark("это было простое задание").score(19, out_of=20).save("1.json")
Mark("это было задание посложнее").score(8, out_of=10).save("2.json")
t = Transcript()
t.register("1.json")
t.register("2.json")
p = t.summary.percent
"""

import datetime
import json
from dataclasses import dataclass, field
from pathlib import Path
from uuid import uuid1


def get_id(length=6):
    return str(uuid1()).replace("-", "")[0:length]


def now() -> str:
    return datetime.datetime.now().isoformat()


@dataclass
class Mark:
    """Оценка за отдельное задание.

    title: str - название задания или упражнения.
    points: int - количество набранных баллов.
    out_of: int - максимальное количество баллов за задание.
    comment: str - комментарий (опционально).
    payload: str - результаты работы (опционально).
    iso_timestamp: str - метка времени в формате ISO (создается автоматически).
    """

    title: str
    points: int = 0
    out_of: int = 0
    note: str = ""
    payload: list = field(default_factory=list)
    iso_timestamp: str = field(default_factory=now)

    def score(self, points: int, out_of: int):
        self.points = points
        self.out_of = out_of
        self.iso_timestamp = now()
        return self

    def attach(self, x):
        content = json.dumps(x, ensure_ascii=False)
        self.payload.append(content)
        return self

    def comment(self, text):
        self.note = text
        return self

    @property
    def percent(self):
        return round(self.points / self.out_of * 100)

    def save(self, path):
        content = json.dumps(self.__dict__, ensure_ascii=False, indent=2)
        Path(path).write_text(content, encoding="utf-8")

    @classmethod
    def load(cls, path):
        return Mark(**json.loads(Path(path).read_text(encoding="utf-8")))


@dataclass
class Transcript:
    """Набор выполненных заданий."""

    marks: list[Mark] = field(default_factory=list)

    def register(self, path):
        """Прочитать файл с оценкой за задание."""
        mark = Mark.load(path)
        self.marks.append(mark)

    @property
    def summary(self) -> Mark:
        points = 0
        out_of = 0
        for m in self.marks:
            points += m.points
            out_of += m.out_of
        return Mark("суммарная оценка").score(points, out_of)

    @property
    def notes(self):
        return [m.note for m in self.marks]
