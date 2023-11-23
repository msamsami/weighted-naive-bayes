from enum import Enum

from ._enum_meta import CaseInsensitiveEnumMeta

__all__ = ["Distribution"]


class Distribution(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """
    Names of probability distributions.
    """

    NORMAL = "Normal"
    LOGNORMAL = "Lognormal"
    EXPONENTIAL = "Exponential"
    UNIFORM = "Uniform"
    PARETO = "Pareto"
    GAMMA = "Gamma"
    BETA = "Beta"
    CHI_SQUARED = "Chi-squared"
    BERNOULLI = "Bernoulli"
    CATEGORICAL = "Categorical"
    GEOMETRIC = "Geometric"
    POISSON = "Poisson"
