"""Testing tokenization for the speks package."""

from speks.tokenization import tokenize_no_case_preserving


EX1 = u"RT @ #happyfuncoding: this is a typical Twitter tweet :-)"
EX2 = u"""HTML entities &amp; other Web oddities can be an &aacute;cute
      <em class='grumpy'>pain</em> >:("""
EX3 = u"""It's perhaps noteworthy that phone numbers like +1 (800) 123-4567,
      (800) 123-4567, and 123-4567 are treated as words despite their
      whitespace."""
EX4 = u"&#5; birds just attacked me!"  # HTML digit characters


def test_tokenization():
    tokens1 = tokenize_no_case_preserving(EX1)
    print(tokens1)
    assert len(tokens1) == 11
    assert tokens1[0] == 'rt'
    assert tokens1[1] == '@'
    assert tokens1[3] == ':'
    assert tokens1[10] == ':-)'

    tokens2 = tokenize_no_case_preserving(EX2)
    print(tokens2)
    assert len(tokens2) == 14
    assert tokens2[2] == 'and'
    assert tokens2[9] == 'ácute'

    tokens3 = tokenize_no_case_preserving(EX3)
    print(tokens3)
    assert len(tokens3) == 21

    tokens4 = tokenize_no_case_preserving(EX4)
    print(tokens4)
    assert len(tokens4) == 6
