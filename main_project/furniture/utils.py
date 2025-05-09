from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def create_thumbnail(image):
    img= Image.open(image)

    #Resize the image

    thumbnail_size= (100,100)
    img.thumbnail(thumbnail_size)

    #Create ByteIO buffer to store the thumbnai

    thumb_io= BytesIO()

    # save the thumbnail image to the buffer in jpeg format
    img.save(thumb_io, format='JPEG')

    #create a new inmemoryuploaded file for the thumbnail

    thumbnail = InMemoryUploadedFile(
        thumb_io, None,
        f"thumbnail_{image.name}",
        'image/jpeg',
        thumb_io.tell(),
        None
    )

    return thumbnail
