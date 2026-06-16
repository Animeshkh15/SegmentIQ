from app.pipeline.document_pipeline import DocumentPipeline
from app.schemas.schemas import ClassificationRequest

pipeline = DocumentPipeline()


@router.post("/classify")
def classify_document(
    request: ClassificationRequest
):

    results = pipeline.process_document(
        pages=request.pages
    )

    return {
        "results": results
    }