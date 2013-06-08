import helper
from lxml import etree
from lxml.html import fromstring
from pprint import pformat

ns = etree.FunctionNamespace(None)
for helper_func in dir(helper):
    func_prefix = 'xpath_func_'
    if helper_func.startswith(func_prefix):
        ns[helper_func[len(func_prefix):]] = getattr(helper,helper_func)  #function's name is without the prefix

example_html = '<html><body><p class="tokenize_me">example;tokenize;string</p><p class="title_me">make me a title</p></body></html>'
tree = fromstring(example_html)
print('Tokenized string result: ' + pformat(tree.xpath('tokenize(//p[@class="tokenize_me"]/text(),";")')))
print('Title string result: ' + pformat(tree.xpath('make_title(//p[@class="title_me"]/text())')))
