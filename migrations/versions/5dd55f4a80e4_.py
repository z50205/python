"""empty message

Revision ID: 5dd55f4a80e4
Revises: edcba39bb741
Create Date: 2024-01-31 00:20:46.484393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dd55f4a80e4'
down_revision = 'edcba39bb741'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_photo', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.drop_column('total_photo')

    # ### end Alembic commands ###
