"""empty message

Revision ID: 7b703c45eeae
Revises: b3f6788779ff
Create Date: 2019-11-18 16:08:21.830515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b703c45eeae'
down_revision = 'b3f6788779ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('exerciseTime', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('familiar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('heartRate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('currentHeartRate', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicHeartRate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('heartRate', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicMotionless',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('motionlessTime', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicStress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('stressLevel', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mood',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('mood', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('motionless',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('CurrentmotionlessTime', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idFamiliar', sa.Integer(), nullable=True),
    sa.Column('user', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sleep',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('sleepTime', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPersona', sa.Integer(), nullable=True),
    sa.Column('currentStressLevel', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stress')
    op.drop_table('sleep')
    op.drop_table('persona')
    op.drop_table('motionless')
    op.drop_table('mood')
    op.drop_table('historicStress')
    op.drop_table('historicMotionless')
    op.drop_table('historicHeartRate')
    op.drop_table('heartRate')
    op.drop_table('familiar')
    op.drop_table('exercise')
    # ### end Alembic commands ###