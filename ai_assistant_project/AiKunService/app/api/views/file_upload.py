import errno
from fastapi import APIRouter, UploadFile, File, Depends
from AiKunService.app.api.services.file_service import FileUploader
from AiKunService.app.api.dependencies.dependencies import get_file_uploader
import os
import uuid
router = APIRouter()
@router.post("/file_upload")
async def file_loader(file: UploadFile = File(...), uploader_file: FileUploader = Depends(get_file_uploader)):
    filename, file_extension = os.path.splitext(file.filename)
    new_file_name = str(uuid.uuid4()) + file_extension
    temp_file = "tmp/" + new_file_name
    print("temp_file" + temp_file)

    # check if directory exists, if not create it
    if not os.path.exists(os.path.dirname(temp_file)):
        try:
            os.makedirs(os.path.dirname(temp_file))
            print("temp_file"+temp_file)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(temp_file, "wb") as buffer:
        buffer.write(await file.read())
    oss_file_path = os.path.join('tmp', new_file_name)
    print("oss_file_path"+oss_file_path)
    url = uploader_file.upload_file(temp_file, oss_file_path)
    print("upload_url"+url)

    # 删除临时文件
    os.remove(temp_file)

    return {"upload_url": url}
