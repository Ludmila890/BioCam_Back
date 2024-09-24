"""revision inicial

Revision ID: 4ec9c9effc14
Revises: 
Create Date: 2024-09-24 00:26:37.434219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ec9c9effc14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Clientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('correo', sa.String(length=100), nullable=False),
    sa.Column('clave', sa.String(length=255), nullable=False),
    sa.Column('telefono', sa.String(length=20), nullable=True),
    sa.Column('direccion', sa.String(length=255), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('ultima_actividad', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('Componentes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=50), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('fecha_actualizacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Carritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('fecha_actualizacion', sa.DateTime(), nullable=True),
    sa.Column('estado', sa.Enum('abierto', 'cerrado'), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['Clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Carrito_Items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('carrito_id', sa.Integer(), nullable=False),
    sa.Column('componente_id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('fecha_agregado', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['carrito_id'], ['Carritos.id'], ),
    sa.ForeignKeyConstraint(['componente_id'], ['Componentes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Carrito_Items')
    op.drop_table('Carritos')
    op.drop_table('Componentes')
    op.drop_table('Clientes')
    # ### end Alembic commands ###
