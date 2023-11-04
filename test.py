# import PyPDF2
# from gtts import gTTS




# # Function to extract text from a PDF file
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     pdf_file = open(pdf_path, 'rb')
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
    
#     for page_num in range(len(pdf_reader.pages)):
#         page = pdf_reader.pages[page_num]
#         text += page.extract_text()
    
#     pdf_file.close()
#     return text




# # Function to convert text to speech and save it as an MP3 file
# def text_to_mp3(text, mp3_file):
#     tts = gTTS(text, lang='en')
#     tts.save(mp3_file)




# # Main function
# if __name__ == "__main__":
#     pdf_path = "D:/Projects/Python Projects/PDF_To_mp3/CV.pdf"
#     mp3_file = "output_audio.mp3"
    
#     text = extract_text_from_pdf(pdf_path)
#     text_to_mp3(text, mp3_file)
    
#     print(f"Conversion completed. MP3 file saved as {mp3_file}")
