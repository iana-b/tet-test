def appearance(intervals: dict[str, list[int]]) -> int:
    total = 0
    i, j = 0, 0
    pupil_intervals = merge_intervals(
        limit_intervals(intervals['pupil'], intervals['lesson'][0], intervals['lesson'][1])
    )
    tutor_intervals = merge_intervals(
        limit_intervals(intervals['tutor'], intervals['lesson'][0], intervals['lesson'][1])
    )
    while i < len(pupil_intervals) and j < len(tutor_intervals):
        a_start, a_end = pupil_intervals[i]
        b_start, b_end = tutor_intervals[j]
        start = max(a_start, b_start)
        end = min(a_end, b_end)
        if start < end:
            total += end - start
        if a_end < b_end:
            i += 1
        else:
            j += 1
    return total


def limit_intervals(interval: list[int], lesson_start: int, lesson_end: int) -> list[tuple[int, int]]:
    correct_intervals = []
    for i in range(0, len(interval), 2):
        start = max(interval[i], lesson_start)
        end = min(interval[i + 1], lesson_end)
        if start < end:
            correct_intervals.append((start, end))
    return correct_intervals


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        curr_start, curr_end = current
        if curr_start <= prev_end:
            merged[-1] = (prev_start, max(prev_end, curr_end))
        else:
            merged.append(current)
    return merged
