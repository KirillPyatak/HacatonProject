from uuid import UUID
from sqlalchemy import insert, delete, select
from internal.db.models import Application
from sqlalchemy.ext.asyncio import AsyncSession


async def _create_application(application, session: AsyncSession):
    query = Application(
        first_name=application.first_name,
        second_name=application.second_name,
        surname=application.surname,
        login_telegram=application.login_telegram,
        cv_file=application.cv_file,
    )
    session.add(query)
    await session.commit()
    await session.refresh(query)
    return query


async def _delete_application(id: UUID, session: AsyncSession):
    query = delete(Application).where(Application.id == id)
    post_to_delete = await session.execute(query)
    if post_to_delete:
        await session.commit()
        return {"message": "Post deleted"}


async def _get_all_application(session: AsyncSession):
    stmt = select(Application)
    result = await session.execute(stmt)
    return result.scalars().all()


async def _get_one_application(id: UUID, session: AsyncSession):
    stmt = select(Application).where(Application.id == id)
    result = await session.execute(stmt)
    return result.scalars().one()
