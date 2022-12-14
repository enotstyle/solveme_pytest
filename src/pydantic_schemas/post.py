from pydantic import BaseModel, validator, Field

"""
Просто pydemic схема и тут же небольшая валидация.
"""

class Post(BaseModel):
    id: int = Field(le=2)
    title: str

    @validator("id")
    def check_that_id_is_less_than_two(cls, v):
        if v > 2:
            raise ValueError('Id is not less than two')
        else:
            return v


x = {'id': 1, 'title': 'Post 1'}
ans = Post.parse_obj(x)
print(ans.check_that_id_is_less_than_two(1))
