from llama_cpp import Llama
import os
from dotenv import load_dotenv

load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH")


class Transponder:

    def __init__(self):
        self.response = None
        n_gpu_layers = 10
        seed = 1337
        n_ctx = 2048

        self.llm = Llama(
            MODEL_PATH,
            n_gpu_layers=n_gpu_layers,
            seed=seed,
            n_ctx=n_ctx
        )

    def prompt(self, message):
        output = self.llm(prompt=message, max_tokens=32, stop=["Q: ", "\n"], echo=True)
        prompt_and_response = output.get("choices")[0].get("text")
        self.response = prompt_and_response.replace(message, "")
