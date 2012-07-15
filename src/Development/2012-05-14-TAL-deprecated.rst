TAL Templates deprecated
################################

:date: 2012-05-14
:author: Marcel Hellkamp

Andrea Belvedere found a bug in SimpleTALTemplates that went unnoticed for months. Conclusion: Nobody actually uses Bottle+TAL.

Perhaps it is a good time to remove SimpleTALTemplate support instead of fixing it. Or move it to a plugin.

Here is the deal: The TAL template adapter needs a maintainer or support will be removed within the next two releases.

https://github.com/defnull/bottle/issues/322

