from sentence_transformers import SentenceTransformer, util
import tensorflow
import sklearn
import pandas
import torch
import numpy
import nltk
import re


# Process keywords
class WordEmbedding_Transformer(sklearn.base.BaseEstimator,
                                sklearn.base.TransformerMixin):
    """download all-MiniLM-L6-v2"""
    def __init__(self, pre_train_model: str):
        super().__init__()

        self.pre_train_model = pre_train_model
        self.model_ = SentenceTransformer(self.pre_train_model)

    def fit(self, X: numpy.array, y: numpy.array = None):
        return self

    def transform(self, X: numpy.array) -> tensorflow.Tensor:
        X = self.model_.encode(X, convert_to_tensor=True)
        return X


class WordEmbedding_Comparing(sklearn.base.BaseEstimator,
                              sklearn.base.TransformerMixin):
    def __init__(self, corpus: str):
        super().__init__()
        self.corpus = corpus

    def fit(self, X: numpy.array, y: numpy.array = None):
        return self

    def transform(self, X: numpy.array) -> tensorflow.Tensor:
        cosine_score = util.pytorch_cos_sim(X, self.corpus)[0]
        N_top_results = torch.topk(cosine_score, k=5)
        return N_top_results


class Top_Results(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    def __init__(self):
        super().__init__()
        self.top_n = []

    def fit(self, X: numpy.array, y: numpy.array = None):
        return self

    def transform(self, X: numpy.array):
        for score, idx in zip(X[0], X[1]):
            score = score.cpu().data.numpy()
            idx = self.top_n.append(idx.cpu().data.numpy())

        return self.top_n


# Process keywords
class extract_keywords_keybert(sklearn.base.BaseEstimator,
                               sklearn.base.TransformerMixin):
    """KeyBERT Must be imported, as dependence"""
    def __init__(self, variable: list, extractor):
        super().__init__()

        if not isinstance(variable, list):
            raise ValueError("feature must be a list")

        self.variable = variable
        self.key_extractor = extractor
        self.all_key_words = []

    def fit(self, X: pandas.DataFrame, y: pandas.Series = None):
        return self

    def transform(self, X: pandas.DataFrame) -> pandas.DataFrame:
        def extracting_keywords(row: str) -> list:
            """Initiate tranformer , extract keywords into a list"""

            keywords_ = (self.key_extractor.extract_keywords(
                docs=row,
                keyphrase_ngram_range=(1, 2),
                stop_words='english',
                top_n=3,
                use_mmr=True,
                diversity=.6))

            keywords_ = [word[0] for word in keywords_]
            return keywords_

        # create a copy
        X = X.copy()

        for col in self.variable:
            X[col +
              str("_t")] = X[col].apply(lambda row: extracting_keywords(row))

        return X
