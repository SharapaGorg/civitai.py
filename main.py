from civitaiApi import get_models
from civitaiApi import types

models = get_models("SharapaGorg", types.LORA)

for model in models:
    print(model.name)
