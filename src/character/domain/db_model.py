from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from common.domain.db_model import Base


class CharacterORM(Base):
    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    year_of_birth: Mapped[str] = mapped_column(String(255), nullable=True)
    month_of_birth: Mapped[str] = mapped_column(String(255), nullable=True)
    day_of_birth: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    gender: Mapped[str] = mapped_column(String(255), nullable=True)
    life_status: Mapped[int] = mapped_column(nullable=False)
