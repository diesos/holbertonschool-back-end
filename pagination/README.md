# <p align = "center">📃 Pagination</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

<img src="https://i.imgur.com/ApIWwBr.png" width="100%"/>

### Learning Objectives
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

### Tasks
- **0-simple_helper_function.py** : function named `index_range` that takes two integer arguments `page` and `page_size`
- **1-simple_pagination.py** : implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10
- **2-hypermedia_pagination.py** : implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:
    - `page_size`: the length of the returned dataset page
    - `page`: the current page number
    - `data`: the dataset page (equivalent to return from previous task)
    - `next_page`: number of the next page, None if no next page
    - `prev_page`: number of the previous page, None if no previous page
    - `total_pages`: the total number of pages in the dataset as an integer
- **3-hypermedia_del_pagination.py** : implement a `get_hyper_index` method with two integer arguments: `index` with a `None` default value and `page_size` with default value of 10. The method should return a dictionary with the following key-value pairs:
    - `index`: the current start index of the return page
    - `next_index`: the next index to query with
    - `page_size`: the current page size
    - `data`: the actual page of the dataset
