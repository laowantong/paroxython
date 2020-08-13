<%!
    from pdoc.html_helpers import minify_css
%>
<%def name="homelink()" filter="minify_css">
    .homelink {
        display: block;
    }
    .homelink:hover {
        color: inherit;
    }
    .homelink img {
        margin: auto;
        margin-bottom: .3em;
    }
</%def>
<a href="https://github.com/laowantong/paroxython"><img style="position: absolute; top: 0; right: 0; border: 0; width: 150px; height: 150px" src="https://laowantong.github.io/paroxython/resources/source_on_github.png" alt="Source on GitHub"></a>
<style>${homelink()}</style>
<link rel="canonical" href="https://laowantong.github.io/${module.url()[:-len('index.html')] if module.is_package else module.url()}">
<link rel="icon" href="https://laowantong.github.io/paroxython/resources/logo.png">
