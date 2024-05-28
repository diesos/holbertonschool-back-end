#!/usr/bin/env python3
""" Simple pagination + add get_hyper function """

import csv
import math
from typing import List
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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns page of dataset
        Args:
            page (int): page number
            page_size (int): page size
        Returns:
            List[List]: page of dataset
         """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_rows = index_range(page, page_size)

        start_index = total_rows[0]
        end_index = total_rows[1]

        if len(self.dataset()) < end_index:
            return []

        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Returns a dictionary with pagination info
        Args:
            page (int): page number
            page_size (int): page size
        Returns:
            dict: pagination info
        """
        dataset_page = self.get_page(page, page_size)

        start_index, end_index = index_range(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if end_index < len(self.dataset()) else None

        previous_page = page - 1 if start_index > 0 else None

        pagination_info = {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": previous_page,
            "total_pages": total_pages
        }

        return pagination_info
