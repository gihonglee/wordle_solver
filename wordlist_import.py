import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns


class wordle():
    def __init__(self):
        path1 = "asset/wordle-words.txt"
        path2 = "asset/wordle-answers.txt"
        self.allword_list = []
        self.answer_list = []
        with open(path1) as file_obj:
            for line in file_obj:
                word = line.strip()
                self.allword_list.append(word)
        with open(path2) as file_obj:
            for line in file_obj:
                word = line.strip()
                self.answer_list.append(word)

    def choose_word(self):
        self.wordToday = random.choice(self.allword_list)

    def word_analysis(self):
        char_set = set()
        result_dict = {}
        for word in self.answer_list:
            for char in word:
                if char not in char_set:
                    result_dict[char] = 1
                    char_set.add(char)
                else:
                    result_dict[char] += 1
        df = pd.DataFrame.from_dict(result_dict, orient='index')
        return df

    def word_analysis2(self):
        result = []
        for i in range(5):
            result_dict = {}
            for word in self.allword_list:
                if word[i] not in result_dict:
                    result_dict[word[i]] = 1
                else:
                    result_dict[word[i]] = result_dict[word[i]] + 1    
            result.append(result_dict)       
        df = pd.DataFrame(result[0], index=[0])
        for i in range(1,5):
            df = df.append(pd.DataFrame(result[i], index=[i]))

        df["index"] = [0,1,2,3,4]
        df = df.set_index("index")
        res = df.div(df.sum(axis=1), axis=0)

        # print(res.reset_index())
        return df, res



w = wordle()

df,res = w.word_analysis2()
ax = sns.heatmap(res, linewidth=0.5)
plt.show()

maxValueIndex = df.idxmax(axis = 1)
print(maxValueIndex)
# print(df)
# df = pd.DataFrame(columns=['A'])
# for i in range(5):
#     df = df.append({'A': i}, ignore_index=True)
# print(df)

# df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])
# df
# #    A  B
# # x  1  2
# # y  3  4
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'), index=['x', 'y'])
# df.append(df2)
                

