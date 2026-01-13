class GeminiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.gemini.com/v1"

    def get_market_data(self, symbol):
        endpoint = f"{self.base_url}/marketdata/{symbol}"
        response = self._make_request(endpoint)
        return response

    def place_order(self, symbol, amount, price, side):
        endpoint = f"{self.base_url}/order/new"
        order_data = {
            "symbol": symbol,
            "amount": amount,
            "price": price,
            "side": side
        }
        response = self._make_request(endpoint, method='POST', data=order_data)
        return response

    def _make_request(self, endpoint, method='GET', data=None):
        headers = {
            "Content-Type": "application/json",
            "X-GEMINI-APIKEY": self.api_key
        }
        if method == 'POST':
            response = requests.post(endpoint, headers=headers, json=data)
        else:
            response = requests.get(endpoint, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} - {response.text}")

        return response.json()