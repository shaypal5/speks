#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This code implements a basic, Twitter-aware tokenizer.

A tokenizer is a function that splits a string of text into words. In
Python terms, we map string and unicode objects into lists of unicode
objects.

There is not a single right way to do tokenizing. The best method
depends on the application.  This tokenizer is designed to be flexible
and this easy to adapt to new domains and tasks.  The basic logic is
this:

1. The tuple regex_strings defines a list of regular expression
   strings.

2. The regex_strings strings are put, in order, into a compiled
   regular expression object called word_re.

3. The tokenization is done by word_re.findall(s), where s is the
   user-supplied string, inside the tokenize() method of the class
   Tokenizer.

4. When instantiating Tokenizer objects, there is a single option:
   preserve_case.  By default, it is set to True. If it is set to
   False, then the tokenizer will downcase everything except for
   emoticons.

The __main__ method illustrates by tokenizing a few examples.

I've also included a Tokenizer method tokenize_random_tweet(). If the
twitter library is installed (http://code.google.com/p/python-twitter/)
and Twitter is cooperating, then it should tokenize a random
English-language tweet.
"""

__author__ = "Christopher Potts"
__copyright__ = "Copyright 2011, Christopher Potts"
__credits__ = []
__license__ = """Creative Commons Attribution-NonCommercial-ShareAlike 3.0
Unported License: http://creativecommons.org/licenses/by-nc-sa/3.0/"""
__version__ = "1.0"
__maintainer__ = "Christopher Potts"
__email__ = "See the author's website"

######################################################################

import re
import html


def lmap(f, xs):
    return list(map(f, xs))
######################################################################
# The following strings are components in the regular expression
# that is used for tokenizing. It's important that phone_number
# appears first in the final regex (since it can contain whitespace).
# It also could matter that tags comes after emoticons, due to the
# possibility of having text like
#
#     <:| and some text >:)
#
# Most imporatantly, the final element should always be last, since it
# does a last ditch whitespace-based tokenization of whatever is left.

# This particular element is used in a couple ways, so we define it
# with a name:


emoticon_string = r"""
    (?:
      [<>]?
      [:;=8]                     # eyes
      [\-o\*\']?                 # optional nose
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
      |
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
      [\-o\*\']?                 # optional nose
      [:;=8]                     # eyes
      [<>]?
    )"""

# The components of the tokenizer:
regex_strings = (
    # Phone numbers:
    r"""
    (?:
      (?:            # (international)
        \+?[01]
        [\-\s.]*
      )?
      (?:            # (area code)
        [\(]?
        \d{3}
        [\-\s.\)]*
      )?
      \d{3}          # exchange
      [\-\s.]*
      \d{4}          # base
    )""",
    # Emoticons:
    emoticon_string,
    # HTML tags:
    r"""<[^>]+>""",
    # Twitter username:
    r"""(?:@[\w_]+)""",
    # Twitter hashtags:
    r"""(?:\#+[\w_]+[\w\'_\-]*[\w_]+)""",
    # Remaining word types:
    r"""
    (?:[a-z][a-z'\-_]+[a-z])       # Words with apostrophes or dashes.
    |
    (?:[+\-]?\d+[,/.:-]\d+[+\-]?)  # Numbers, including fractions, decimals.
    |
    (?:[\w_]+)                     # Words without apostrophes or dashes.
    |
    (?:\.(?:\s*\.){1,})            # Ellipsis dots.
    |
    (?:\S)                         # Everything else that isn't whitespace.
    """
)

######################################################################
# This is the core tokenizing regex:

joined_regex_str = r"""(%s)""" % "|".join(regex_strings)
word_re = re.compile(joined_regex_str, re.VERBOSE | re.I | re.UNICODE)

# The emoticon string gets its own regex so that we can preserve case
# for them as needed:
emoticon_re = re.compile(regex_strings[1], re.VERBOSE | re.I | re.UNICODE)

# These are for regularizing HTML entities to Unicode:
html_entity_digit_re = re.compile(r"&#\d+;")
html_entity_alpha_re = re.compile(r"&\w+;")
amp = "&amp;"

######################################################################


def tokenize_no_case_preserving(s):
    """Tokenizes the given string without preserving letter case.

    Parameters
    ----------
    s : str or unicode object
        The string to tokenize.

    Returns
    -------
    list
        A tokenized list of strings; conatenating this list returns the
        original string (except for letter case).
    """
    # Try to ensure unicode:
    # try:
    #   s = str(s,'utf-8')
    # except UnicodeDecodeError:
    #   s = str(s).encode('string_escape')
    #   s = str(s,'utf-8')
    # Fix HTML character entitites:
    s = _html2unicode(s)
    # Tokenize:
    words = word_re.findall(s)
    # Possible alter the case, but avoid changing emoticons like :D into :d:
    words = lmap((lambda x: x if emoticon_re.search(x) else x.lower()), words)
    return words


def _html2unicode(s):
    """Replace HTML entities in a string with corresponding unicode characters.

    An internal metod that seeks to replace all the HTML entities in
    s with their corresponding unicode characters.
    """
    # First the digits:
    ents = set(html_entity_digit_re.findall(s))
    if len(ents) > 0:
        for ent in ents:
            entnum = ent[2:-1]
            try:
                entnum = int(entnum)
                s = s.replace(ent, chr(entnum))
            except Exception:
                pass
    # Now the alpha versions:
    ents = set(html_entity_alpha_re.findall(s))
    ents = filter((lambda x: x != amp), ents)
    for ent in ents:
        entname = ent[1:-1]
        try:
            s = s.replace(ent, chr(html.entities.name2codepoint[entname]))
        except Exception:
            pass
        s = s.replace(amp, " and ")
    return s
