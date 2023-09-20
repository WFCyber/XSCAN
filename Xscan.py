from fofa_api import fofa_test as fofa
import argparse
import datetime

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
                                                -------made by Wanfeng
"""

Parser = argparse.ArgumentParser(description="一个工具")
Parser.add_argument('-fofa', "--fofa_inquire", help="fofa查询，参数为语句，扫描的目标host会被保存到./target里")
args = Parser.parse_args()


def fofa_use(fofa_inquire):
    current_time = datetime.datetime.now()
    result = fofa.Fofa(fofa_inquire).json()
    res = set()
    for item in result['results']:
        res.add(item)
    filename = current_time.strftime('fofa_%Y-%m-%d_%H-%M-%S')
    with open(f'./target/{filename}', 'w') as file:
        for item in res:
            file.write(item + '\n')
    print(result)
    print(f'结果保存在./target/{filename}')

if __name__ == '__main__':
    fofa_use(args.fofa_inquire)
