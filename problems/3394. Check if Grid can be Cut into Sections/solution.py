class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        event_x = []
        event_y = []

        for x_s, _, x_e, _ in sorted(rectangles, key = lambda x: (x[0])):
            event_x.append([x_s, x_e]) 

        check = 0
        max_end = event_x[0][1]
        for x_s, x_e in event_x:
            if max_end <= x_s:
                check += 1
                if check >= 2:
                    return True
            max_end = max(max_end, x_e)

        for _, y_s, _, y_e in sorted(rectangles, key = lambda x: (x[1])):
            event_y.append([y_s, y_e]) 

        check = 0
        max_end = event_y[0][1]
        for y_s, y_e in event_y:
            if max_end <= y_s:
                check += 1
                if check >= 2:
                    return True
            max_end = max(max_end, y_e)


        return False