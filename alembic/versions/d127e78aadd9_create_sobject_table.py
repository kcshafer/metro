"""Create sobject table

Revision ID: d127e78aadd9
Revises: 
Create Date: 2016-07-28 12:59:51.519759

"""

# revision identifiers, used by Alembic.
revision = 'd127e78aadd9'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'sobject',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('amount', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('sobject')
