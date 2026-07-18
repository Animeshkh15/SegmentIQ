from pdf2image import convert_from_path
from paddleocr import PaddleOCR
import logging

logger = logging.getLogger(__name__)


class OCRService:
    _ocr = None

    def __init__(self):
        if OCRService._ocr is None:
            logger.info("Loading PaddleOCR model...")
            OCRService._ocr = PaddleOCR(
                lang="en"
            )
            logger.info("PaddleOCR initialized successfully.")

    def extract_text(self, pdf_path: str):

        images = convert_from_path(
            pdf_path,
            poppler_path=r"C:\poppler\Library\bin"
        )

        pages = {}

        for page_number, image in enumerate(images, start=1):

            try:
                result = OCRService._ocr.predict(image)

                extracted_lines = []
                confidences = []

                for block in result:

                    if "rec_texts" in block:
                        extracted_lines.extend(block["rec_texts"])

                    if "rec_scores" in block:
                        confidences.extend(block["rec_scores"])

                text = "\n".join(extracted_lines).strip()

                avg_confidence = (
                    sum(confidences) / len(confidences)
                    if confidences else 0.0
                )

                pages[page_number] = {
                    "text": text,
                    "confidence": round(avg_confidence, 4),
                    "word_count": len(text.split()),
                    "ocr_engine": "PaddleOCR"
                }

            except Exception as e:
                logger.exception(
                    f"OCR failed for page {page_number}: {e}"
                )

                pages[page_number] = {
                    "text": "",
                    "confidence": 0.0,
                    "word_count": 0,
                    "ocr_engine": "PaddleOCR"
                }

        return pages

    @staticmethod
    def assess_quality(text: str):

        cleaned = text.strip()

        if not cleaned:
            return True, "OCR extracted empty text"

        if len(cleaned) < 15:
            return (
                True,
                f"OCR text length ({len(cleaned)}) is too short"
            )

        alnum = sum(
            1
            for c in cleaned
            if c.isalnum() or c.isspace()
        )

        ratio = alnum / len(cleaned)

        if ratio < 0.5:
            return (
                True,
                f"OCR text contains too much noise ({ratio:.2%})"
            )

        return False, ""