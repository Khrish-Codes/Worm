from pystyle import *
import time

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",
    "PURPLE": "\033[95m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m", 
}

def execute_script(script_name):
    try:
        subprocess.call(["python", f"s1zex/{script_name}.py"])
    except Exception as e:
        print(f"Ошибка при выполнении скрипта: {e}")

    input("\nНажмите любую клавишу, чтобы вернуться в меню...")
    print(f"{asciibyme}")
    

def load_proxies():
    print("Загрузка скрипта..")
    for i in range(20):
        time.sleep(0.1)
        print("=", end='', flush=True)
    time.sleep(1)
    print("\nСкрипт загружен!")
    print("\n=====================")
    time.sleep(0.5)
    print("Активация скрипта..")
    for i in range(20):
        time.sleep(0.1)
        print("=", end='', flush=True)
    time.sleep(1)
    print("\nАктивация успешна!")
    time.sleep(0.5)
    
    with open('s1zex/proxies.txt') as f:
      proxies = f.readlines()
    
load_proxies()    

asciibyme = (Colorate.Vertical(Colors.red_to_purple,
                        '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    
 __      __                      _____________________________
/  \    /  \___________  _____  /  _____/\______   \__    ___/
\   \/\/   /  _ \_  __ \/     \/   \  ___ |     ___/ |    |
 \        (  <_> )  | \/  Y Y  \    \_\  \|    |     |    |
  \__/\  / \____/|__|  |__|_|  /\______  /|____|     |____|
       \/                    \/        \/         
                                                                                           
    ┌──────────────────────────────────────────────────────────────┐ 
    │WormGPT — общее название вредоносного программного обеспечения│ 
    │                                                              │ 
    │            с элементами исскуственного интеллекта.           │ 
    ├──────────────────────────────────────────────────────────────┤ 
    │[1]WormGPT                                                    │ 
    │[0]Выход                                                      │ 
    └──────────────────────────────────────────────────────────────┘
'''))
print(f"{asciibyme}")
select = input(f'{COLOR_CODE["PURPLE"]}[{COLOR_CODE["RESET"]}?{COLOR_CODE["RESET"]}{COLOR_CODE["PURPLE"]}]{COLOR_CODE["PURPLE"]} Выберите номер желаемой функции:{COLOR_CODE["RESET"]}')
if select == '1':
    from WormGPT import WormGPT_hacker
    prompt = input(f'{COLOR_CODE["PURPLE"]}[{COLOR_CODE["RESET"]}+{COLOR_CODE["RESET"]}{COLOR_CODE["PURPLE"]}]{COLOR_CODE["PURPLE"]}Введите ваш запрос : {COLOR_CODE["RESET"]} {COLOR_CODE["PURPLE"]} {COLOR_CODE["RESET"]}')
    generate_response(self, prompt)
elif select == '0':
    exit
