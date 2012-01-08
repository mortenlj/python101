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

.. topic:: Notes
    :class: handout

    - Python is an interpreted language, with strong dynamic typing
    - Noted for clear, readable syntax
    - Object-oriented, but supports procedural and functional styles aswell
    - Runs "everywhere"

Hello World
===========

.. topic:: Code

    .. include:: code/hello.py
        :code: python

.. topic:: Output

    .. include:: code/hello.out
        :code:

.. topic:: Notes
    :class: handout

    - Shebang-line at the top
    - Coding line. Optional, but if not present code is assumed to be ASCII

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

Strings and formatting (2)
==========================

.. topic:: Code

    .. include:: code/text2.py
        :code: python

.. topic:: Output

    .. include:: code/text2.out
        :code:

Built-in datatypes (dict)
=========================

.. topic:: Code

    .. include:: code/data_dict.py
        :code: python

.. topic:: Output

    .. include:: code/data_dict.out
        :code:

.. topic:: Notes
    :class: handout

    - Looks a lot like JSON
    - Output is the "repr" of a dict, which for all built-in types can be `eval`-ed back to the original object
    - Used extensively internally in the language and highly optimized

Built-in datatypes (list and tuple)
===================================

.. topic:: Code

    .. include:: code/data_list_tuple.py
        :code: python

.. topic:: Output

    .. include:: code/data_list_tuple.out
        :code:

.. topic:: Notes
    :class: handout

    - List have methods allowing it to be used as a queue, stack, or a plain list

Built-in datatypes (set)
========================

.. topic:: Code

    .. include:: code/data_set.py
        :code: python

.. topic:: Output

    .. include:: code/data_set.out
        :code:

.. topic:: Notes
    :class: handout

    - Supports all common set-operations with syntax and methods

Control structures (if)
=======================

.. topic:: Code

    .. include:: code/if.py
        :code: python

.. topic:: Output

    .. include:: code/if.out
        :code:

.. topic:: Notes
    :class: handout

    - Indentation is *significant*
    - All code-blocks start with a `:`, and uses indentation to delineate the block
    - Python has no `switch`-statement. Use either if-elif-else like here, or a dispatching dict

Control structures (for)
========================

.. topic:: Code

    .. include:: code/for.py
        :code: python

.. topic:: Output

    .. include:: code/for.out
        :code:

.. topic:: Notes
    :class: handout

    - For is a for-each loop. The typical C/Pascal-style loop can be emulated with `range`
    - `else` is executed when the loop finishes normally (not using `break`)
    - Can iterate over anything that supports the iterator protocol

Control structures (while)
==========================

.. topic:: Code

    .. include:: code/while.py
        :code: python

.. topic:: Output

    .. include:: code/while.out
        :code:

.. topic:: Notes
    :class: handout

    - It's possible to add an `else`-clause to this, similar to the `for`-loop
    - There is no do-while

Control structures (try)
========================

.. topic:: Code

    .. include:: code/try.py
        :code: python

.. topic:: Output

    .. include:: code/try.out
        :code:

.. topic:: Notes
    :class: handout

    - Can have multiple `except`-blocks
    - Can mix `except` and `finally`

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

.. topic:: Notes
    :class: handout

    - Note that the syntax for a class method is the same as for a function
    - Explicit self
    - Explicit self allows taking a function and attaching it to a class after the fact

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

.. topic:: Notes
    :class: handout

    - List-comprehensions can be nested
    - Beware: Too much usage harms readability!

New functions on the fly
========================

.. topic:: Code

    .. include:: code/new_func.py
        :code: python

.. topic:: Output

    .. include:: code/new_func.out
        :code:

.. topic:: Notes
    :class: handout

    - Note the fact that we can use a function just like any other variable

Decorators
==========

.. topic:: Code

    .. include:: code/decorator.py
        :code: python

.. topic:: Output

    .. include:: code/decorator.out
        :code:

.. topic:: Notes
    :class: handout

    - This is where it gets tricky...
    - We define a function that takes a function as an argument,
      and returns a new function that calls the function that was passed in
    - @-notation is just syntactic sugar, can be done "manually" as demonstrated

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

.. topic:: Notes
    :class: handout

    - Build a domain-model on the fly, based on parsed input
    - Create types from configuration

Modules and packages
====================

.. topic:: Code

    .. include:: code/import_modules.py
        :code: python

.. topic:: Output

    .. include:: code/import_modules.out
        :code:

.. topic:: Notes
    :class: handout

    - `dir` is a built-in function that returns a list of all attributes of an object
    - `pprint` pretty-prints the object
    - Imports search the `PYTHONPATH` for modules and packages with the given name

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

.. topic:: Notes
    :class: handout

    - This is a shortened list of the available modules and packages in the standard library
    - No need to read it all, just look at the docs later on

The Zen of Python
=================

.. topic:: Code

    .. include:: code/zen.py
        :code: python

.. topic:: Output

    .. include:: code/zen.out
        :code:

.. topic:: Notes
    :class: handout

    - The `this`-module is included as an easter egg
    - Describes the essence of what many consider "pythonic" code
    - Note especially:
        - Explicit is better than implicit (ref. explicit self)
        - Readability counts
        - There should be one... (compare Perl: "There's more than one way to do it")
        - ...refuse the temptation to guess

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

Dive Into Python 3 (Free online book)
    http://www.diveintopython3.net
