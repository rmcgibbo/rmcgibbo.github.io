title: Projects in the Pipeline
date: 2013-05-23 00:32
comments: true
summary: A few of the projects on my mind right now. Some are father along than others.
tags: msmbuilder, science
slug: projects-in-the-pipeline


A few of the projects on my mind right now. Some are father along than others.

- Accelerated conformation clustering with RMSD using a kmeans-like algorithm.
  The key to kmeans is that you can take the average of a set of data points
  under an $L_p$ norm by just... taking their average. But that doesn't work
  for RMSD, because alignment isn't transitive. I'm working on some ways to do
  that averaging, and I think I can accelerate RMSD clustering compared to
  k-medoids. The procedure works well for a small number of atoms, but needs
  some tweaks -- I think a better weighting -- when there are more atoms (or
  the dynamic range of distances is greater).
- MSMAccelerator2: Last month, I refactored the MSMAccelerator code base. Well,
  actually I ripped all of the old code out and started from the ground up. The
  new code has a message massing architecture with ZeroMQ, and has a little
  server that looks like a mini version of the FAH workserver. Now, this code
  needs to get some exercise. I've started folding some small proteins, and
  we need to analyze the convergence. I think we're going to see an impressive
  speedup.
- GBVI: We need to push on this. Currently, not a lot has been done.
- Optimal-K: At this point, the framework for choosing the optimal number of
  states, at least under euclidean metrics, is low hanging fruit. Getting this
  finished and out the door is academic priority number 1.
  


