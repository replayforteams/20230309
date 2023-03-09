import pandas as pd

#获取[1,7],我们感兴趣的值，然后再通过drop_duplicates去重
data = pd.DataFrame(pd.read_excel("target.xlsx", usecols=[1, 7], header=0, ))
re_row = data.drop_duplicates(subset='Signal Name')
dict1 = {}
msgDict={}
print(re_row)
# i[2]是信号名字
# i[1]是message id号
#  把信号名字i[2]作为key， id号作为value，原因是避免key重复
def fishdata():
    global dt
    for i in re_row.itertuples():
        dict1[i[2]] = i[1]
    # 再把字典的key value顺序调换下，并转成tuple,为了转成期望的i[1]:[i[0],i[00])
    dt = [(i[1], i[0]) for i in dict1.items()]
    # print(dt)





def outdict():
    for (key, value) in dt:
        if key not in msgDict:  # 判断是否存在字典里面，因为第一次的时候不存在字典里面，所以字典key的初始化只执行一次
            msgDict[key] = [value]
            # print(key, value)
        else:
            msgDict[key].append(value)

fishdata()
outdict()
# print(msgDict['GW_50'])

#
#获取[1,7],我们感兴趣的值，然后再通过drop_duplicates去重
data = pd.DataFrame(pd.read_excel("target.xlsx", usecols=[5, 7], header=0, ))
re_row = data.drop_duplicates(subset='Signal Name')
crcDict = {}

print(re_row)
# # i[2]是信号名字
# # i[1]是byte NO
# #  把信号名字i[2]作为key， id号作为value，原因是避免key重复
def fishByteNo():
    global dt
    for i in re_row.itertuples():
        crcDict[i[2]] = i[1]

fishByteNo()

print(msgDict['GW_50'])
print(crcDict['LAS_DTC2_LowByte'])
msg=''
msgtimerdef = ''
msgdef =''

def checkhasCRCName(inputkey):
    if crcDict[inputkey] !=None:
        return crcDict[inputkey]
    else:
        return  -1

#查询
#创建显示的字符串   msTimer GW50;
for key,value  in msgDict.items():
    # print(key,value)
    msgtimerdef += 'msTimer '+str(key).lower() +';\n'
#创建字符串  message CAN1::GW_50 msg50;
for key,value  in msgDict.items():
    # print(key,value)
    msgdef += 'message CAN1::'+key+' msg_'+ str(key).lower() + ';\n'
#创建字符串   byte crc_temp507[64];
for key,value  in msgDict.items():
    print(key,value)
    for i in value:
        if "CRCCheck".upper() in ( str(i).upper()):#找到对应的crccheck字段

            result = checkhasCRCName(str(i))
            print(int(result))
            print(str(i[-3:]))
            if str(i[-3:]) in str(key)[-3:] and result != -1: #找到和messageid后缀一致的byte id
                break
        else:
            result = -1

    if result != -1:
        msgdef += 'byte '+ 'crc_temp_' + str(key).lower()+'['+str(int(result))+']' +';\n'





msgtimerdef= '\nvariables \n{\n'+msgdef+'\n'+msgtimerdef +'\n}\n'

print(msgtimerdef)
msg1=''
# print(msgtimerdef)
#创建 信号的初始化msg188.TCU_ShiftinProgress.phys = 0;
#signal 成员列表
msgSignal=''
msglist =[]
for key,value  in msgDict.items():
    # print(key,value)
    tempvalue = value

    for i in tempvalue:
        msgSignal += str(str(key).lower()+'.'+str(i)+'.phys = 0;\n')
        print(f'1111111111{i}')
        print(msgSignal)
        print('2222222222')
    else:
        msg1+='on timer ' +str(key) +'\n'+'{'+'\n' +str(msgSignal)+'\n'+'}'+'\n'
        # msglist.append(msg1)
        # msg1=''
        msgSignal=''
        # continue
    # msg += 'on timer ' + key + '\n{\n}\n'
    # print(msgSignal)
print(msg1)
# for i in msglist:
#     print(i)
# for key,value  in msgDict.items():
#     print(key,value)
#     # msgdef = '\n variables \n{\n'
#     msg += 'on timer ' +key +'\n{\n}\n'


#
# # ---------------------
# # 判断有几个checksum
# # 输入frame name
# # 输出 个数
# def getCRCCheckNumber(name):
#     crcnum = 0
#     for signalList in res:
#         if name == signalList["Frame Name"]:
#             if "CRCCheck" in signalList["Signal Name"]:
#                 print(signalList["Signal Name"])
#                 crcnum += 1
#     return crcnum
#
#
# print(getCRCCheckNumber("GW_50"))
# ---------------------


# ----------------------
# 记录checksum对应的属性值

# frame name作为唯一关键字
# ----------------------

# -------------------------
# 文件的创建与保存
# -------------------------

# ---------------------
# 创建msg名称   message CAN1::GW_3E7 msg3E7;
# 创建 timer   msTimer GW3E7;
# 创建dlc       int dlc530=8;
# 创建rcount的计数器     int Rcount365=0;
# 创建crc data数组        byte crc_temp26A[8];
# 创建循环计数器    int i38A;
# ------------------------------

# ------------------------------
# 创建  on start
# 创建 on timer  on timer GW507
# ------------------------


# --------------------------
# ui界面的导入
# ---------------------------
