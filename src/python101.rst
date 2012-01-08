==========
Python 101
==========

.. footer:: http://bitbucket.org/mortenlj/python101

.. figure:: python.png
    :align: center
    :alt: http://xkcd.com/353/

.. epigraph::

    I wrote 20 short programs in Python yesterday.  It was wonderful.  Perl, I'm leaving you.

    -- Randall Munroe

Hello World
===========

.. topic:: Code

    .. include:: code/hello.py
        :code: python

.. topic:: Output

    .. include:: code/hello.out
        :code:

Numbers
=======

.. topic:: Code

    .. include:: code/numbers.py
        :code: python

.. topic:: Output

    .. include:: code/numbers.out
        :code:


Strings and formatting
======================

.. topic:: Code

    .. include:: code/text.py
        :code: python

.. topic:: Output

    .. include:: code/text.out
        :code:

Built-in datatypes (dict)
=========================

.. topic:: Code

    .. include:: code/data_dict.py
        :code: python

.. topic:: Output

    .. include:: code/data_dict.out
        :code:

Built-in datatypes (list and tuple)
===================================

.. topic:: Code

    .. include:: code/data_list_tuple.py
        :code: python

.. topic:: Output

    .. include:: code/data_list_tuple.out
        :code:

Built-in datatypes (set)
========================

.. topic:: Code

    .. include:: code/data_set.py
        :code: python

.. topic:: Output

    .. include:: code/data_set.out
        :code:

Control structures (if)
=======================

.. topic:: Code

    .. include:: code/if.py
        :code: python

.. topic:: Output

    .. include:: code/if.out
        :code:

Control structures (for)
========================

.. topic:: Code

    .. include:: code/for.py
        :code: python

.. topic:: Output

    .. include:: code/for.out
        :code:


Control structures (while)
==========================

.. topic:: Code

    .. include:: code/while.py
        :code: python

.. topic:: Output

    .. include:: code/while.out
        :code:

.. topic:: notes
    :class: hidden print

    - It's possible to add an `else`-clause to this, similar to the `for`-loop


Control structures (try)
========================

.. topic:: Code

    .. include:: code/try.py
        :code: python

.. topic:: Output

    .. include:: code/try.out
        :code:

Functions
=========

.. topic:: Code

    .. include:: code/func1.py
        :code: python

.. topic:: Output

    .. include:: code/func1.out
        :code:

Functions (2)
=============

.. topic:: Code

    .. include:: code/func2.py
        :code: python

.. topic:: Output

    .. include:: code/func2.out
        :code:


Classes
=======

.. topic:: Code

    .. include:: code/classes.py
        :code: python

.. topic:: Output

    .. include:: code/classes.out
        :code:

Generators
==========

.. topic:: Code

    .. include:: code/generator.py
        :code: python

.. topic:: Output

    .. include:: code/generator.out
        :code:

Generators (2)
==============

.. topic:: Code

    .. include:: code/generator2.py
        :code: python

.. topic:: Output

    .. include:: code/generator2.out
        :code:

List-comprehensions
===================

.. topic:: Code

    .. include:: code/comprehensions.py
        :code: python

.. topic:: Output

    .. include:: code/comprehensions.out
        :code:

New functions on the fly
========================

.. topic:: Code

    .. include:: code/new_func.py
        :code: python

.. topic:: Output

    .. include:: code/new_func.out
        :code:

Decorators
==========

.. topic:: Code

    .. include:: code/decorator.py
        :code: python

.. topic:: Output

    .. include:: code/decorator.out
        :code:


Descriptors
===========

.. topic:: Code

    .. include:: code/descriptors.py
        :code: python

.. topic:: Output

    .. include:: code/descriptors.out
        :code:

New types on the fly
====================

.. topic:: Code

    .. include:: code/new_type.py
        :code: python

.. topic:: Output

    .. include:: code/new_type.out
        :code:

Modules and packages
====================

.. topic:: Code

    .. include:: code/import_modules.py
        :code: python

.. topic:: Output

    .. include:: code/import_modules.out
        :code:

The standard library
====================

    "Batteries included"

- String Services: regex, diff, wrapping, charset encoding etc.
- Data Types: dates and calendars, collections, weakrefs, deepcopy utils, pretty printing
- Numeric and Mathematical Modules: math functions, rational numbers, random, operators
- File and Directory Access: filepath abstractions, file compare, tempfile, glob, shell-like utilities
- Data Persistence: several serialization protocols, sqlite-database, DBM-databases
- Data Compression and Archiving: zlib, gzip, bzip2, zip and tar
- File Formats: CSV, ini-style, XDR
- Cryptographic Services: MD5, SHA1, SHA224, SHA256, SHA384 and more
- Operating System Services: streams, time, argument parsing, logging, OS abstractions and more
- More Operating System Services: IO select, threading, multiprocessing, memory mapped files, readline
- Interprocess Communication and Networking: subprocesses, socket, ssl and more
- Internet Data Handling: Parsing email and MIME, json, mailboxes, base64, quoted-printable, uuencode
- Structured Markup Processing Tools: HTMLParser, XML-parsers (dom, sax and etree)
- Internet Protocols and Support: CGI, URL utils, FTP, POP, IMAP, NNTP, SMTP, telnet, XML-RPC with servers
- ... Tk GUI modules, unittesting, debugger, profilers, build-tools, reflection and introspection utils
- ... Import hooks, tokenizer, Python compiler, disassembler, documention generator and lots more!

The Zen of Python
=================

.. topic:: Code

    .. include:: code/zen.py
        :code: python

.. topic:: Output

    .. include:: code/zen.out
        :code:

Interesting applications using Python
=====================================

- Two out of three popular distributed version control systems are written in Python (Bazaar and Mercurial)
- The original BitTorrent client
- Calibre, an open source e-book management tool
- Dropbox, a web-based file hosting service
- GNU Mailman, one of the more popular packages for running email mailing lists
- Civilization IV and V uses Python for most of its internal scripting
- Battlefield 2 uses Python for all of its addons and a lot of its functionality
- Eve Online uses Stackless Python, both its server and client side applications
- World of Tanks uses Python for most of its tasks
- WingIDE, a Python IDE written in Python

Other notable mentions of Python
================================

- Linux Journal Readers choice award three years running
- reddit was originally written in Common Lisp, but was rewritten in Python in 2005
- YouTube uses Python "to produce maintainable features in record times, with a minimum of developers"
- Google App Engine launched with only Python support, Java came later
- Google uses Python for many tasks including the backends of web apps such as Google Groups, Gmail, and Google Maps, as well as for some of its search-engine internals
- NASA is using Python to implement a CAD/CAE/PDM repository and model management, integration, and transformation system which will be the core infrastructure for its next-generation collaborative engineering environment

Where to go from here
=====================

This presentation
    http://bitbucket.org/mortenlj/python101
Python website
    http://www.python.org
Dive Into Python 3
    http://www.diveintopython3.net
