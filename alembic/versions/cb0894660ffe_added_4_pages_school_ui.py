"""added 4 pages school ui

Revision ID: cb0894660ffe
Revises: 784cdfeb474d
Create Date: 2022-09-26 11:30:12.763948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb0894660ffe'
down_revision = '784cdfeb474d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('school',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('institutionName', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('urlName', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('postalAddress', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('totalNoOfTeachingStaff', sa.Integer(), nullable=True),
    sa.Column('totalBoys', sa.Integer(), nullable=True),
    sa.Column('correspondentName', sa.String(), nullable=True),
    sa.Column('medium', sa.String(), nullable=True),
    sa.Column('officeEmailId', sa.String(), nullable=True),
    sa.Column('specialNeeds', sa.String(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.Column('pincode', sa.Integer(), nullable=True),
    sa.Column('officialPhoneNumber', sa.String(), nullable=True),
    sa.Column('assessmentAcademicYear', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('currentNoOfStudents', sa.Integer(), nullable=True),
    sa.Column('correspondentMobileNo', sa.String(), nullable=True),
    sa.Column('nameOfPrincipal', sa.String(), nullable=True),
    sa.Column('yearOfEstablish', sa.Integer(), nullable=True),
    sa.Column('natureOfAffiliation', sa.String(), nullable=True),
    sa.Column('currentNoOfGirls', sa.Integer(), nullable=True),
    sa.Column('totalOfNonTeachingStaff', sa.Integer(), nullable=True),
    sa.Column('correspondentEmailId', sa.String(), nullable=True),
    sa.Column('schoolLevel', sa.String(), nullable=True),
    sa.Column('principalOrHeadMobileNo', sa.String(), nullable=True),
    sa.Column('principalOrHeadEmailId', sa.String(), nullable=True),
    sa.Column('principalOrHeadOfficePhoneNo', sa.String(), nullable=True),
    sa.Column('isInstituteRecognizedByGovt', sa.String(), nullable=True),
    sa.Column('nameOfBoardAffiliated', sa.String(), nullable=True),
    sa.Column('affiliationNo', sa.String(), nullable=True),
    sa.Column('yearOfAffiliation', sa.String(), nullable=True),
    sa.Column('isAffiliationPermanentOrTemp', sa.String(), nullable=True),
    sa.Column('conditionsOfAffiliation', sa.String(), nullable=True),
    sa.Column('minorityStausCertificate', sa.String(), nullable=True),
    sa.Column('christian', sa.String(), nullable=True),
    sa.Column('hindu', sa.String(), nullable=True),
    sa.Column('islam', sa.String(), nullable=True),
    sa.Column('others', sa.String(), nullable=True),
    sa.Column('nonBelievers', sa.String(), nullable=True),
    sa.Column('fireSafetyCertificate', sa.String(), nullable=True),
    sa.Column('sanitationCertificate', sa.String(), nullable=True),
    sa.Column('buildingSafetyCertificate', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('school')
    # ### end Alembic commands ###