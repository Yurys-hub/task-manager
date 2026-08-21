'''Representation of task'''
from dataclasses import dataclass, asdict

@dataclass
class Task:
    '''Represents one task'''
    task_id: int
    name: str
    description: str
    status: str = "in progress"

    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            task_id=data['task_id'],
            name=data['name'],
            description=data['description'],
            status=data['status']
        )
