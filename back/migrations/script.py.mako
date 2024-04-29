"""
${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# Revision identifiers
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    """
    Applies changes made in migration.
    """

    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """
    Reverts changes made by migration.
    """

    ${downgrades if downgrades else "pass"}
