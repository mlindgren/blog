Title: Switching to Pelican
Date: 2015-10-12
Category: Technology
Slug: switching-to-pelican
Tags: Meta, Python, Projects

I keep forgetting to mention it, but this May was the fifth anniversary of
this blog. Thus, it's time again for some housekeeping.
[Three years ago](/entry/2012/09/23/switching-to-octopress/) I stopped using
Wordpress for my blog and moved it to [Octopress](http://octopress.org).
Octopress is a great blogging framework, but its current incarnation
[has some major shortcomings](http://octopress.org/2015/01/15/octopress-3.0-is-coming/).
Those will be fixed with Octopress 3.0, but 3.0 has been a long time coming, and
due to the changing distribution model the work to move from 2.0 to 3.0 may be
substantial. Plus, Octopress isn't the best fit for me because it's written in
Ruby, which I don't know and don't have much interest in learning; I much prefer
Python.

I recently learned of [Pelican](http://getpelican.com), which is a
Python-based blogging tool. Luckily, Maurizio Sambati has already done the hard
work of
[porting the Octopress theme to Pelican](https://github.com/duilio/pelican-octopress-theme).
Since my blog's theme is the Octopress theme with a few tweaks, it wasn't an
inordinate amount of work to
[port my own theme to Pelican](https://github.com/mlindgren/mlindgren-pelican-theme).
Jake Vanderplas also did some great work in
[porting some of Octopress' Liquid tags](https://github.com/getpelican/pelican-plugins/pull/21)
to Pelican, and he also has
[a great blog post](https://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/)
which walks through the process (and describes some of his reasons for
switching, which mirror my own). In the end, it did take me several hours of
work to move everything over and clean up some of the posts where I was making
use of various Octopress plug-ins, but I think it will be a boon in the long
run. (Please let me know if anything appears to be broken, as it's possible that
I missed something.)

In addition to being easier for me to use and contribute to, I'm really excited
about Pelican's support for tags. Tagging will help organize my blog,
especially since I've limited myself to having only a few categories since I'm
committed to having a unique, easily-distinguishable color for each one. I'm
also excited that Pelican has built-in support for
[translating articles](http://docs.getpelican.com/en/3.6.3/content.html#translations),
which I plan to take advantage of to practice the languages I'm learning.

Check back in three years to see which new blogging platform I switch to next!
