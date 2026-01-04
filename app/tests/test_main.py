import pytest
from src.schemas import UserSchema

@pytest.mark.asyncio
async def test_pydantic_validation():
    user = UserSchema(username="dev_user", email="dev@test.com")
    assert user.username == "dev_user"

@pytest.mark.asyncio
async def test_invalid_username():
    with pytest.raises(ValueError):
        # Username muito curto (conforme definido no Field do Pydantic)
        UserSchema(username="ab", email="test@test.com")
