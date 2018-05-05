"""empty message

Revision ID: cc1d30042d02
Revises: 07db4641aa55
Create Date: 2018-05-05 16:57:33.793211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc1d30042d02'
down_revision = '07db4641aa55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('orders_item_id_fkey', 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'menus', ['item_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key('orders_item_id_fkey', 'orders', 'menus', ['item_id'], ['id'])
    # ### end Alembic commands ###
