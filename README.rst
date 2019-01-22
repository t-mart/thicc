thicc
#####

Convert characters to their fullwidth representation

Usage Examples
==============

Pipe in text from standard input:

.. code-block:: bash
    $ echo "foo" | thc

.. code-block:: bash
    ｆｏｏ

Pass a filename argument:

.. code-block:: bash
    $ thc thatfile

.. code-block:: bash
    ｂａｒ

Reverse fullwidth text:

.. code-block:: bash
    $ thc -r <<<ｂａｚ

`<<<` is not special thicc syntax. It is a shell "herestring". It is one of many ways to pass standard input to a
program on your shell.

.. code-block:: bash
    baz

Installation
============

.. code-block:: bash
    $ pip install --upgrade thicc
