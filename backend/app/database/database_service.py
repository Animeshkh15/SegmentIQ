from sqlalchemy.orm import Session

from app.database.models import (
    Document,
    Page,
    AgentResult,
    VotingResult,
    SegmentModel,
    ReviewTaskModel
)


class DatabaseService:

    def __init__(self, db: Session):
        self.db = db

    # ======================================================
    # DOCUMENT
    # ======================================================

    def create_document(
        self,
        document_name: str,
        status: str = "Processing"
    ) -> Document:

        document = Document(
            document_name=document_name,
            status=status
        )

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def update_document_status(
        self,
        document: Document,
        status: str
    ):

        document.status = status
        self.db.commit()

    # ======================================================
    # PAGE
    # ======================================================

    def create_page(
        self,
        document_id: int,
        page_number: int,
        category: str,
        confidence: float,
        reasoning: str,
        review_required: bool,
        ocr_confidence: float,
        word_count: int,
        ocr_engine: str
    ) -> Page:

        page = Page(
            document_id=document_id,
            page_number=page_number,
            category=category,
            confidence=confidence,
            reasoning=reasoning,
            review_required=review_required,
            ocr_confidence=ocr_confidence,
            word_count=word_count,
            ocr_engine=ocr_engine
        )

        self.db.add(page)
        self.db.commit()
        self.db.refresh(page)

        return page

    # ======================================================
    # AGENT RESULTS
    # ======================================================

    def create_agent_result(
        self,
        page_id: int,
        agent_name: str,
        success: bool,
        category: str,
        reasoning: str,
        error: str
    ):

        agent = AgentResult(
            page_id=page_id,
            agent_name=agent_name,
            success=success,
            category=category,
            reasoning=reasoning,
            error=error
        )

        self.db.add(agent)
        self.db.commit()

    # ======================================================
    # VOTING
    # ======================================================

    def create_voting_result(
        self,
        page_id: int,
        category: str,
        confidence: float,
        reasoning: str,
        review_required: bool
    ):

        voting = VotingResult(
            page_id=page_id,
            category=category,
            confidence=confidence,
            reasoning=reasoning,
            review_required=review_required
        )

        self.db.add(voting)
        self.db.commit()

    # ======================================================
    # SEGMENTS
    # ======================================================

    def create_segment(
        self,
        document_id: int,
        segment_number: int,
        category: str,
        start_page: int,
        end_page: int
    ):

        segment = SegmentModel(
            document_id=document_id,
            segment_number=segment_number,
            category=category,
            start_page=start_page,
            end_page=end_page
        )

        self.db.add(segment)
        self.db.commit()

    # ======================================================
    # REVIEW QUEUE
    # ======================================================

    def create_review_task(
        self,
        page_id: int,
        reason: str,
        confidence: float,
        winning_category: str,
        reasoning: str
    ):

        review = ReviewTaskModel(
            page_id=page_id,
            reason=reason,
            confidence=confidence,
            winning_category=winning_category,
            reasoning=reasoning
        )

        self.db.add(review)
        self.db.commit()