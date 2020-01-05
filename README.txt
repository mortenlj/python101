Python 101
==========

A 20 minute intro to Python
---------------------------

This is a set of files/slides used to present an introduction to Python at an internal academy session for FINN.no.

The python.png image included here is from http://xkcd.com/353/.

This presentation is written by Morten Lied Johansen, and can be found at https://github.com/mortenlj/python101.
The presentation is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License:
http://creativecommons.org/licenses/by-nc-sa/3.0/

The S5-theme python101 is based on the Scala theme from http://www.netzgesta.de/S5/demos.php, with some modifications.
Additional styling for syntax-highlighting comes from Pygments with some small modifications.

Working with the presentation
-----------------------------

In the `src` directory, there is a `Makefile`, set up to generate the output from the examples, and create a S5-presentation
and a ODP-presentation. This requires the latest version of docutils, Pygments, rst2odp and PIL (See `requirements.txt`).

The ODP-presentation does not work, because of limitations in rst2odp related to scaling/styling of source-code.
