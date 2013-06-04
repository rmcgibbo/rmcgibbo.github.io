title: What is the uncertainty in an MSM?
date: 2013-05-26 14:23
comments: true
tags: msmbuilder, science
slug: what-is-the-uncertainty-in-an-msm

Two major sources of error characterize a Markov state model. The first is
the convergence of the dataset -- we can only model the processes that we've
simulated, in some form or another. When the sampling is insufficient, its
not like the MSM can make something out of nothing. This sampling error is
hard to model, because we *don't know* whats out there. The best that we can
do is assess how "densely" sampled the data we've seen is. Do we have
transitions that we've only seen once? If we split the dataset in half, are the
halves look consistent with one another?

The second major source of uncertainty is uncertainty in the parameters. These
are the number of clusters, their locations and size, and transition probabilities
between them (also the lag time, but let's leave that aside for now).

To really assess these errors, we need an approach that models them all
explicitly. This is challenging though -- our traditional clustering approaches
are parametric in the number of states, so they don't allow us to naturally
express our uncertainty there. We're going to need to go nonparametric.

Here's the idea: Small peptide (ala2 or ala5). [Dirichlet process gaussian mixture model](http://blog.echen.me/2012/03/20/infinite-mixture-models-with-nonparametric-bayes-and-the-dirichlet-process/)
"clustering" (nonparametric in number of states), with a [Gibbs sampler](http://blog.echen.me/2012/03/20/infinite-mixture-models-with-nonparametric-bayes-and-the-dirichlet-process/)
so that we can sample from the posterior over clusterings. For each
clustering, sample transition matrices with the MCMC engine that Kyle's been
working on. We would have to do the whole thing in probably the projected
backbone dihedral space. It would be nice to use the [von Mises](http://en.wikipedia.org/wiki/Von_Mises_distribution)
distribution instead of the gaussian to avoid going into the sin/cos space
doubling the number of variable.

I think going nonparameteric in the number of states is pretty key. This
is probably going to be really expensive, and tuning the settings on the
samplers could definitely be a nightmare (now there's a whole separate
convergence issue to worry about), but it would be nice do a careful accounting
for the uncertainties. Other approaches that you might do don't really model
the uncertainty in the clustering parameters.

A simpler approach might be to run a bootstrap on the actual trajectory data.
That's a good option too, but not as elegant. You don't get uncertainty in the
number of states, and there are so many issues with the bootstrap on timeseries.


