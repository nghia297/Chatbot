from transformers import pipeline
corrector = pipeline("text2text-generation", model="bmd1905/vietnamese-correction")
print(corrector("cho em hỏi họ phí ngành koa học mái tính",max_length=128))