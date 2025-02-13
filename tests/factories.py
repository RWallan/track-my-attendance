# type: ignore
from datetime import UTC, datetime

import factory
import factory.fuzzy

from track_my_attendance import models


class AbsenceFactory(factory.Factory):
    class Meta:
        model = models.Absence

    date = factory.fuzzy.FuzzyDateTime(
        datetime(2024, 1, 1, tzinfo=UTC), datetime(2025, 1, 1, tzinfo=UTC)
    )
    present = factory.Faker('pybool')

    course_id = 1
