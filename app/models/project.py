from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from app.database import Base


project_technology = Table(
    "project_technology",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("technology_id", Integer, ForeignKey("technologies.id"), primary_key=True)
)


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String, nullable=False)

    url = Column(String, nullable=True)

    profile_id = Column(
        Integer,
        ForeignKey("profiles.id"),
        nullable=False
    )

    average_rating = Column(Float, default=0.0)

    upvotes = Column(Integer, default=0)

    profile = relationship(
        "Profile",
        back_populates="projects"
    )

    feedbacks = relationship(
        "Feedback",
        back_populates="project",
        cascade="all, delete-orphan"
    )

    technologies = relationship(
        "Technology",
        secondary=project_technology,
        back_populates="projects"
    )