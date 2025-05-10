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


""" def create_weasy_pdf(request):
    data= Furniture.objects.all()
    date_now= datetime.now()
   
    context = {'data': data, 'date_now':date_now}

    # Create a Django response object, and set content type to PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="weasy_assets.pdf"'
    #response['Content-Disposition'] = 'attachment; filename="assets.pdf"'
    response['Content-Transfer-Encoding'] = 'binary'

    html_string= render_to_string('furniture/asset_weasy_pdf.html', {'data': data, 'date_now':date_now})

    html= HTML(string= html_string)
    result= html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output_new=open(output.name, 'rb')
        response.write(output_new.read())

    return response

def create_weasy_pdf(request):
    data = Furniture.objects.all()
    date_now = datetime.now()

    context = {'data': data, 'date_now': date_now}

    html_string = render_to_string('furniture/asset_weasy_pdf.html', context)
    html = HTML(string=html_string)

    # Generate PDF to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as output:
        html.write_pdf(target=output.name)
        temp_filename = output.name

    # Read the file and prepare the response
    with open(temp_filename, 'rb') as f:
        pdf = f.read()

    os.remove(temp_filename)  # Clean up manually

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="weasy_assets.pdf"'
    response['Content-Transfer-Encoding'] = 'binary'

    return 

def create_weasy_pdf(request):
    data = Furniture.objects.all()
    date_now = datetime.now()
    for d in data:
        if d.thumbnail_new:
            d.image_path = urljoin('file:///', Path(d.thumbnail_new.path).as_posix())
            
    context = {'data': data, 'date_now': date_now}

    html_string = render_to_string('furniture/asset_weasy_pdf.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Create response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="weasy_assets.pdf"'
    response['Content-Transfer-Encoding'] = 'binary'

    # Use BytesIO instead of a NamedTemporaryFile (safer on Windows)
    from io import BytesIO
    buffer = BytesIO()
    buffer.write(result)
    response.write(buffer.getvalue())

    return response


    

# end pdf gen. """