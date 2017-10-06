layout: post
Title: Computer Science Career Advice
date: 2017-10-05
Category: Coding
Slug: software-development-career-advice
Tags: Personal, Computer Science

A few months ago, a family member of a friend of mine sent me an email asking for advice on pursuing
a career in computer science. I enjoyed answering his questions, and I thought other aspiring
computer scientists might have similar questions, so with his permission, I decided to reproduce my
answers here. I've made a few edits here and there, mostly to remove personal information.

I want to be clear up front that I've only been doing this professional for about six years now, and
I don't consider myself any sort of expert on how to have a successful career. The path I've chosen
has worked out pretty well for me so far, but it's not the right path for everyone, and in an
industry that changes as quickly as this one does, it's always hard to know what students should
focus on when they're still several years from graduation.

### What position do you hold at Microsoft and what is the scope of your work?
I'm a Software Development Engineer working in Windows OS security. Specifically, my team and I have
spent the last several years working on [Windows Hello](http://www.microsoft.com/en-us/windows/windows-hello).
We don't do the actual template generation or matching for biometrics (face/fingerprint
authentication), but we own pretty much the whole stack below that, including basically all of the
crypto and some parts of the UI and UX. The marketing for Windows Hello mostly focuses on the
biometric aspect, but the feature is actually a lot more than that.

