from OCRService.app.services.analyzers.IAnalyzer import IAnalyzer

class TextRecognizer(IAnalyzer):
    def analyze(self, text):
        print("TextRecognizer analyze")
        pass
