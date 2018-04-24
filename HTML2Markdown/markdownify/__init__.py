#!/usr/bin/python
#coding:utf-8

from bs4 import BeautifulSoup, NavigableString
import re
import six

# 正则
convert_heading_re = re.compile(r'convert_h(\d+)')
# 正则
line_beginning_re = re.compile(r'^', re.MULTILINE)
# 正则
whitespace_re = re.compile(r'[\r\n\s\t ]+')

FRAGMENT_ID = '__MARKDOWNIFY_WRAPPER__'

wrapped = '<div id="%s">%%s</div>' % FRAGMENT_ID


# Heading styles
ATX = 'atx'
ATX_CLOSED = 'atx_closed'
UNDERLINED = 'underlined'
SETEXT = UNDERLINED

# 替换
def escape(text):
    if not text:
        return ''
    return text.replace('_', r'\_')

# 转换 dict
def _todict(obj):
    return dict((k, getattr(obj, k)) for k in dir(obj) if not k.startswith('_'))

# 类定义
class MarkdownConverter(object):
    # 类定义
    class DefaultOptions:
        strip = None
        convert = None
        autolinks = True
        heading_style = UNDERLINED
        bullets = '*+-'  # An iterable of bullet types.
    # 类定义
    class Options(DefaultOptions):
        pass

    # 初始化
    def __init__(self, **options):
        # Create an options dictionary. Use DefaultOptions as a base so that
        # it doesn't have to be extended.
        self.options = _todict(self.DefaultOptions)
        self.options.update(_todict(self.Options))
        self.options.update(options)
        if self.options['strip'] is not None and self.options['convert'] is not None:
            raise ValueError('You may specify either tags to strip or tags to'
                             ' convert, but not both.')

    def convert(self, html):
        # We want to take advantage of the html5 parsing, but we don't actually
        # want a full document. Therefore, we'll mark our fragment with an id,
        # create the document, and extract the element with the id.
        html = wrapped % html
        soup = BeautifulSoup(html, 'html.parser')
        return self.process_tag(soup.find(id=FRAGMENT_ID), children_only=True)

    # 处理标签
    # node 处理的那个节点
    # children_only 只处理子节点
    def process_tag(self, node, children_only=False):
        text = ''

        # Convert the children first
        # 首先获得子标签
        for el in node.children:

            # 如果 el 是NavigableString类型的话
            # Tag中的字符串即为NavigableString对象。
            # 如果里面不再包含另外的标签的话，需要直接连接
            if isinstance(el, NavigableString):
                text += self.process_text(six.text_type(el))
            else:
                elclass = el.attrs.get('class', None)

                if elclass is not None and elclass[0] == u'example_code':
                    text += '<pre>\n'
                    # text += self.process_just_appen(str(el).decode('utf-8'))
                    text += self.process_just_appen(el.get_text())
                    text += '</pre>\n\n'
                elif elclass is not None and elclass[0] == u'prettyprint':
                    text += '<pre>\n'
                    text += self.process_just_appen(el.get_text())
                    text += '\n</pre>\n\n'
                elif el.name is not None and el.name == u'pre':
                    # text += '<pre>\n'
                    text += '\n```\n'
                    text += self.process_just_appen(el.get_text())
                    text += '\n```\n\n'
                    # text += '\n</pre>\n\n'

                elif el.name is not None and el.name == u'table':
                   # print el.contents
                   # print type(el.contents)

                   for cc in el.contents:
                       text += '\n<table>\n'
                       text += str(cc).decode("UTF-8")
                       text += '\n</table>\n'
                else:
                    text += self.process_tag(el)

        if not children_only:
            convert_fn = getattr(self, 'convert_%s' % node.name, None)
            if convert_fn and self.should_convert_tag(node.name):
                text = convert_fn(node, text)

        return text

    # 处理字符
    def process_text(self, text):
        return escape(whitespace_re.sub(' ', text or ''))

    # 直接追加
    def process_just_appen(self,text):
        return text;

    # 处理属性
    def __getattr__(self, attr):
        # Handle headings
        mathch = convert_heading_re.match(attr)
        if mathch:
            n = int(mathch.group(1))

            def convert_tag(el, text):
                return self.convert_hn(n, el, text)

            convert_tag.__name__ = 'convert_h%s' % n
            setattr(self, convert_tag.__name__, convert_tag)

            return convert_tag

        raise AttributeError(attr)

    # 标签转换
    def should_convert_tag(self, tag):
        tag = tag.lower()
        strip = self.options['strip']
        convert = self.options['convert']
        if strip is not None:
            return tag not in strip
        elif convert is not None:
            return tag in convert
        else:
            return True
    # 缩进
    def indent(self, text, level):
        return line_beginning_re.sub('\t' * level, text) if text else ''

    # 下划线
    def underline(self, text, pad_char):
        text = (text or '').rstrip()
        return '%s\n%s\n\n' % (text, pad_char * len(text)) if text else ''

    # 替换a标签
    def convert_a(self, el, text):
        href = el.get('href')
        title = el.get('title')
        if self.options['autolinks'] and text == href and not title:
            # Shortcut syntax
            return '<%s>' % href
        title_part = ' "%s"' % title.replace('"', r'\"') if title else ''
        return '[%s](%s%s)\n' % (text or '', href, title_part) if href else text or ''
    # 替换b 标签
    def convert_b(self, el, text):
        return self.convert_strong(el, text)
    # 替换块
    def convert_blockquote(self, el, text):
        return '\n' + line_beginning_re.sub('> ', text) if text else ''

    # LW added here 替换 pre
    def convert_pre(self, el, text):
        return '\n``` \n%s \n```\n' % text if text else ''

    # 替换 br
    def convert_br(self, el, text):
        return '  \n'
    # 替换 em
    def convert_em(self, el, text):
        return '*%s*' % text if text else ''
    # 替换 header
    def convert_hn(self, n, el, text):
        style = self.options['heading_style']
        text = text.rstrip()
        if style == UNDERLINED and n <= 2:
            line = '=' if n == 1 else '-'
            return self.underline(text, line)
        hashes = '#' * n
        if style == ATX_CLOSED:
            return '%s %s %s\n\n' % (hashes, text, hashes)
        return '%s %s\n\n' % (hashes, text)
    # 替换 i 标签
    def convert_i(self, el, text):
        return self.convert_em(el, text)
    # 替换 list
    def convert_list(self, el, text):
        nested = False
        while el:
            if el.name == 'li':
                nested = True
                break
            el = el.parent
        if nested:
            text = '\n' + self.indent(text, 1)
        return text

    convert_ul = convert_list
    convert_ol = convert_list
    # 替换 li
    def convert_li(self, el, text):
        parent = el.parent
        if parent is not None and parent.name == 'ol':
            bullet = '%s.' % (parent.index(el) + 1)
        else:
            depth = -1
            while el:
                if el.name == 'ul':
                    depth += 1
                el = el.parent
            bullets = self.options['bullets']
            bullet = bullets[depth % len(bullets)]
        return '%s %s\n' % (bullet, text or '')
    # 替换 p 标签
    def convert_p(self, el, text):
        return '%s\n\n' % text if text else ''
    # 替换 strong 标签
    def convert_strong(self, el, text):
        return '**%s**' % text if text else ''
    # 替换 img
    def convert_img(self, el, text):
        alt = el.attrs.get('alt', None) or ''
        src = el.attrs.get('src', None) or ''
        title = el.attrs.get('title', None) or ''
        title_part = ' "%s"' % title.replace('"', r'\"') if title else ''
        return '![%s](%s%s)\n' % (alt, src, title_part)


def markdownify(html, **options):
    return MarkdownConverter(**options).convert(html)
