import uvicorn

from core.config import Settings, get_settings

if __name__ == "__main__":
    settings: Settings = get_settings()

    print(
        f"Swagger UI URL: \033[97mhttp://{settings.DOMAIN}:{settings.BACKEND_PORT}/docs\033[0m"
    )

    uvicorn.run(
        app="main:recognition_api",
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=settings.DEV_MODE,
    )
