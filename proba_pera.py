@app.get("/users")
async def get_users(
    user_id: Annotated[int | None, Query()] = None,
) -> list[User]:
    async with asyncsessionmaker.begin() as session:
        stmt = select(User).where(User.isactive.is(True))
        if user_id is not None:
            stmt = stmt.where(User.id == user_id)
        return (await session.scalars(stmt)).all()