Title: Group Meeting
date: 2013-05-22 23:33
comments: true
Tags: group meeting, science, python
slug: group-meeting

A few weeks ago, I gave the Pande Group meeting. The slides are on [github](https://github.com/rmcgibbo/group_meeting_april22),
and you can view them [here](http://htmlpreview.github.io/?http://github.com/rmcgibbo/group_meeting_april22/blob/master/index.html).
The title of the talk is *Protein Folding is Easy: Towards Markov State Models
for Conformational Change*, and mostly addresses my learning distance metrics
for kinetic clustering of protein conformations from molecular dynamics
simulations. The central challenge here is detecting structurally subtle but
slow conformational changes in a dataset that might contain massive structural
changes, like folding. Simply clustering at a tiny radius with a standard distance
metric (RMSD) is fine in theory, but fails in practice to deal with the bias-variance
tradeoff effectively.

The slides are written in pure markdown and rendered to HTML5 using an adapted
version of the google-io-2012 HTML5 slide deck. The slide deck is now a little
python package, hosted on [github](https://github.com/rmcgibbo/slidedeck). After
installing it (`python setup.py install`), just run `slidedeck create` to get
started with a new template deck, and `slidedeck render` to make some HTML5.
