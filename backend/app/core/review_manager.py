from app.schemas.schemas import ReviewRequired


class ReviewManager:

    def __init__(self):

        self.review_queue = []

    def submit_review(
        self,
        review: ReviewRequired
    ):

        self.review_queue.append(review)

    def get_reviews(self):

        return self.review_queue