# Lab 2025-08-19
 
# You are given a small dataset with 10 short movie reviews.
# Five reviews are positive, five reviews are negative.
# Your task is to build a model that can determine the sentiment of the reviews.

# Bonus 🌟
# Add your own movie reviews to the corpus and see if the model improves.
# Try removing stopwords (by adding stop_words="english" in CountVectorizer).


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

corpus = [
    "the movie was fantastic and i loved every part of it, the movie",
    "an absolute masterpiece with brilliant acting",
    "the film was boring and too long",
    "i really enjoyed the story and the visuals",
    "the plot was terrible and the acting was even worse",
    "what a wonderful experience, highly recommend",
    "not worth my time, very disappointing",
    "a truly great film, i will watch it again",
    "the script was weak and the characters were flat",
    "an amazing journey from start to finish"
]

POSITIVE = "Positive"
NEGATIVE = "Negative"

categories = [
    POSITIVE, POSITIVE, NEGATIVE, POSITIVE, NEGATIVE,
    POSITIVE, NEGATIVE, POSITIVE, NEGATIVE, POSITIVE
]

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