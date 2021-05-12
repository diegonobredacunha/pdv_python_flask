"""empty message

Revision ID: 9e2c15ecb0a0
Revises: 
Create Date: 2021-04-10 21:32:16.464697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e2c15ecb0a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pessoas',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('dt_nascimento', sa.Date(), nullable=True),
    sa.Column('sexo', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pessoas')
    # ### end Alembic commands ###