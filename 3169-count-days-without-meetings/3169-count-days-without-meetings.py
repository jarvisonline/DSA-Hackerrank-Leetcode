class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        day_map = defaultdict(int)
        prefix_sum = 0
        free_days = 0
        previous_day = days

        for meeting in meetings:
            previous_day = min(previous_day, meeting[0])

            day_map[meeting[0]] += 1
            day_map[meeting[1] + 1] -= 1

        free_days += previous_day - 1
        for current_day in sorted(day_map.keys()):
            if prefix_sum == 0:
                free_days += current_day - previous_day
            prefix_sum += day_map[current_day]
            previous_day = current_day

        free_days += days - previous_day + 1
        return free_days