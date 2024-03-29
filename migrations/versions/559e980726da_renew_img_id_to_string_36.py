"""renew img_id to String(36)

Revision ID: 559e980726da
Revises: a9e509277fb1
Create Date: 2024-01-28 18:32:20.941539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '559e980726da'
down_revision = 'a9e509277fb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.alter_column('img_id',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=36),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.alter_column('img_id',
               existing_type=sa.String(length=36),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)

    # ### end Alembic commands ###
