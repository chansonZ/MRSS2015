import sklearn.preprocessing

from HPOlibConfigSpace.configuration_space import ConfigurationSpace
from HPOlibConfigSpace.hyperparameters import CategoricalHyperparameter

from ..preprocessor_base import AutoSklearnPreprocessingAlgorithm


class Imputation(AutoSklearnPreprocessingAlgorithm):
    def __init__(self, strategy, random_state=None):
        # TODO pay attention to the cases when a copy is made (CSR matrices)
        self.strategy = strategy

    def fit(self, X, Y):
        self.preprocessor = sklearn.preprocessing.Imputer(
            strategy=self.strategy, copy=False)
        self.preprocessor.fit(X, Y)
        return self

    def transform(self, X):
        if self.preprocessor is None:
            raise NotImplementedError()
        return self.preprocessor.transform(X)

    @staticmethod
    def get_properties():
        return {'shortname': 'Imputation',
                'name': 'Imputation',
                'handles_missing_values': True,
                'handles_nominal_values': True,
                'handles_numerical_features': True,
                'prefers_data_scaled': False,
                'prefers_data_normalized': False,
                'handles_regression': True,
                'handles_classification': True,
                'handles_multiclass': True,
                'handles_multilabel': True,
                'is_deterministic': True,
                # TODO find out of this is right!
                'handles_sparse': True,
                'handles_dense': True,
                'preferred_dtype': None}

    @staticmethod
    def get_hyperparameter_search_space(dataset_properties=None):
        # TODO add replace by zero!
        strategy = CategoricalHyperparameter(
            "strategy", ["mean", "median", "most_frequent"], default="mean")
        cs = ConfigurationSpace()
        cs.add_hyperparameter(strategy)
        return cs

    def __str__(self):
        name = self.get_properties()['name']
        return "AutoSklearn %" % name
