class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1"

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, messages):
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": messages
        }
        response = requests.post(url, headers=self._headers(), json=payload)
        return response.json()

    def generate_text(self, prompt):
        url = f"{self.base_url}/completions"
        payload = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "max_tokens": 150
        }
        response = requests.post(url, headers=self._headers(), json=payload)
        return response.json()

    def edit_text(self, input_text, instruction):
        url = f"{self.base_url}/edits"
        payload = {
            "model": "text-davinci-edit-001",
            "input": input_text,
            "instruction": instruction
        }
        response = requests.post(url, headers=self._headers(), json=payload)
        return response.json()