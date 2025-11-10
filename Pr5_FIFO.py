# FIFO Page Replacement Algorithm

from collections import deque

def fifo_page_replacement(pages, num_frames):
    """
    Implements FIFO (First-In-First-Out) page replacement algorithm.
    
    Args:
        pages: List of page references
        num_frames: Number of frames available in memory
        
    Returns:
        Number of page faults
    """
    frames = set()
    fifo_queue = deque()
    page_faults = 0
    
    for page in pages:
        if page not in frames:
            page_faults += 1
            if len(frames) == num_frames:
                oldest_page = fifo_queue.popleft()
                frames.remove(oldest_page)
            frames.add(page)
            fifo_queue.append(page)
            
    return page_faults

if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    num_frames = 3
    faults = fifo_page_replacement(pages, num_frames)
    print(f"Number of page faults using FIFO: {faults}")