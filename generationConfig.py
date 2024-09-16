# use for configure the output


import google.generativeai as genai

generation_config = genai.GenerationConfig(
    temperature=0.1,  # 0,0 e 2,0
    max_output_tokens=50,
    top_p=0.9,
    top_k=50 # test 50
)
