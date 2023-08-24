from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from common.domain import Base


class MilestoneORM(Base):
    __tablename__ = 'milestones'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    date: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    