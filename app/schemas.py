from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

StudentIdStr = Annotated[str, StringConstraints(min_length=8, max_length=8)]
DescriptionStr = Annotated[str, StringConstraints(min_length=5, max_length=100)]
StatusStr = Annotated[str, StringConstraints(min_length=4, max_length=10)]

class UserCreate(BaseModel):
    equipment_id: int = Field(gt=1, lt=500)
    student_id: StudentIdStr
    description: DescriptionStr
    priority: int = Field(gt=1, lt=5)
    status: StatusStr

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    equipment_id: int
    student_id: StudentIdStr
    description: DescriptionStr
    priority: int 
    status: StatusStr