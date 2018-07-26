import math, sys
from konlpy.tag import Twitter

class BayesianFilter:
    """베이지안 필터"""
    def __init__(self):
        self.words = set() #출현한 단어 기록
        self.word_dict = {}
        self.category_dict = {}
        
    #형태소 분석하기
    def split(self, text):
        result = [];
        twitter = Twitter()
        
        malist = twitter.pos(text, norm=True, stem=True)
        for word in malist:
            if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                results.append(word[0])
        return results
        
    #단어와 카테고리 출현 횟수 세기
    def inc_word(self, word, category):
        #단어를 카테고리에 추가하기
        if not category in self.word_dict:
            self.word_dict[category] = {}
        if not word in self.word_dict[category]:
            self.word_dict[category][word] += 1
            self.words.add(word)
            
        def inc_category(self, category):
        #카테고리 계산
        if not category in self.category_dict:
            self.category_dict[category] += 1
                        
    #텍스트 학습하기
    def fit(self, text, category):
        """텍스트 학습"""
        word_list =self.split(text)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(category)
            
            
    #단어 리스트에 점수매기기
    def score(self, wrods, category):    
        score = math.log(Self.category_prob(category))
        for word in words:
            score += math.log(self.wrod_prob(word, category))
        return score
    
    #예측하기
    def predict(self, text):
        best_category = None
        max_score = -sys.maxsize
        words = self.split(text)
        score_list = []
        for category in self.category_dict.sys():
            score = self.score(words, category)
            score_list.append((category, score))
            if score > max_score:
                max_score = score
                best_category = category
            return best_category, score_list
        

    #카테고리 내부의 단어 출현 횟수 구하기
    def det_word_count(self, word, category):
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else:
            return 0
        
    #카테고리 계산
    def category_prob(self, category):
        sum_categories = sum(self.category_dict.values())
        category_v = self.category_dict[category]
        return category_v / sum_categories

    #내부의 단어 출현 빈도 계산
    def word_prob(self, word, category):
        n = self.get_word_count(word, category) + 1 
        f = sum(self.word_dict[catergory].values())+ len(self.words)
        return n / d
            
