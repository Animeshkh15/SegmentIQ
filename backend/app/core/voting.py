from collections import Counter
from app.schemas.schemas import ReviewRequired

from app.schemas.schemas import (
    AgentResult,
    PageClassification
)


class VotingEngine:

    def __init__(
        self,
        minimum_successful_agents: int = 3
    ):
        self.minimum_successful_agents = minimum_successful_agents

    def vote(
        self,
        page_number: int,
        results: list[AgentResult]
    ):

        successful_results = [
            result
            for result in results
            if result.success
        ]

        if len(successful_results) < self.minimum_successful_agents:

            return ReviewRequired(
                page_number=page_number,
                reason="Insufficient successful agent responses"
            )

        categories = [
            result.category
            for result in successful_results
        ]

        counter = Counter(categories)

        winning_category, winning_votes = (
            counter.most_common(1)[0]
        )

        confidence = (
            winning_votes /
            len(successful_results)
        )

        if confidence < 0.60:

            return ReviewRequired(
                page_number=page_number,
                reason=f"Low confidence: {confidence:.2f}"
            )

        majority_reasoning = next(
            result.reasoning
            for result in successful_results
            if result.category == winning_category
        )

        return PageClassification(
            page_number=page_number,
            category=winning_category,
            confidence=confidence,
            reasoning=majority_reasoning
        )