from OCRService.app.services.analyzers.IAnalyzer import IAnalyzer
from OCRService.app.services.processors.IInputProcessor import IInputProcessor
from OCRService.app.services.errorHandler.IErrorHandler import IErrorHandler
from OCRService.app.services.ocr_commissioning_service import IDocumentExportService

class OCRService:
    def __init__(self, error_handler: IErrorHandler):
        self.error_handler = error_handler
        self.processors = {}
        self.analyzers = {}
        self.exporters = {}

    def register_processor(self, processor_type: str, processor: IInputProcessor):
        self.processors[processor_type] = processor

    def unregister_processor(self, processor_type: str):
        self.processors.pop(processor_type, None)

    def register_analyzer(self, analyzer_type: str, analyzer: IAnalyzer):
        self.analyzers[analyzer_type] = analyzer

    def unregister_analyzer(self, analyzer_type: str):
        self.analyzers.pop(analyzer_type, None)

    def register_exporter(self, exporter_type: str, exporter: IDocumentExportService):
        self.exporters[exporter_type] = exporter

    def unregister_exporter(self, exporter_type: str):
        self.exporters.pop(exporter_type, None)

    def process_input(self, input_data, processor_type):
        processor = self.processors.get(processor_type)
        if not processor:
            raise ValueError(f"No processor for type: {processor_type}")
        return self.error_handler.handle_error(processor.process, input_data)

    def analyze(self, data, analyzer_type):
        analyzer = self.analyzers.get(analyzer_type)
        if not analyzer:
            raise ValueError(f"No analyzer for type: {analyzer_type}")
        return self.error_handler.handle_error(analyzer.analyze, data)

    def export_document(self, document, exporter_type):
        exporter = self.exporters.get(exporter_type)
        if not exporter:
            raise ValueError(f"No exporter for type: {exporter_type}")
        return self.error_handler.handle_error(exporter.export, document)
