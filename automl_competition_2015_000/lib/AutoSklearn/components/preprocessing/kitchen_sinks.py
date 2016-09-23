import sklearn.kernel_approximation

from HPOlibConfigSpace.configuration_space import ConfigurationSpace
from HPOlibConfigSpace.hyperparameters import UniformFloatHyperparameter, \
    UniformIntegerHyperparameter

from ..preprocessor_base import AutoSklearnPreprocessingAlgorithm

class RandomKitchenSinks(AutoSklearnPreprocessingAlgorithm):

    def __init__(self, gamma, n_components, random_state = None):
        """ Parameters:
        gamma: float
               Parameter of the rbf kernel to be approximated exp(-gamma * x^2)

        n_components: int 
               Number of components (output dimensionality) used to approximate the kernel
        """
        self.gamma = gamma
        self.n_components = n_components
        self.random_state = random_state

    def fit(self, X, Y):
        self.preprocessor = sklearn.kernel_approximation.RBFSampler(self.gamma, self.n_components, self.random_state)
        self.preprocessor.fit(X, Y)
        return self
    
    def transform(self, X):
        if self.preprocessor is None:
            raise NotImplementedError()
        return self.preprocessor.transform(X)

    @staticmethod
    def get_properties():
        return {'shortname': 'KitchenSink',
                'name': 'Random Kitchen Sinks',
                'handles_missing_values': False,
                'handles_nominal_values': False,
                'handles_numerical_features': True,
                'prefers_data_scaled': True,
                'prefers_data_normalized': True,
                'handles_regression': True,
                'handles_classification': True,
                'handles_multiclass': True,
                'handles_multilabel': True,
                'is_deterministic': True,
                'handles_sparse': True,
                'handles_dense': True,
                'preferred_dtype': None}

    @staticmethod
    def get_hyperparameter_search_space(dataset_properties=None):
        gamma = UniformFloatHyperparameter(
            "gamma", 0.3, 2., default=1.0)
        n_components = UniformIntegerHyperparameter(
            "n_components", 50, 10000, default=100, log=True)
        cs = ConfigurationSpace()
        cs.add_hyperparameter(gamma)
        cs.add_hyperparameter(n_components)
        return cs

    def __str__(self):
        name = self.get_properties()['name']
        return "AutoSklearn %" % name

