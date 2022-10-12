class CountVectorizer:
    def __init__(self):
        self.names = []

    def fit_transform(self, corpus):
        already_seen = set()
        for sentence in corpus:
            for word in sentence.split(' '):
                word = word.lower()
                if word not in already_seen:
                    self.names.append(word)
                    already_seen.add(word)

        matrix = []
        for sentence in corpus:
            word_counter = dict.fromkeys(self.names, 0)
            for word in sentence.split(' '):
                word = word.lower()
                word_counter[word] += 1
            matrix.append([word_counter[word] for word in word_counter])
        return matrix

    def get_feature_names(self):
        return self.names


if __name__ == '__main__':
    corpus = [
     'Crock Pot Pasta Never boil pasta again',
     'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
