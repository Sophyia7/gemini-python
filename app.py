from flask import Flask, request, render_template
import google.generativeai as genai
import os 
import markdown

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv('YOUR_API_KEY'))

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Start AI Conversations
chat = model.start_chat(history=[])

@app.route('/chat', methods=['GET', 'POST'])
def chat_view():
    if request.method == 'POST':
        user_input = request.form.get('message')
        response = chat.send_message(user_input)
        formatted = markdown.markdown(response.text)
        # return {'message': response.text}
        return {'message': formatted}
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)