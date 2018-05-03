"""empty message

Revision ID: fedf447ed578
Revises: 9aefbdf8aa81
Create Date: 2018-05-02 20:48:23.892455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fedf447ed578'
down_revision = '9aefbdf8aa81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'menus_meal_id_fkey', 'menus', type_='foreignkey')
    op.create_foreign_key(None, 'menus', 'meals', ['meal_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'menus', type_='foreignkey')
    op.create_foreign_key(u'menus_meal_id_fkey', 'menus', 'meals', ['meal_id'], ['id'])
    # ### end Alembic commands ###
