speks
#####
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

A Python 3, packaged version of the `TwitterGenderPredictor code by JT Wolohan <https://github.com/jtwool/TwitterGenderPredictor>`_, which itself is a Python 2 implementation of Sap et al.'s gender prediction algorithm for Twitter. SPEKS stands for Sap, Park, Eichstaedt, Kern and Stilwell, the first five writers of the `paper describing the algorithm <http://wwbp.org/papers/emnlp2014_developingLexica.pdf>`_ implemented here. 

.. code-block:: python

  >>> from speks import predict_gender_by_tweets
  >>> gender = predict_gender_by_tweets(" ".join(["Please Do.", "Join me in praying!"]))


.. contents::

.. section-numbering::


Features
========

* Supports Python 3.
* ``pip``-installable.
* Fully tested.


Installation
============

.. code-block:: bash

  pip install speks
  

Use
===

This is a Python 3, packaged version of the `TwitterGenderPredictor code by JT Wolohan <https://github.com/jtwool/TwitterGenderPredictor>`_, which itself is a Python 2 implementation of Sap et al.'s gender prediction algorithm for Twitter. According to Wolohan, the algorithm should be 90% accurate given a large sample of users and a reasonable amount of data for each user.


You can have the package predict the gender of a Twitter user by providing the ``predict_gender_by_tweets`` function with a string containing tweets contents.

.. code-block:: python

  >>> from speks import predict_gender_by_tweets
  >>> gender = predict_gender_by_tweets(" ".join(["No touchy", "Trial by fire"]))


Licensing
=========

Most of the code was released by `JT Wolohan`_ under the `MPL 2.0 license <https://www.mozilla.org/en-US/MPL/2.0/>`_, and thus I'm releasing my additions under the same license. However, the tokenization code - although slightly adapted - was originally written by `Christopher Potts`_ and released by him under the `CC BY-NC-SA 3.0 license <https://creativecommons.org/licenses/by-nc-sa/3.0/>`_, and thus remains released under that license.


Contributing
============

Current package maintainer and author is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/speks.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd speks
  pip install -e '.[test]'



Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd speks
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


Credits
=======

Algorithm by `Sap et al <http://wwbp.org/papers/emnlp2014_developingLexica.pdf>`_. Original code by `JT Wolohan`_, with tokenization code by `Christopher Potts`_. Packaging and Python 3 adaptation by `Shay Palachy <shaypalachy.com>`_.

Original paper reference:
*Sap, M., Park, G., Eichstaedt, J., Kern, M., Stillwell, D., Kosinski, M., ... & Schwartz, H. A. (2014). Developing age and gender predictive lexica over social media. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) (pp. 1146-1151).*


.. _`JT Wolohan`: https://github.com/jtwool 
.. _`Christopher Potts`: https://web.stanford.edu/~cgpotts/


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/speks.svg
  :target: https://pypi.org/project/speks

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/speks.svg
   :target: https://pypi.org/project/speks

.. |Build-Status| image:: https://travis-ci.org/shaypal5/speks.svg?branch=master
  :target: https://travis-ci.org/shaypal5/speks

.. |LICENCE| image:: https://img.shields.io/badge/License-MIT-yellow.svg
  :target: https://pypi.python.org/pypi/pdpipe

.. |Codecov| image:: https://codecov.io/github/shaypal5/speks/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/speks?branch=master
