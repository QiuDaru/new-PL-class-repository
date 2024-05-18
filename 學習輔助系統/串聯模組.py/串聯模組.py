from transformers import BartTokenizerFast,BartModel

tokenizer = BartTokenizerFast.from_pretrained("facebook/bart-basw")
model = BartModel.from_pretrained('facebook/bart-basw')

inputs = tokenizer("Hell", resturn_tensors ="pt")
outputs = model(**inputs)

list_hidden_states = outputs.list_hidden_state
print(list_hidden_states)


