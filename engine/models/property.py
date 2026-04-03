"""
Property data model for SIE analysis inputs.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PropertyData:
    address: str
    city: str
    state: str = "TX"
    zip_code: str = ""
    owner_name: str = ""
    year_built: Optional[int] = None
    unit_count: Optional[int] = None
    structure_type: str = ""          # residential / commercial / multifamily
    demo_permit_confirmed: bool = False
    tdlr_tabs_number: str = ""
    gc_name: str = ""
    gc_phone: str = ""
    rezoning_approved: bool = False
    rezoning_date: str = ""
    developer_name: str = ""
    phase: int = 1
    notes: str = ""
