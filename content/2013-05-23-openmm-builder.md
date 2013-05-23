Title: OpenMM Script Builder
date: 2013-05-23 00:08
comments: true
Tags: web, science
slug: openmm-builder

[Build](http://builder.openmm.org) custom OpenMM scripts right in the browser!
[OpenMM](http://openmm.org/) is one of the most flexible molecular dynamics
packages, put it can be a little intimidating for the new user. Instead of
interacting with it via a set of command line scripts, as one would with
amber or gromacs, to interact with OpenMM you write a little python script.
If you've never written a script before, this might seem a little unfamiliar,
but it's an incredibly powerful paradigm.

But to help you out, I've written a little [web application](http://builder.openmm.org)
that'll build an OpenMM python script for you. As you select the options via
the menus, the script will be "written" for you, live. The code is
live on heroku, at [builder.openmm.org](http://builder.openmm.org), and free (GPL)
on [github](https://github.com/rmcgibbo/openmm-webbuilder). Fork away.

It would be really awesome if the webapp had a "run" button that would run
your simulation for a short period of time on a donated GPU, but that's
going to a little nontrivial, especially with the security ramifications. Pull
requests welcome!