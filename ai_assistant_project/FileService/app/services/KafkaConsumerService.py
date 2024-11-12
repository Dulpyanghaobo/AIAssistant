from FileService.app.services.file_service import FileUploader
from fastapi import Depends
from FileService.app.dependencies.dependencies import get_file_uploader

class KafkaConsumerService:
    def __init__(self, consumer_factory):
        self.consumer = consumer_factory.get_consumer()

    def listen_upload_requests(self):
        for message in self.consumer:
            self.process_upload_request(message)

    def process_upload_request(self, message, uploader_file: FileUploader = Depends(get_file_uploader)):
        # Process the upload request
        filename = message['filename']
        filecontent = message['filecontent']
        # Pass the filename and content to the actual uploader
        result = uploader_file.upload_file(filename, filecontent)
        # The result can be a URL or an object that contains the URL
        return result
