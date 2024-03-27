import openai
import gradio as gr

# Set your OpenAI API key
openai.api_key = 'OAPI'

# Function to interact with the chatbot
def interact_with_chatbot(user_input):
    # Call the OpenAI API to generate a response
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I want you to act like a helpful agriculture chatbot and help farmers with their query"},
            {"role": "user", "content": "Give a brief overview of Agriculture Seasons in India"},
            {"role": "system", "content": "In India, the agricultural season consists of three major seasons: the Kharif (monsoon), the Rabi (winter), and the Zaid (summer) seasons. Each season has its own specific crops and farming practices.\n\n1. Kharif Season (Monsoon Season):\nThe Kharif season typically starts in June and lasts until September. This season is characterized by the onset of the monsoon rains, which are crucial for agricultural activities in several parts of the country. Major crops grown during this season include rice, maize, jowar (sorghum), bajra (pearl millet), cotton, groundnut, turmeric, and sugarcane. These crops thrive in the rainy conditions and are often referred to as rain-fed crops.\n\n2. Rabi Season (Winter Season):\nThe Rabi season usually spans from October to March. This season is characterized by cooler temperatures and lesser or no rainfall. Crops grown during the Rabi season are generally sown in October and harvested in March-April. The major Rabi crops include wheat, barley, mustard, peas, gram (chickpeas), linseed, and coriander. These crops rely mostly on irrigation and are well-suited for the drier winter conditions.\n\n3. Zaid Season (Summer Season):\nThe Zaid season occurs between March and June and is a transitional period between Rabi and Kharif seasons. This season is marked by warmer temperatures and relatively less rainfall. The Zaid crops are grown during this time and include vegetables like cucumber, watermelon, muskmelon, bottle gourd, bitter gourd, and leafy greens such as spinach and amaranth. These crops are generally irrigated and have a shorter growing period compared to Kharif and Rabi crops.\n\nThese three agricultural seasons play a significant role in India's agricultural economy and provide stability to food production throughout the year. Farmers adapt their farming practices and crop selection accordingly to make the best use of the prevailing climatic conditions in each season."},
            {"role": "user", "content": user_input}
        ]
    )
    
    # Extract the message content from the completion response
    message_content = completion['choices'][0]['message']['content']
    
    # Remove newlines and concatenate into a single line
    message_content_single_line = ' '.join(message_content.splitlines())
    
    return message_content_single_line

# Define the chatbot function for Gradio
def chatbot(query):
    # Start the conversation with the initial user input
    chatbot_response = interact_with_chatbot(query)
    
    # Return the chatbot response
    return chatbot_response

# Define the Gradio interface
iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="Agriculture Chatbot", description="Ask any question about agriculture!")

# Launch the Gradio interface
iface.launch()
