"""Lexicon-based gender prediction code."""

from math import sin

from .tokenization import tokenize_no_case_preserving
from .gender_lex import GENDER_LEXICON


def weigh(token, tokens):
    """Calculates the relative weight of the given token.

    Parameters
    ----------
    token : str
        The token to calculate the relative weight for.
    tokens : list of str
        A list of all tokens in the currently examined text.

    Returns
    -------
    float
        The relative weight of the input token in the current text.
    """
    w = GENDER_LEXICON.get(token, 0)
    if w == 0:
        return 0
    else:
        return w * tokens.count(token) / len(tokens)


def predict_gender_by_tweets(text):
    """Predicts a Twitter user gender from his tweets' texts.

    Parameters
    ----------
    text : str
        A text written by the user to predict gender for. Can also be a
        concatenation of several texts by that user.

    Returns
    -------
    int
        1 if the predicted gender is female; 0 if it is male.
    """
    tokens = list(tokenize_no_case_preserving(text))
    weights = sum([weigh(t, tokens) for t in set(tokens)])
    p = sin(-0.06724152 + weights)
    if p >= 0:
        # Female
        return 1
    else:
        # Male
        return 0
