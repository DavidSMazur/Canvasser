from pydantic import BaseModel


class Canvas(BaseModel):
    course: int


class Submit(BaseModel):
    file_path: str
    course_id: str
    assignment_id: str
