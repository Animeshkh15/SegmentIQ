from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text
)

from sqlalchemy.orm import relationship

from app.database.db import Base


# ==========================================================
# Documents
# ==========================================================

class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    document_name = Column(String, nullable=False)

    status = Column(
        String,
        nullable=False,
        default="Processing"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    pages = relationship(
        "Page",
        back_populates="document",
        cascade="all, delete-orphan"
    )

    segments = relationship(
        "SegmentModel",
        back_populates="document",
        cascade="all, delete-orphan"
    )


# ==========================================================
# Pages
# ==========================================================

class Page(Base):

    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)

    page_number = Column(Integer, nullable=False)

    category = Column(String)

    confidence = Column(Float)

    reasoning = Column(Text)

    review_required = Column(
        Boolean,
        default=False
    )

    # OCR metadata
    ocr_confidence = Column(Float)

    word_count = Column(Integer)

    ocr_engine = Column(String)

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    document = relationship(
        "Document",
        back_populates="pages"
    )

    agent_results = relationship(
        "AgentResult",
        back_populates="page",
        cascade="all, delete-orphan"
    )

    voting_result = relationship(
        "VotingResult",
        back_populates="page",
        uselist=False,
        cascade="all, delete-orphan"
    )

    review_tasks = relationship(
        "ReviewTaskModel",
        back_populates="page",
        cascade="all, delete-orphan"
    )


# ==========================================================
# Agent Results
# ==========================================================

class AgentResult(Base):

    __tablename__ = "agent_results"

    id = Column(Integer, primary_key=True)

    agent_name = Column(String)

    category = Column(String)

    reasoning = Column(Text)

    success = Column(Boolean)

    error = Column(Text)

    page_id = Column(
        Integer,
        ForeignKey("pages.id")
    )

    page = relationship(
        "Page",
        back_populates="agent_results"
    )


# ==========================================================
# Voting Results
# ==========================================================

class VotingResult(Base):

    __tablename__ = "voting_results"

    id = Column(Integer, primary_key=True)

    category = Column(String)

    confidence = Column(Float)

    reasoning = Column(Text)

    review_required = Column(Boolean)

    page_id = Column(
        Integer,
        ForeignKey("pages.id"),
        unique=True
    )

    page = relationship(
        "Page",
        back_populates="voting_result"
    )


# ==========================================================
# Segments
# ==========================================================

class SegmentModel(Base):

    __tablename__ = "segments"

    id = Column(Integer, primary_key=True)

    segment_number = Column(Integer)

    category = Column(String)

    start_page = Column(Integer)

    end_page = Column(Integer)

    document_id = Column(
        Integer,
        ForeignKey("documents.id")
    )

    document = relationship(
        "Document",
        back_populates="segments"
    )


# ==========================================================
# Review Queue
# ==========================================================

class ReviewTaskModel(Base):

    __tablename__ = "review_tasks"

    id = Column(Integer, primary_key=True)

    reason = Column(Text)

    confidence = Column(Float)

    winning_category = Column(String)

    reasoning = Column(Text)

    resolved = Column(
        Boolean,
        default=False
    )

    page_id = Column(
        Integer,
        ForeignKey("pages.id")
    )

    page = relationship(
        "Page",
        back_populates="review_tasks"
    )