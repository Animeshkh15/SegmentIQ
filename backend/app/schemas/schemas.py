from pydantic import BaseModel
from typing import List, Optional

class OCRPage(BaseModel):
    page_number: int
    text: str


class AgentPrediction(BaseModel):
    page_number: int
    category: str
    reasoning: str

class AgentResult(BaseModel):
    success: bool
    category: Optional[str] = None
    reasoning: Optional[str] = None
    error: Optional[str] = None


class VotingResult(BaseModel):
    page_number: int
    category: str
    confidence: float
    votes: int
    total_agents: int
    reasoning: str


class ReviewTask(BaseModel):
    page_number: int
    predicted_category: str
    confidence: float


class Segment(BaseModel):
    segment_id: int
    page_start: int
    page_end: int
    category: str
    confidence: float


class ProcessingResult(BaseModel):
    segments: List[Segment]


class PageClassification(BaseModel):
    page_number: int
    category: str
    confidence: float
    reasoning: str


class ReviewRequired(BaseModel):
    page_number: int
    reason: str


class ClassificationRequest(BaseModel):
    pages: dict[int, str]