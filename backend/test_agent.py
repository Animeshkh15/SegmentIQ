from app.core.adk_runner import ADKRunner

runner = ADKRunner()

result = runner.classify_page(
    page_number=1,
    text="""
    Invoice Number INV-123

    Vendor: ABC Ltd

    Customer: XYZ Ltd

    Total Amount: $5000
    """
)

print(result)