"""
Functions as a connector/wrapper for the Llama3 LLM, utilizing llama.cpp.
Requires that the path to the LLM .gguf file is saved in a local .env file
"""
import os
from dotenv import load_dotenv
from llama_cpp import Llama
import collections


class Transponder:

    load_dotenv()
    _MODEL_PATH = os.getenv("MODEL_PATH")
    _CONTEXT_LENGTH = 25

    def __init__(self):
        self.context = collections.deque()
        n_gpu_layers = 10
        seed = 1337
        n_ctx = 2048

        self.llm = Llama(
            self._MODEL_PATH,
            n_gpu_layers=n_gpu_layers,
            seed=seed,
            n_ctx=n_ctx
        )

    def prompt(self, prompt):
        """
        Prompts the LLM to generate output, and returns the response.

        :param prompt: The incoming user query to use for generation.
        :return: A response generated by the LLM based on the prompt.
        """
        self._save_context(prompt)

        output = self.llm(
            prompt=self._get_context(),
            max_tokens=256,
            stop=["Q: ", "\n"],
            echo=True
        )
        prompt_and_response = output.get("choices")[0].get("text")
        response = prompt_and_response.replace(self._get_context(), "")
        self._save_context(response)

        return response

    def _save_context(self, message):
        """
        Private method for maintaining temporary context retention. Saves
        incoming prompts to a deque for the LLM to use as context later.

        :param message: Incoming prompt being passed to the LLM
        """
        if len(self.context) >= self._CONTEXT_LENGTH:
            self.context.popleft()

        self.context.append(message)

    def _get_context(self):
        """
        Private method for returning a portion of the conversation context as
        a string.

        :return: String representing conversation context.
        """
        return " ".join(self.context)
