import cloudinary.uploader

cloudinary.config(
    cloud_name="dtno3vc4f",
    api_key="576867971649242",
    api_secret="8ZcPy4RKfhiGolOJPyChw8EFkpI"
)


def get_uploader():
    return cloudinary.uploader
