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

<style>${homelink()}</style>
<link rel="canonical" href="https://pdoc3.github.io/pdoc/doc/${module.url()[:-len('index.html')] if module.is_package else module.url()}">
<link rel="icon" href="https://pdoc.github.io/pdoc/logo.png">
