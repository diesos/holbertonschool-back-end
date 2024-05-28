#!/usr/bin/env python3
""" Function that returns a tuple of size 2 with the start and end indexes """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns tuple of size 2 with start and end indexes
    Args:
        page (int): page number
        page_size (int): page size
    Returns:
        Tuple[int, int]: start and end indexes
     """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
