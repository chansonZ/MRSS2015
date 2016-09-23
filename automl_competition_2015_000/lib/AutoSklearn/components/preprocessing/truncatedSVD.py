import sklearn.decomposition

from HPOlibConfigSpace.configuration_space import ConfigurationSpace
from HPOlibConfigSpace.hyperparameters import UniformIntegerHyperparameter

from ..preprocessor_base import AutoSklearnPreprocessingAlgorithm
import numpy as np



class TruncatedSVD(AutoSklearnPreprocessingAlgorithm):
    def __init__(self, target_dim, random_state=None):
        self.target_dim = int(target_dim)
        self.random_state = random_state
        self.preprocessor = None

    def fit(self, X, Y):
        target_dim = min(self.target_dim, X.shape[0])
        self.preprocessor = sklearn.decomposition.TruncatedSVD(
            target_dim, algorithm='arpack')
        self.preprocessor.fit(X, Y)

        return self

    def transform(self, X):
        if self.preprocessor is None:
            raise NotImplementedError()
        return self.preprocessor.transform(X)

    @staticmethod
    def get_properties():
        return {'shortname': 'TSVD',
                'name': 'Truncated Singular Value Decomposition',
                'handles_missing_values': False,
                'handles_nominal_values': False,
                'handles_numerical_features': True,
                'prefers_data_scaled': False,
                'prefers_data_normalized': False,
                'handles_regression': True,
                'handles_classification': True,
                'handles_multiclass': True,
                'handles_multilabel': True,
                'is_deterministic': True,
                'handles_sparse': True,
                'handles_dense': False,
                'preferred_dtype': np.float32}

    @staticmethod
    def get_hyperparameter_search_space(dataset_properties=None):
        target_dim = UniformIntegerHyperparameter(
            "target_dim", 10, 256, default=128)
        cs = ConfigurationSpace()
        cs.add_hyperparameter(target_dim)
        return cs

    def __str__(self):
        name = self.get_properties()['name']
        return "AutoSklearn %" % name
