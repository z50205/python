"""add img_id

Revision ID: a9e509277fb1
Revises: 13fee054ad82
Create Date: 2024-01-28 18:19:39.684345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9e509277fb1'
down_revision = '13fee054ad82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_id', sa.String(length=32), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.drop_column('img_id')

    # ### end Alembic commands ###
