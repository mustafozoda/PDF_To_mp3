import PyPDF2
from gtts import gTTS


def pdf_to_text(pdf_link):
    text_from_pdf = ""
    pdf_file = open(pdf_link, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_numbers in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_numbers]
        text_from_pdf += page.extract_text()

    pdf_file.close()
    return text_from_pdf


def text_to_mp3(text, mp3_file):
    speach_from_text = gTTS(text, lang='en')
    speach_from_text.save(mp3_file)


if __name__ == "__main__":
    pdf_link = "D:/Projects/Python Projects/PDF_To_mp3/text.pdf"
    mp3_file = "audio.mp3"

    text = pdf_to_text(pdf_link)
    text_to_mp3(text, mp3_file)

    print(f"Conversion completed. MP3 file saved as {mp3_file}")
