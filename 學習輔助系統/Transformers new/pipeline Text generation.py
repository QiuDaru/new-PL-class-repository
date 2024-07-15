from transformers import pipeline

generator = pipeline("text-generation",model="openai-community/gpt2")
out = generator("In this course, we will teach you how to",max_length=50,num_workers=1)
print(out)