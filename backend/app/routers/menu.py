from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, Response, status
from app.schemas import MenuCreate, MenuOut
import app.services as services

router = APIRouter(prefix="/api/menu", tags=["Menu"])

@router.post("", response_model=MenuOut, status_code=status.HTTP_201_CREATED)
def create_menu(payload: MenuCreate, response: Response):
    data_baru = services.simpan_menu_baru(payload)
    response.headers["Location"] = f"/api/menu/{data_baru['id']}"
    return data_baru

@router.get("", response_model=List[MenuOut], status_code=status.HTTP_200_OK)
def get_menu_list(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0),
    search: Optional[str] = Query(None)
):
    return services.ambil_semua_menu(skip=skip, limit=limit, search=search)

@router.get("/{id}", response_model=MenuOut, status_code=status.HTTP_200_OK)
def get_menu_detail(id: int):
    item = services.cari_menu_berdasarkan_id(id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item menu tidak ditemukan"
        )
    return item