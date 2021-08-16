class ForUser:
    def __init__(self, user_id, user_name, phone, email, role, dob, created_on, modified_on):
        self.user_id = user_id
        self.user_name = user_name
        self.phone = phone
        self.email = email
        self.role = role
        self.dob = dob
        self.created_on = created_on
        self.modified_on = modified_on


class ForTask:
    def __init__(self, task_id, name, description, status, priority, notes, bookmark, owner_id, creator_id, created_on, modified_on):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.status = status
        self.priority = priority
        self.notes = notes
        self.bookmark = bookmark
        self.owner_id = owner_id
        self.creator_id = creator_id
        self.created_on = created_on
        self.modified_on = modified_on