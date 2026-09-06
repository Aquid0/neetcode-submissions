import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []      
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        def can_meet_before_target(p1: tuple[int, int], p2: tuple[int, int], target: int) -> bool:
            x1, v1 = p1
            x2, v2 = p2

            if v1 <= v2:
                return False

            t = (x2 - x1) / (v1 - v2)

            shared_pos = x1 + v1 * t

            return shared_pos <= target

        while cars:
            if len(stack) <= 0:
                stack.append(cars.pop(0))
            else:
                car = cars.pop(0)
                prev = stack[-1]

                meets = can_meet_before_target(car, prev, target)

                if not meets:
                    # Car does not belong to the fleet
                    stack.append(car)
                else:
                    pass

        return len(stack)
            


                
                
 
        