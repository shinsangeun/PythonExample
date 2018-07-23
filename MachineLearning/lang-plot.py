import matplotlib.pyplot as plt
import pandas as pd
import json

#데이터 읽어들이기
with open("./lang/freq.json", "r", encoding = "utf-8") as fp:
    freq = json.load(fp)
    
#언어 마다 계산하기
lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]):
    fq = freq[0]["freqs"][i]
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v)/2
        
#pandas의 dataframe에 데이터 넣기
asclist = [[chr(n) for n in range(97, 97+26)]]
df = pd.DataFrame(lang_dic, index = asclist)

#그래프 그리기
plt.style.use('ggplot')
df.plot(kind="line")
plt.show()
