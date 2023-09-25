import fofa
import argparse
import datetime

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def show_banner():
    text = """
                                                                      ,--. 
     ,--,     ,--,    .--.--.      ,----..      ,---,               ,--.'| 
     |'. \   / .`|   /  /    '.   /   /   \    '  .' \          ,--,:  : | 
     ; \ `\ /' / ;  |  :  /`. /  |   :     :  /  ;    '.     ,`--.'`|  ' : 
     `. \  /  / .'  ;  |  |--`   .   |  ;. / :  :       \    |   :  :  | | 
      \  \/  / ./   |  :  ;_     .   ; /--`  :  |   /\   \   :   |   \ | : 
       \  \.'  /     \  \    `.  ;   | ;     |  :  ' ;.   :  |   : '  '; | 
        \  ;  ;       `----.   \ |   : |     |  |  ;/  \   \ '   ' ;.    ; 
       / \  \  \      __ \  \  | .   | '___  '  :  | \  \ ,' |   | | \   | 
      ;  /\  \  \    /  /`--'  / '   ; : .'| |  |  '  '--'   '   : |  ; .' 
    ./__;  \  ;  \  '--'.     /  '   | '/  : |  :  :         |   | '`--'   
    |   : / \  \  ;   `--'---'   |   :    /  |  | ,'         '   : |       
    ;   |/   \  ' |               \   \ .'   `--''           ;   |.'       
    `---'     `--`                 `---`                     '---'    
            version:1.0                              -------made by Wanfeng
    """
    print(text)

Parser = argparse.ArgumentParser(description="一个工具")
Parser.add_argument('-fofa', "--fofa_inquire", help="fofa查询，参数为语句，扫描的目标host会被保存到./target里")

args = Parser.parse_args()


def fofa_use(fofa_inquire):
    show_banner()
    current_time = datetime.datetime.now()
    result = fofa.Fofa(fofa_inquire).json()
    time=current_time.strftime('%Y.%m.%d %H:%M:%S')
    res = set()
    print(BLUE + f'查询语句为{result["query"]}' + RESET,end='\t')
    print(BLUE + f'时间：{time}' + RESET)
    print('----------------------------------------------------')
    for item in result['results']:
        res.add(item)
    filename = current_time.strftime('fofa_%Y-%m-%d_%H-%M-%S')
    with open(f'./target/{filename}', 'w') as file:
        for item in res:
            print(RED + '|-' + RESET, end='')
            print(item)
            file.write(item + '\n')
    print('----------------------------------------------------')
    print(f'结果保存在./target/{filename}')


if __name__ == '__main__':
    fofa_use(args.fofa_inquire)
