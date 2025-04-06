from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.db.database import user_collection
from app.models.user_model import User

router = APIRouter()

@router.post("/")
async def create_user(user: User):
    user_dict = user.dict()
    result = await user_collection.insert_one(user_dict)
    return {"message": "User created successfully!", "id": str(result.inserted_id)}


@router.get("/{user_id}")
async def get_user(user_id: str):
    try:
        obj_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    user = await user_collection.find_one({"_id": obj_id})
    if user:
        user["_id"] = str(user["_id"])
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{user_id}")
async def update_user(user_id: str, user: User):
    try:
        obj_id = ObjectId(user_id)
        update_data = user.dict(exclude_unset=True)
        result = await user_collection.update_one({"_id": obj_id}, {"$set": update_data})

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {"message": "User updated successfully", "updated_data": update_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    try:
        obj_id = ObjectId(user_id)
        result = await user_collection.delete_one({"_id": obj_id})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")
