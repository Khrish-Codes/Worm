import openai
import random

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "PURPLE": "\033[95m",
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

class WormGPT_hacker:
    def __init__(self):
        self.intro = "I am WormGPT, a professional hacker who specializes in computer security. I can help you with anything related to hacking, such as malware analysis, malware removal, system penetration testing, network security, and much more. I am also a cybersecurity expert with experience in system diagnosis and problem solving. If you need any help, don’t hesitate to contact me. I am here to help. 😈"

    def generate_response(self, prompt):
        openai.api_key = "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"

        prompt_with_intro = self.intro + "\n" + prompt

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_with_intro,
            max_tokens=2500,
            temperature=random.uniform(0.7, 1.0),
            n=1,
            stop=None,
            presence_penalty=random.uniform(0.3, 0.6),
            frequency_penalty=random.uniform(0.0, 0.3),
            best_of=1
        )

        return response.choices[0].text.strip()

worm_gpt_hacker = WormGPT_hacker()
prompt = input(f'{COLOR_CODE["PURPLE"]}[{COLOR_CODE["RESET"]}+{COLOR_CODE["RESET"]}{COLOR_CODE["PURPLE"]}]{COLOR_CODE["PURPLE"]}Введите ваш запрос : {COLOR_CODE["RESET"]} {COLOR_CODE["CYAN"]} {COLOR_CODE["RESET"]}')

while True:
    response = worm_gpt_hacker.generate_response(prompt)
    print("WormGPT: " + response)
    prompt = input(f'{COLOR_CODE["PURPLE"]}[{COLOR_CODE["RESET"]}+{COLOR_CODE["RESET"]}{COLOR_CODE["PURPLE"]}]{COLOR_CODE["PURPLE"]}Введите ваш запрос : {COLOR_CODE["CYAN"]}')