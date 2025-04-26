
def get_response(user_input):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm doing great, thanks!",
        "bye": "Goodbye!",
    }
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")
