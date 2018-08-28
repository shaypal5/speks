from .gender_predictor import (  # noqa: F401
    predict_gender_by_tweets,
)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
