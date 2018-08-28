"""Test gender prediction for the speks package."""

from speks import predict_gender_by_tweets


USER1 = [
    "We need more prominent women in physics.",
    "Motherhood is amazing!",
    "I went shopping today.",
    "queen beyonce",
]

USER2 = [
    "dude, i'm going to kick your ass!!!",
    "screw you, bitch",
    "omg played my PS4 all day today sup?",
    "I fucking love 4chan",
]


def test_prediction():
    prediction1 = predict_gender_by_tweets(" ".join(USER1))
    assert prediction1 == 1

    prediction2 = predict_gender_by_tweets(" ".join(USER2))
    assert prediction2 == 0
