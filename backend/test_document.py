from app.pipeline.document_pipeline import DocumentPipeline

pipeline = DocumentPipeline()

pages = {
    1: """
    Invoice Number INV-123
    Vendor ABC Ltd
    Total Amount $5000
    """,

    2: """
    Invoice Number INV-124
    Vendor XYZ Ltd
    Total Amount $2500
    """,

    3: """
    Patient Name John Doe
    Diagnosis: Diabetes
    """
}

results = pipeline.process_document(
    pages=pages
)

for result in results:
    print(result)