import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(["What's in this photo?", img])