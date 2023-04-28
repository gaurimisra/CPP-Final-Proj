import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.http import FileResponse
from vehicle import models

# Generate PDF File
def genPdf1(request):
    # Create ByteStream Buffer
    buf = io.BytesIO()
    # Create a Canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 10)

    # Lines of text
    customer=models.Customer.objects.get(user_id=request.user.id)
    enquiries=models.Request.objects.all().filter(customer_id=customer.id).exclude(status='Pending')

    #Loop
    textob.textLine("Vehicle Name    |    Vehicle Number    |    Problem Description    |    Enquiry Date    |    Total Cost")
    # for line in lines:
    #     textob.textLine(line)
    for enq in enquiries:
        textob.textLine(str(enq.vehicle_name) + "    |    " + str(enq.vehicle_no) + "    |    " + str(enq.problem_description) + "    |    " + str(enq.date) + "    |    " + str(enq.cost))

    # Finish
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='PDF_File.pdf')
