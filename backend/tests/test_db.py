import sqlalchemy as sa

from backend.database import models


def test_create_user(session):
    new_user = models.User(
        name='Test User',
        course='Test',
        period='1',
        email='test@test.com',
        password='test',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(
        sa.select(models.User).where(models.User.email == 'test@test.com')
    )

    assert user
    assert user.email == 'test@test.com'
