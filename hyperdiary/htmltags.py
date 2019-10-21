_escaped_attrs = ('id', 'class', 'type')

_render_compact_tags = ('p', 'span', 'a', 'b', 'i', 'small', 'li',
                        'h1', 'h2', 'h3', 'h4',
                        'button', 'ht', 'td', 'title')


class HTMLElement(object):
    tag = 'div'

    def __init__(self, *content, **attributes):
        self.content = list(content)
        self.attributes = attributes
        for a in _escaped_attrs:
            if '_' + a in self.attributes:
                self.attributes[a] = self.attributes.pop('_' + a)

    def append(self, *items):
        self.content += items
        return self

    def __call__(self, *items):
        return self.append(*items)

    def subelement(self, item):
        self.content.append(item)
        return item

    def lazy_render_attributes(self):
        if self.attributes:
            for k, v in self.attributes.items():
                yield ' '
                yield str(k)
                yield '="'
                yield str(v)
                yield '"'

    def lazy_render(self, indent='', add_indent=''):
        is_doc_root = self.tag.lower() == 'html'
        if is_doc_root:
            yield '<!DOCTYPE HTML>\n'
        do_linebreak = self.tag not in _render_compact_tags and self.content
        yield indent
        yield '<'
        yield self.tag
        yield from self.lazy_render_attributes()
        yield '>'
        if do_linebreak:
            yield '\n'
        child_indent = indent + add_indent if do_linebreak else ''
        if not do_linebreak:
            add_indent = ''
        for child in self.content:
            if hasattr(child, 'lazy_render'):
                yield from child.lazy_render(child_indent, add_indent)
            else:
                yield '{}{}'.format(child_indent, child)
            if do_linebreak:
                yield '\n'
        if do_linebreak:
            yield indent
        yield '</'
        yield self.tag
        yield '>'
        if is_doc_root:
            yield '\n'

    def __str__(self):
        return ''.join(self.lazy_render(add_indent='  '))

    def write(self, fname):
        with open(fname, 'w') as f:
            for s in self.lazy_render(add_indent='  '):
                f.write(s)


# TAGS

class a (HTMLElement):
    tag = 'a'


class article (HTMLElement):
    tag = 'article'


class body (HTMLElement):
    tag = 'body'


class button (HTMLElement):
    tag = 'button'


class div (HTMLElement):
    tag = 'div'


class footer (HTMLElement):
    tag = 'footer'


class form (HTMLElement):
    tag = 'form'


class h1 (HTMLElement):
    tag = 'h1'


class h2 (HTMLElement):
    tag = 'h2'


class h3 (HTMLElement):
    tag = 'h3'


class h4 (HTMLElement):
    tag = 'h4'


class head (HTMLElement):
    tag = 'head'


class header (HTMLElement):
    tag = 'header'


class hr (HTMLElement):
    tag = 'hr'


class html (HTMLElement):
    tag = 'html'


class img (HTMLElement):
    tag = 'img'


class li (HTMLElement):
    tag = 'li'


class link (HTMLElement):
    tag = 'link'


class meta (HTMLElement):
    tag = 'meta'


class nav (HTMLElement):
    tag = 'nav'


class ol (HTMLElement):
    tag = 'ol'


class p (HTMLElement):
    tag = 'p'


class small (HTMLElement):
    tag = 'small'


class span (HTMLElement):
    tag = 'span'


class style (HTMLElement):
    tag = 'style'


class table (HTMLElement):
    tag = 'table'


class tbody (HTMLElement):
    tag = 'tbody'


class td (HTMLElement):
    tag = 'td'


class th (HTMLElement):
    tag = 'th'


class thead (HTMLElement):
    tag = 'thead'


class title (HTMLElement):
    tag = 'title'


class tr (HTMLElement):
    tag = 'tr'


class ul (HTMLElement):
    tag = 'ul'
