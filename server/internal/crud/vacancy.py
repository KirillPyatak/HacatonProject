from uuid import UUID
from sqlalchemy import insert, delete, select
from internal.db.models import vacancy
from sqlalchemy.ext.asyncio import AsyncSession


async def _create_vacancy(vacancy, session: AsyncSession):
    query = vacancy(
        first_name=vacancy.first_name,
        second_name=vacancy.second_name,
        surname=vacancy.surname,
        login_telegram=vacancy.login_telegram,
        cv_file=vacancy.cv_file,
    )
    session.add(query)
    await session.commit()
    await session.refresh(query)
    return query


async def _delete_vacancy(id: UUID, session: AsyncSession):
    query = delete(vacancy).where(vacancy.id == id)
    post_to_delete = await session.execute(query)
    if post_to_delete:
        await session.commit()
        return {"message": "Post deleted"}


async def _get_all_vacancy(session: AsyncSession):
    stmt = select(vacancy)
    result = await session.execute(stmt)
    return result.scalars().all()


async def _get_one_vacancy(id: UUID, session: AsyncSession):
    stmt = select(vacancy).where(vacancy.id == id)
    result = await session.execute(stmt)
    return result.scalars().one()

