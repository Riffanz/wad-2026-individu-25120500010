from typing import List, Optional
from app.schemas import MenuCreate

_menu_db: List[dict] = []
_id_counter = 1

def simpan_menu_baru(data: MenuCreate) -> dict:
    global _id_counter
    item = data.model_dump()
    item["id"] = _id_counter
    _menu_db.append(item)
    _id_counter += 1
    return item

def ambil_semua_menu(skip: int = 0, limit: int = 10, search: Optional[str] = None) -> List[dict]:
    hasil = _menu_db
    if search:
        kata_kunci = search.lower()
        hasil = [
            m for m in hasil 
            if kata_kunci in m["nama"].lower() or kata_kunci in m["sku"].lower()
        ]
    return hasil[skip : skip + limit]

def cari_menu_berdasarkan_id(item_id: int) -> Optional[dict]:
    for item in _menu_db:
        if item["id"] == item_id:
            return item
    return None