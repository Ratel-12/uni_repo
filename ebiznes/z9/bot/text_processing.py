import openai

class ChatInstance:
    def __init__(self) -> None:
        self.api_key = ""
        with open("credentials/openai.txt", mode="r") as key_file:
            self.api_key = key_file.read()
        openai.api_key = self.api_key

        self.history=[{"role": "system", "content": "You are a friendly Discord chatbot."}]

    def process_message(self, message) -> str:
        self.history.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history
        )
        response_innards = response['choices'][0]['message']['content']
        self.history.append({"role": "assistant", "content": response_innards})
        return response_innards
