# Lab 2025-08-19
 
# You are given a small dataset with 10 short movie reviews.
# Five reviews are positive, five reviews are negative.
# Your task is to build a model that can determine the sentiment of the reviews.

# Bonus 🌟
# Add your own movie reviews to the corpus and see if the model improves.
# Try removing stopwords (by adding stop_words="english" in CountVectorizer).


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import os

corpus = []
pos_dir = './pos'
neg_dir = './neg'

# get positive reviews
for fname in os.listdir(pos_dir):
    fpath = os.path.join(pos_dir, fname)
    if fname.endswith('.txt') and os.path.isfile(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            corpus.append(f.read().strip())

# get negative reviews
for fname in os.listdir(neg_dir):
    fpath = os.path.join(neg_dir, fname)
    if fname.endswith('.txt') and os.path.isfile(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            corpus.append(f.read().strip())


POSITIVE = "Positive"
NEGATIVE = "Negative"


categories = [POSITIVE] * 500 + [NEGATIVE] * 500

# CountVectorizer类会将文本中的词语转换为 词频矩阵. ngram_range：指定要提取的n-gram范围，例如,ngram_range=(1, 2) 将提取单个词和二元词组。
vectorizer = CountVectorizer(ngram_range=(1, 2))

#计算某个词出现的次数
vectors = vectorizer.fit_transform(corpus)

#获取词袋中所有文本关键词
print(vectorizer.get_feature_names_out())

#查看词频结果
print(vectors.toarray())


clf = SVC(kernel='linear')
clf.fit(vectors, categories)

test_corpus = [
    "the movie was great",
    "i hated the film",
    "a boring and bad story",
    "absolutely loved it"
]


test_categories = [POSITIVE, NEGATIVE, NEGATIVE, POSITIVE]

test_x = vectorizer.transform(test_corpus)

print(clf.predict(test_x))
print(clf.score(test_x, test_categories))