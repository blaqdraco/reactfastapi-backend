from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey, JSON, Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.db.database import Base


class Story(Base):
    __tablename__ = 'stories'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    nodes = relationship("StoryNode", back_populates="story")


class StoryNode(Base):
    __tablename__ = 'story_nodes'

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey('stories.id'), index=True)
    content = Column(String, index=True)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON)  # removed index=True, JSON can't be indexed directly

    story = relationship("Story", back_populates="nodes")
