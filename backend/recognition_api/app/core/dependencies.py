from typing import Annotated

from fastapi import Depends

from app.core.config import Settings, get_settings

SettingsDependency = Annotated[Settings, Depends(get_settings)]
"""Зависимость для endpoint, которые нуждаются в информации о приложении"""

from app.services.model_service import RecognitionModelService, get_model_service

RecognitionModelServiceDependency = Annotated[
    RecognitionModelService, Depends(get_model_service)
]
"""Зависимость для endpoint, которые обращаются к модели компьютерного зрения."""
