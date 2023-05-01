from sqlalchemy.orm import Mapped

from tgbot.db import Base


class Resource(Base):
    """Resource model."""

    title: Mapped[str]
    url: Mapped[str]
    xpath: Mapped[str]
