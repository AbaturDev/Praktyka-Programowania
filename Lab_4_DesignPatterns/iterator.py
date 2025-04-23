class Iterator:
    def __init__(self, items_collection):
        self.collection = items_collection
        self.position = 0

    def get_current_element(self):
        if 0 <= self.position < len(self.collection):
            return self.collection[self.position]
        else:
            return None

    def next_element(self):
        if self.position + 1 < len(self.collection):
            self.position += 1
        else:
            raise Exception("Next element does not exist")

    def get_next_element(self):
        if self.position + 1 < len(self.collection):
            return self.collection[self.position + 1]
        else:
            print("Next element does not exist")
            return None

    def reset_iterator(self):
        self.position = 0

    def edit_current_element(self, new_value):
        if 0 <= self.position < len(self.collection):
            self.collection[self.position] = new_value
        else:
            raise Exception("No current element to edit")

    def delete_element(self):
        if 0 <= self.position < len(self.collection):
            del self.collection[self.position]
            if self.position >= len(self.collection):
                self.position = max(0, len(self.collection) - 1)
        else:
            raise Exception("No element to delete at current position")
