# # -*- coding: utf-8 -*-
# """
# Created on Mon Nov  9 23:36:41 2020

# @author: Peanut
# """


# #coding=gbk
# import os
# import wave
# import numpy as np
# import pylab as plt
 
# CutTimeDef = 3 #以1s截断文件
# # CutFrameNum =0
 
 
# path = r"C:\Users\Peanut\Desktop"
# files = os.listdir(path)
# files = [path + "\\" + f for f in files if f.endswith('.wav')]
 
# def SetFileName(WavFileName):
#     for i in range(len(files)):
#         FileName = files[i]
#         print("SetFileName File Name is ", FileName)
#         FileName = WavFileName;
 
# def CutFile():
#     for i in range(len(files)):
#         FileName = files[i]
#         print("CutFile File Name is ",FileName)
#         f = wave.open(r"" + FileName, "rb")
#         params = f.getparams()
#         print(params)
#         nchannels, sampwidth, framerate, nframes = params[:4]
#         CutFrameNum = framerate * CutTimeDef
#          # 读取格式信息
#          # 一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte    单位）, 采
#          # 样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
 
#         print("CutFrameNum=%d" % (CutFrameNum))
#         print("nchannels=%d" % (nchannels))
#         print("sampwidth=%d" % (sampwidth))
#         print("framerate=%d" % (framerate))
#         print("nframes=%d" % (nframes))
#         str_data = f.readframes(nframes)
#         f.close()# 将波形数据转换成数组
#         # Cutnum =nframes/framerate/CutTimeDef
#         # 需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
#         wave_data = np.fromstring(str_data, dtype=np.short)
#         wave_data.shape = -1, 2
#         wave_data = wave_data.T
#         temp_data = wave_data.T
#         # StepNum = int(nframes/200)
#         StepTotalNum = 0;
#         StepNum = int(CutFrameNum/2)
#         haha = 0
#         while (StepTotalNum < int((nframes-2*StepNum)/2)) :
#         # for j in range(int(Cutnum)):
#             print("Stemp=%d" % (haha))
#             FileName = "D:\\testcutresults\\" + files[i][-17:-4] +"-"+ str(haha+1) + ".wav"
#             print(FileName)
#             temp_dataTemp = temp_data[StepNum * (haha):StepNum * (haha + 1)]
#             haha = haha + 1;
#             StepTotalNum = haha * StepNum;
#             temp_dataTemp.shape = 1, -1
#             temp_dataTemp = temp_dataTemp.astype(np.short)# 打开WAV文档
#             f = wave.open(FileName, "wb")#
#             # 配置声道数、量化位数和取样频率
#             f.setnchannels(nchannels)
#             f.setsampwidth(sampwidth)
#             f.setframerate(framerate)
#              # 将wav_data转换为二进制数据写入文件
#             f.writeframes(temp_dataTemp.tostring())
#             f.close()
 
# if __name__ == '__main__' :
#     CutFile()
 
 
#     print("Run Over")


import os
import wave
import numpy as np
import pylab as plt

#----------------------path改
path = r"C:\Users\Peanut\Desktop"
files = os.listdir(path)
files = [path + "\\" + f for f in files if f.endswith('.wav')]
CutTime = 3 #单位长度4s

def CutAudios():
    for i in range(len(files)):
        FileName = files[i]
        f = wave.open(r"" + FileName, 'rb')
        params = f.getparams() #读取音频文件信息
        nchannels, sampwidth, framerate, nframes = params[:4]  #声道数, 量化位数, 采样频率, 采样点数   
        str_data = f.readframes(nframes)
        f.close()
     
        wave_data = np.frombuffer(str_data, dtype=np.short)
        #根据声道数对音频进行转换
        if nchannels > 1:
                wave_data.shape = -1, 2
                wave_data = wave_data.T
                temp_data = wave_data.T
        else:
                wave_data = wave_data.T
                temp_data = wave_data.T

        CutFrameNum = framerate * CutTime  
        Cutnum =nframes/CutFrameNum  #音频片段数
        StepNum = int(CutFrameNum)
        StepTotalNum = 0
   
        for j in range(int(Cutnum)):
            #-------------------改
            FileName = r"D:\testcutresults\\" + files[i][-7:-4] +"-"+ str(j) + ".wav"
            temp_dataTemp = temp_data[StepNum * (j):StepNum * (j + 1)]
            StepTotalNum = (j + 1) * StepNum
            temp_dataTemp.shape = 1, -1
            temp_dataTemp = temp_dataTemp.astype(np.short)# 打开WAV文档
            f = wave.open(FileName, 'wb')
            # 配置声道数、量化位数和取样频率
            f.setnchannels(nchannels)
            f.setsampwidth(sampwidth)
            f.setframerate(framerate)
            f.writeframes(temp_dataTemp.tostring())  # 将wav_data转换为二进制数据写入文件
            f.close()
            
if __name__ == '__main__' :
    CutAudios()
