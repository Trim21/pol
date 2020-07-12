"""add ep air time

Revision ID: 5ae2c65a3059
Revises: 36351ca94db8
Create Date: 2020-07-12 16:21:18.071546

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "5ae2c65a3059"
down_revision = "36351ca94db8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("ep", sa.Column("air_time", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ep", "air_time")
    # ### end Alembic commands ###
