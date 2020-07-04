from abc import ABC, abstractmethod


class Group(ABC):
    @abstractmethod
    def child_values(self):
        pass

    def validate(self):
        return self.validate_range() and self.validate_duplicates()

    def validate_range(self):
        child_values = self.child_values()
        max_val = max(child_values)
        min_val = min(child_values)
        return max_val in range(0, 10) and min_val in range(0, 10)

    def validate_duplicates(self):
        seen = {}
        dupes = []
        child_values = self.child_values()
        for _v in child_values:
            if _v == 0:
                continue
            if _v not in seen:
                seen[_v] = 1
            else:
                if seen[_v] == 1:
                    dupes.append(_v)
                seen[_v] += 1
        return len(dupes) == 0
