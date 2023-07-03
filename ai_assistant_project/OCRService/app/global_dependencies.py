from fastapi import Depends
from OCRService.app.services.ocr_service import OCRService
from OCRService.app.services.errorHandler.IErrorHandler import RetryErrorHandler
from OCRService.app.services.exporters.document_exporter import DocumentExporter
from OCRService.app.services.processors.base64_processor import Base64Processor
from OCRService.app.services.processors.pdf_processor import PDFProcessor
from OCRService.app.services.processors.word_processor import WordProcessor
from OCRService.app.services.processors.image_processor import ImageProcessor
from OCRService.app.services.processors.url_processor import UrlProcessor
from OCRService.app.services.processors.powerpoint_document_processor import PowerPointDocumentProcessor
from OCRService.app.services.processors.rtf_document_processor import RTFDocumentProcessor
from OCRService.app.services.processors.text_document_processor import TextDocumentProcessor
from OCRService.app.services.processors.excel_document_processor import ExcelDocumentProcessor
from OCRService.app.services.processors.email_processor import EmailProcessor
from OCRService.app.services.analyzers.image_analyzer import ImageAnalyzer
from OCRService.app.services.analyzers.content_analyzer import ContentAnalyzer
from OCRService.app.services.analyzers.photo_repairer import PhotoRepairer
from OCRService.app.services.analyzers.question_solver import QuestionSolver
from OCRService.app.services.analyzers.document_converter import DocumentConverter
from OCRService.app.services.analyzers.document_optimizer import DocumentOptimizer
from OCRService.app.services.analyzers.translator import Translator
from OCRService.app.services.analyzers.text_recognizer import TextRecognizer
from OCRService.app.services.exporters.document_exporter import IDocumentExportService


# Create an instance of OCRService and register all processors




def get_ocr_service():
    error_handler = RetryErrorHandler(max_retries=3)
    ocr_service = OCRService(error_handler)
    ocr_service.register_processor("base64", Base64Processor())
    ocr_service.register_processor("image", ImageProcessor())
    ocr_service.register_processor("pdf", PDFProcessor())
    ocr_service.register_processor("url", UrlProcessor())
    ocr_service.register_processor("word", WordProcessor())
    ocr_service.register_processor("ppt", PowerPointDocumentProcessor())
    ocr_service.register_processor("rtf", RTFDocumentProcessor())
    ocr_service.register_processor("text", TextDocumentProcessor())
    ocr_service.register_processor("excel", ExcelDocumentProcessor())
    ocr_service.register_processor("email", EmailProcessor())

    ocr_service.register_analyzer("content", ContentAnalyzer())
    ocr_service.register_analyzer("document_convert", DocumentConverter())
    ocr_service.register_analyzer("document_optimize", DocumentOptimizer())
    ocr_service.register_analyzer("document_organize", DocumentOptimizer())
    ocr_service.register_analyzer("image", ImageAnalyzer())
    ocr_service.register_analyzer("photo_repair", PhotoRepairer())
    ocr_service.register_analyzer("question_solve", QuestionSolver())
    ocr_service.register_analyzer("text_recognize", TextRecognizer())
    ocr_service.register_analyzer("translate", Translator())

    ocr_service.register_analyzer("document", DocumentExporter())
    return ocr_service
