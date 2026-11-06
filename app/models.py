from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class UserDB(Base):
    _tablename_ = "id"

id: Mapped[int] = mapped_column(primary_key=True, index=True)
equipment_id: Mapped[int] = mapped_column(Integer, nullable=False)
student_id: Mapped[str] = mapped_column(
    String(8), unique=True, nullable=False
)
description: Mapped[str] = mapped_column(String(100), unique=True, nullable=False
)
priority: Mapped[int] = mapped_column(Integer, nullable=False)
status: Mapped[str] = mapped_column(
    String(10), unique=True, nullable=False
)