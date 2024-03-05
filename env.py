import os

os.environ[
    "CLOUDINARY_URL"
] = "cloudinary://238594668156571:lsx76q3oNCsymsy3D8aCtbAmFDs@dvgkiln0f"

os.environ[
    "DATABASE_URL"
] = "postgres://ttqjluvp:HSXZDMgJRBVjoNjE1BAajvvep9CRwAUT@cornelius.db.elephantsql.com/ttqjluvp"

os.environ.setdefault(
    "SECRET_KEY", "1IiF9Z1jhjWlgECo_E_xTBUeCOtBZn7GiPCeYc8Vxf5IrW-qhj8"
)

os.environ["DEV"] = "0"
