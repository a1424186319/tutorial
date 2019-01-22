
import optparse
import time
import zhineng  # 这里我上端代码独立生成一个文件“apiutil.py"，所以要导入一下
import json


app_key = 'pdR9GrQWm4Db1lg4'
app_id = '2110733945'
a = input('请输入想说的话:')
questionS = a


def anso(questionS):
    str_question = questionS
    session = 10000
    ai_obj = zhineng.AiPlat(app_id, app_key)

    rsp = ai_obj.getNlpTextChat(session, str_question)
    if rsp['ret'] == 0:
        print('............................................................')
        ask = (rsp['data'])['answer']
        print(ask)
    else:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))


if __name__ == '__main__':
    anso(questionS)