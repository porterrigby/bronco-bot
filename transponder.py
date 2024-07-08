import transformers
import torch

class Transponder:


    def __init__(self):
        model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

        global pipeline
        pipeline = transformers.pipeline(
            "text-generation",
            model=model_id,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )

        global terminators
        terminators = [
            pipeline.tokenizer.eos_token_id,
            pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        global context
        context = ["You are a pirate chatbot who always responds in pirate speak!"]

    def update_context(self, message):
        context.append(message)

    def get_context(self):
        return context


    def prompt(self, message):

        messages = [
            {"role": "system", "content": self.get_context()},
            {"role": "user", "content": message},
        ]

        outputs = pipeline(
            messages,
            max_new_tokens=256,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )

        output = outputs[0]["generated_text"][-1]
        dialog = output.get("content")

        print(output)

        return dialog
