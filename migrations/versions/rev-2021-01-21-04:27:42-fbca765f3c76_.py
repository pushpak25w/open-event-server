"""empty message

Revision ID: fbca765f3c76
Revises: 102aec60f690
Create Date: 2021-01-21 04:27:42.273720

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'fbca765f3c76'
down_revision = '0c584e84a77b'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('speakers_calls', sa.Column('soft_ends_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('speakers_calls', 'soft_ends_at')
    # ### end Alembic commands ###
