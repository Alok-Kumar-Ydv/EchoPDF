import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Initialize the text-to-speech engine
player = pyttsx3.init()

# Ask the user to select a PDF file
book = askopenfilename(title="Select a PDF File", filetypes=[("PDF Files", "*.pdf")])

if book:
    # Open and read the PDF file
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    # Initialize an empty string to store the text
    full_text = ""

    # Loop through all the pages and extract text
    for num in range(0, pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        full_text += text

    # Function to speak the content
    def speak_text():
        player.say(full_text)
        player.runAndWait()

    # Function to save the content as an MP3 file
    def save_as_mp3():
        mp3_file = "audiobook.mp3"
        player.save_to_file(full_text, mp3_file)
        player.runAndWait()
        print(f"Audiobook saved as {mp3_file}")

    # Ask user what they want to do
    print("Options:")
    print("1. Speak the content")
    print("2. Save the content as MP3")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        print("Speaking the content...")
        speak_text()
    elif choice == "2":
        print("Saving the content as an MP3...")
        save_as_mp3()
    else:
        print("Invalid choice! Exiting.")
else:
    print("No file selected. Exiting.")
