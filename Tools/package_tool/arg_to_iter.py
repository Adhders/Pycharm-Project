

import six
from scrapy.item import BaseItem
_ITERABLE_SINGLE_VALUES = dict, BaseItem, six.text_type, bytes
def arg_to_iter(arg):
    """Convert an argument to an iterable. The argument can be a None, single
    value, or an iterable.

    Exception: if arg is a dict, [arg] will be returned
    """
    if arg is None:
        return []
    elif not isinstance(arg, _ITERABLE_SINGLE_VALUES) and hasattr(arg, '__iter__'):
        return arg
    else:
        return [arg]

tags=('junbo',)
print((arg_to_iter(tags)))