from typing import TypeVar
from collections import Iterator


ReturnType = TypeVar("ReturnType")


class ItemPaged(Iterator[ReturnType]):
    def __init__(self, *args, **kwargs):
        """Return an iterator of items.

        args and kwargs will be passed to the PageIterator constructor directly,
        except page_iterator_class
        """
        self._args = args
        self._kwargs = kwargs
        self._page_iterator = None
        self._page_iterator_class = self._kwargs.pop(
            "page_iterator_class", PageIterator
        )

    def by_page(self, continuation_token=None):
        # type: (Optional[str]) -> Iterator[Iterator[ReturnType]]
        """Get an iterator of pages of objects, instead of an iterator of objects.

        :param str continuation_token:
            An opaque continuation token. This value can be retrieved from the
            continuation_token field of a previous generator object. If specified,
            this generator will begin returning results from this point.
        :returns: An iterator of pages (themselves iterator of objects)
        """
        return self._page_iterator_class(
            continuation_token=continuation_token, *self._args, **self._kwargs
        )

    def __repr__(self):
        return "<iterator object azure.core.paging.ItemPaged at {}>".format(hex(id(self)))

    def __iter__(self):
        """Return 'self'."""
        return self

    def __next__(self):
        if self._page_iterator is None:
            self._page_iterator = itertools.chain.from_iterable(self.by_page())
        return next(self._page_iterator)

    next = __next__  # Python 2 compatibility.

if __name__ == '__main__':
    ItemPaged({}, None)