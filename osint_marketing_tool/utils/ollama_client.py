class OllamaClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.ollama.com/v1"

    def send_request(self, endpoint, data):
        import requests

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers=headers)
        
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} - {response.text}")
        
        return response.json()

    def get_model_info(self, model_name):
        return self.send_request(f"models/{model_name}/info", {})

    def generate_text(self, model_name, prompt):
        data = {
            "model": model_name,
            "prompt": prompt
        }
        return self.send_request("generate", data)