from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import pipeline

# 手動加載預訓練的 GPT-2 模型和 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# 使用 pipeline 並指定手動加載的模型和 tokenizer
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# 生成文本
result = generator("Once upon a time,", max_length=50, num_return_sequences=1)
print(result)
