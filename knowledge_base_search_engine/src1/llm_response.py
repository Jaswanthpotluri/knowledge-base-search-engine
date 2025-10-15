import google.generativeai as genai

def generate_answer(prompt, temperature=0.2, model_name="models/gemini-2.5-flash"):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(
        prompt,
        generation_config={"temperature": temperature}
    )
    return response.text
