class GroupModel:
    def __init__(self):
        self.origin_id = None
        self.destination_id = None

    def set_origin(self, group_id):
        self.origin_id = group_id

    def set_destination(self, group_id):
        self.destination_id = group_id

    def get_origin(self):
        return self.origin_id

    def get_destination(self):
        return self.destination_id
