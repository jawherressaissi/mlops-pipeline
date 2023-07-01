from flask import Flask, request
import torch
from peft import PeftModel, PeftConfig
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)

peft_model_id = "bigscience/mt0-small_LORA_SEQ_2_SEQ_LM"
config = PeftConfig.from_pretrained(peft_model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(config.base_model_name_or_path)
model = PeftModel.from_pretrained(model, peft_model_id)
model.eval()

tokenizer = AutoTokenizer.from_pretrained(peft_model_id)

@app.route('/api/sa/classify', methods=('POST',))
def classify():
    data = request.get_json()
    if 'text' in data:
        text = data['message']
    else:
        return "Error: No text passed as a parameter.", 400
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(input_ids=inputs["input_ids"], max_new_tokens=10)
    return tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0].title()
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)