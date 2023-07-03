class ITextRecognizerService:
    def recognize_text(self, image):
        raise NotImplementedError

class IDocumentExportService:
    def export_document(self, document):
        raise NotImplementedError
