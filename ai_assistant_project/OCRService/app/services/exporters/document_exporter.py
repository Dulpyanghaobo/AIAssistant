from OCRService.app.services.ocr_commissioning_service import IDocumentExportService
class DocumentExporter:
    def export(self, document):
        return self.service.export_document(document)