Under the covers, Windows Hello provides key and/or X509 certificate-based login to domains and
certain web services such as Microsoft accounts. In short, Windows Hello is more secure than using
passwords, and you can get that benefit even if you don't have the hardware to do biometrics or
don't want to use biometrics. We're working with industry standards bodies to specify and implement
a set of [web authentication APIs](https://w3c.github.io/webauthn/) which will
[allow the use of key-based authentication technologies like Windows Hello with regular websites](https://docs.microsoft.com/en-us/microsoft-edge/dev-guide/device/web-authentication),
which will hopefully eventually mean you won't have to have dozens of different passwords for each
website you visit, or reuse the same password everywhere and risk having all your accounts get
compromised.

My day-to-day work involves designing and implementing features and improvements to make Windows
Hello more secure and easier to use, and of course fixing bugs as they're found. Developers are also
responsible for writing and maintaining automated tests related to their features. Personally my
favorite part of the job is writing code, so I try to spend as much time as possible doing that.
Product managers (PMs) are responsible for mapping out the requirements, but in practice it's a very
collaborative process between PMs and developers, so there are often a lot of meetings to hash
things out.  Meetings aren't my favorite way to spend my time, but I am glad that developers get to
have input on the way features should work. The balance between design and coding varies a lot
depending on where we are in the release cycle; Microsoft still basically uses waterfall-style
development.

All of the code I write is in C++. On my team we make fairly heavy use of C++11 and C++14 (and soon
C++17) features, which have really modernized the language and made it much nicer to deal with.
Plus, trying to keep up with the latest additions to the C++ standard means I'm always learning new
techniques and tricks, which is fun.
<!-- PELICAN_END_SUMMARY -->

### What kind of education, work experience, and or skills did you cultivate to obtain your current job?
I started writing code when I was probably around 10 years old in Visual Basic 6.0. I wasn't super
dedicated to writing code when I was younger; I'd come up with projects and work on them for a few
weeks or months at a time, and then eventually "finish" or abandon them and not write any code for
several months. As a teenager, I started writing [PHP](https://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/)
and occasionally tinkered with other languages such as Java. I tried out C a few times during this
period, but I generally found it to be over my head until I picked it up in university, where I was
finally able to grasp some of the trickier concepts like stack versus heap allocation and how
pointers work.

I spent two years in the CS program at the University of Northern British Columbia, which was mostly
taught using Java. I then decided to transfer to the University of Alberta. UNBC has a decent CS
program, but it's very small and has limited funding, so they simply can't offer the variety of
courses that bigger schools can offer. For instance, I took courses at U of A in computer vision and
"Advanced Game Programming in C++." To my knowledge, UNBC doesn't offer anything like that. That
said, neither of those courses are very relevant to the work I do now, and the game programming one
was actually pretty disappointing. It ended up being more like "basic C++ programming and a few
concepts that tangentially relate to games." The best thing U of A offered was a very good
internship program, through which I landed a 16-month internship at Pason Systems in Calgary.

I think that internship was the single most important part of my education, both formal and
informal. This is not necessarily due to the technical knowledge I gained from it, but more due to
the hands-on industry experience I got. I worked with some very skilled developers who gave me a lot
of good career advice and connections within the industry, and I also consider many of them to be
great personal friends to this day. It's honestly hard for me to completely enumerate all the things
I gained from working at Pason, but career-wise, when you're looking for your first job out of
university it's a huge plus if you already have some industry experience on your resume. If you only
take one thing away from reading this post, it should be that the most important thing you can do
for your career is to take opportunities like this when they come up, even if you're not sure you're
ready for them.

The next best thing to have on your resume is a personal project (or projects). In my case, I
developed an iPhone game during my second and third years of university. I didn't really do this
with my career in mind, to be honest. At the time, the app store was fairly new and there was still
sort of a "gold rush" for iOS app developers, although it was already starting to die out by the
time I released my game. I was kind of hoping that I'd make some money off of it, but I ended up
making $0 because the game never sold enough copies to get to the threshold at which Apple actually
pays out the earnings. It was worth it for the experience and for the enjoyment I got out of the
project itself, though, and it helped me land both the internship I mentioned above and probably
also my job at Microsoft.

In terms of specific skills to cultivate, that largely depends on what you want to work on.  I've
done a bunch of web programming, both back-end and front-end, but personally I've always found
client programming more interesting. There are endless job opportunities for programming enterprise
asset management apps, but to a large extent, if you've worked on one <acronym title="Create, read,
update, delete">CRUD</acronym> app you've worked on all of them, and they're generally not very
technically interesting. For that reason, it was important to me to become proficient in C++.

That said, having strong fundamentals is more important than what particular languages you know.
It's easy to pick up a new language if you have a strong understanding of the core concepts
underlying all software development. For example, memory allocation, threads, page tables, user mode
versus kernel mode, indirection (pointers, passing by value vs by reference), compilers, recursion,
debugging, different language paradigms (imperative vs functional), etc. Pretty much any CS program
will teach you these things, but to really understand them in a hands-on manner, it helps to have
practical experience. How much of that you get kind of depends on what courses you take. Even if you
plan to focus on higher level languages, I'd recommend doing at least a little programming in C (not
C++) and assembly, because those are the best ways to get close to the metal and really understand
what a chunk of code in a high-level language translates to at the machine level.

### Do you like your job and would you recommend the field of work to others?
Generally, yes, I like my job, but not always. And I would recommend the field to others, though not
to everyone. This question reminds me of an article titled "[Non-myths about programming](http://files.mlindgren.ca/p35-ben-ari.pdf),"
which I think is worth reading if you're wondering whether or not CS is the right career path for
you. The gist of it is that some of the stereotypes that exist about computer science exist for a
reason, and depending on your personality and lifestyle preferences these may or may not be an issue
for you.

Specifically, the most obvious "downside" to CS is that you will spend most of your time staring at
a computer screen and not interacting with other people. I put "downside" in quotation marks because
if you're an introvert like me, then that's actually an upside.  I've had customer-facing jobs in
the past, and while I enjoyed some aspects of those jobs, ultimately I much prefer self-directed
work where I generally don't have to worry about being the public face of the company. Of course,
most programming jobs do still involve collaborating with a team and hashing things out in meetings,
and if you're more of a people person then there are always project management and people management
roles available. But I do have friends who went into CS and found that they disliked the relative
lack of human interaction, so for some people that can be an issue.

The other caveat is that at least for me, how much enjoyment I get out of programming largely
depends on what it is I'm actually making. I view programming as a creative exercise, but unless you
have the ambition, energy, and financial resources to create your own startup, the parameters of
that creativity will be constrained by whatever project your employer has you working on.  Business
don't measure the output of programmers in terms of code, but rather in terms of "business value,"
i.e. how much money you make for them.

When I was younger, I wanted to be a game programmer, and a big part of me still wants to do that,
but I've never seriously pursued it. I've learned that the game development industry is extremely
hard to get into and also actually not that desirable. Because it's seen as such a cool place to
work, the number of qualified candidates vastly exceeds the number of available positions, and as a
result, companies get away with offering relatively low pay despite the jobs being extremely
technically demanding and infamous for having long hours.  And even for those who do get into the
game industry, for every awesome game like Overwatch or Halo, there are a hundred shitty pay-to-win
mobile games that will suck out your soul.

CS in general doesn't suffer from an overabundance of qualified candidates; it's generally accepted
that there's a labor shortage, and as a result the job market is very friendly to employees, and
wages are high. (That said, there is [some dispute](https://www.bls.gov/opub/mlr/2015/article/stem-crisis-or-stem-surplus-yes-and-yes.htm)
over how much of a shortage there really is.) But, as with games, for every cool product or
interesting problem you might be working on, there are a hundred shitty Enterprise JavaBeans
line-of-business apps that need some poor soul to maintain them.

The point of all this is that you probably won't always be fully engaged in what you're working on.
That has certainly been the case for me. While I do think that what I work on now is pretty cool, I
ended up in security more or less by chance, and it has only been through working on it that I've
come to develop an interest in it. But it's technically challenging and impactful enough that it has
held my interest for five years now, and more generally, I enjoy programming enough that I'd
probably be doing it anyway even if I had to work on a product I found really boring.

Of course, one also has to weigh in pragmatic aspects such as job security and monetary
compensation. I think CS scores very favorably in this regard as well.  There are lots of
well-paying jobs available and the field only seems to be continuing to grow. I don't think I'd
recommend that anyone should go into CS _purely_ for the money; if one is only concerned about
money then it would probably make more sense to be a dentist or something like that. But all things
considered, I can't think of any realistic career option I'd rather be pursuing. (Sadly, I think I'm
getting a bit old to pursue a professional snowboarding career...)

### What would you tell your younger self or someone starting out in computer science today?
Besides what I wrote above, I think I would just point out that like other fields, CS has certain
fads that come and go, and it's best not to get too caught up in these. Node.js and Ruby on Rails
strike me as two frameworks which might fall into this category; they both became very popular very
quickly, and they seem to me like buzzwords that a lot of recruiters are looking for. That said, I
have to admit that I'm biased here because I don't personally like either of those technologies very
much.

Don't get me wrong&mdash;there's nothing wrong with learning Ruby on Rails, or Node.js, or any other
specific technology, whether or not it's a "fad." Being skilled in the latest thing that recruiters
are looking for is probably a good career move in most cases. I just want to reiterate what I stated
earlier, which is that it's more important to have a strong grasp of the fundamental concepts
underlying all of CS. If you have strong fundamentals, you can learn any specific language or
framework with relative ease. But if you only learn one language and don't ever think about how
concepts in that language map to fundamental CS concepts, then you're going to find it very
difficult to transition to something new.

Also, for this reason, I am very skeptical of "coding bootcamps." I find it very hard to believe
that anyone can be taught to be a competent programmer in just a few months. However, I have no
empirical data on how these programs perform, and part of my skepticism might just be subconscious
elitism and desire to preserve the value of my degree. I do think that there's a lot of room for
improvement in how computer science is taught at universities that do traditional four-year degree
programs, and there are also [serious issues with credentialism in general](http://slatestarcodex.com/2015/06/06/against-tulip-subsidies/),
but that's another topic altogether.

### Where do you see the future of computer science in five years and how are you preparing to meet those challenges?
The two big trends that seem most likely to me to have a big impact are quantum computing and
machine learning.

I know about as much about quantum computing as a layperson does about computer science in gneeral.
In other words, it's basically magic, as far as I'm concerned.  However, I can say that when we get
a truly general-purpose quantum computer which can run
[Shor's Algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm), with enough qubits to work
efficiently on 2048-bit and larger RSA keys, that will have huge implications for CS in general and
especially for security. I don't really expect this to happen in the next five years, but again, my
knowledge here is quite limited. If it does happen that soon, it's  hard to predict the magnitude of
the consequences.  Banking now relies heavily on our ability to perform transactions over the
Internet with cryptographic security guarantees, but current software uses cryptographic techniques
which will be vulnerable to quantum factorization, and changing it to use new cryptographic
techniques will not be fast or easy. At worst, I can imagine this having a huge negative impact on
the global economy as digital shopping and banking grind to a halt.

And that's not to mention all the other aspects of computing that rely on cryptographic security.
When you download a software update, your computer knows that it's safe to install because it can
validate the digital signature on the package to confirm that it came from the software publisher.
Without that, it would be almost trivial to trick any current operating system into installing
malware.

Incidentally, Microsoft [just announced](https://arstechnica.com/gadgets/2017/09/microsoft-quantum-toolkit/)
"a new quantum computing programming language, with full Visual Studio integration, along with a
quantum computing simulator." They haven't been released yet, but that's slated for later this year,
and personally I intend to play around with this toolkit to see if I can at least wrap my head
around what programming for quantum computers might look like, and what the practical implications
could be for me as a software developer.

Machine learning is something that we already have, but it is becoming more and more powerful, and
we're finding more and more ways to leverage it. For example, I do expect that fully autonomous
vehicles (i.e. level 4 or 5 according to [SAE classifications](https://en.wikipedia.org/wiki/Autonomous_car#Classification))
will probably be commercially available within the next 5-10 years, at least in certain areas where
conditions are favorable. This will have a huge economic impact as well, as a significant percentage
of the workforce will be made redundant in countries that adopt this technology. (In the US, driving
makes up something like 4 million jobs; truck driving alone is the single most common occupation in
a majority of states.)

In the case of self-driving cars, and for machine learning in general, I think the impact on the
broader economy and society in general will be more consequential than the impact on CS
specifically. Programming will probably be one of the last occupations to be automated, as it's not
really feasible to have a machine program itself until we have real artificial general intelligence,
which is probably decades away at least. Until then, you will at least need humans to define the
inputs and outputs for the machine learning system. But I do think programmers in many different
sub-disciplines will increasingly be expected to be familiar with machine learning techniques and
how they can be leveraged in an increasingly wide variety of applications. There are already many
categories of problems which are more feasible to solve using machine learning than through human
intelligence (computer vision is one example), and that set of problems will only expand as our
tools and techniques get more and more powerful.
