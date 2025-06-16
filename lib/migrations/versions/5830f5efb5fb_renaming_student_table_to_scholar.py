"""Renaming student table to scholar

Revision ID: 5830f5efb5fb
Revises: b078be796e6e
Create Date: 2025-06-16 11:54:27.038450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5830f5efb5fb'
down_revision = 'b078be796e6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
