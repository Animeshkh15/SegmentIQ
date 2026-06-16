from app.core.agent_pool import AgentPool
from app.core.voting import VotingEngine
from app.core.review_manager import ReviewManager
from app.schemas.schemas import ReviewRequired


class DocumentPipeline:

    def __init__(self):

        self.agent_pool = AgentPool()

        self.voting_engine = VotingEngine()

        self.review_manager = ReviewManager()

    def process_document(
        self,
        pages: dict[int, str]
    ):

        print("Pipeline started")

        page_results = []

        for page_number, text in pages.items():

            print(f"Processing page {page_number}")

            agent_results = self.agent_pool.classify_page(
                page_number=page_number,
                text=text
            )

            print(
                f"Agent results received for page {page_number}"
            )

            page_result = self.voting_engine.vote(
                page_number=page_number,
                results=agent_results
            )

            print(
                f"Voting completed for page {page_number}"
            )

            if isinstance(
                page_result,
                ReviewRequired
            ):

                self.review_manager.submit_review(
                    page_result
                )

            page_results.append(page_result)

        print("Pipeline completed")

        return page_results