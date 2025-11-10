# OPTIMAL PAGE REPLACEMENT ALGORITHM

def optimal_page_replacement(pages, capacity):
    """
    Simulates the Optimal Page Replacement algorithm.
    :param pages: List of page references
    :param capacity: Number of pages that can be held in memory
    :return: Number of page faults
    """
    memory = []  # Holds the current pages in memory
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]
        # If the page is not in memory, we need to replace a page
        if page not in memory:
            if len(memory) == capacity:  # Memory full → replace a page
                farthest_use = -1
                index_to_replace = -1
                for j in range(len(memory)):
                    try:
                        # Find next use of the page (absolute index)
                        next_use = pages[i+1:].index(memory[j]) + (i+1)
                    except ValueError:
                        next_use = float('inf')  # Page not used again
                    if next_use > farthest_use:
                        farthest_use = next_use
                        index_to_replace = j
                # Replace the page
                memory[index_to_replace] = page
            else:
                # Free space in memory
                memory.append(page)
            # Increment page faults
            page_faults += 1

    return page_faults
# Example usage
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    capacity = 3
    print("Number of page faults:", optimal_page_replacement(pages, capacity))