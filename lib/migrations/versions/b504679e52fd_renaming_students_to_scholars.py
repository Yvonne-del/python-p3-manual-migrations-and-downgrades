"""Renaming students to scholars

Revision ID: b504679e52fd
Revises: 5830f5efb5fb
Create Date: 2025-06-16 11:55:08.428207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b504679e52fd'
down_revision = '5830f5efb5fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
