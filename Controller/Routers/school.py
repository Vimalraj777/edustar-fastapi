from ctypes.wintypes import PINT
from pickle import GLOBAL
from typing import Set
# from webbrowser import get
from fastapi import status,HTTPException , APIRouter , Depends
from sqlalchemy.orm import Session , relationship
from Utils import utils
from Databases.database import get_db
# from Model import user_profile
from Model import school_model
from Schema import school_schema
from Authorization import oauth2



router=APIRouter(
    tags=['Users']
)

# a function to split the value alone as a list from a dictionary 
def set_data(data):
    key=[]
    get=[]
    set=[]
    for list in data:
        key =list.keys()
        break
    for list in data:
        for value in key:
            get.append(list[value])
        set.append(get)
        get=[]
    return set        



# Insert the data of school Profile
@router.post("/post") 
def crate_post(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    post['scholarship']=set_data(post['scholarship'])
    post['enrollment']=set_data(post['enrollment'])
    # print(post['scholarship'])
    new_post=school_model.Information( **post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post.id}



# This method is used to get the logged in user's record from 'School Profile' Data Table.
@router.get("/profileget")
def test_post(db:Session=Depends(get_db),user_id:str=Depends(oauth2.get_current_user)):
    user_id.id=str(user_id.id)
    new_post=db.query(school_model.Information).filter(school_model.Information.id==user_id.id)
    get=new_post.first()
    print("hiii")
    print(get.enrollment)
    return {'School1':
        {'id':get.id,'institutionName':get.institutionName,'state':get.state,'urlName':get.urlName,'officeEmailId':get.officeEmailId,'district':get.district,'pincode':get.pincode,'specialNeeds':get.specialNeeds,'yearOfEstablish':get.yearOfEstablish,'natureOfAffiliation':get.natureOfAffiliation,'currentNoOfGirls':get.currentNoOfGirls,'totalOfNonTeachingStaff':get.totalOfNonTeachingStaff},
        'School2':
        {'location':get.location,'postalAddress':get.postalAddress,'city':get.city,'officialPhoneNumber':get.officialPhoneNumber,'assessmentAcademicYear':get.assessmentAcademicYear,'gender':get.gender,'correspondentEmailId':get.correspondentEmailId,'schoolLevel':get.schoolLevel,'principalOrHeadMobileNo':get.principalOrHeadMobileNo},
        'School3':
        {'totalNoOfTeachingStaff':get.totalNoOfTeachingStaff,'totalBoys':get.totalBoys,'correspondentName':get.correspondentName,'medium':get.medium,'currentNoOfStudents':get.currentNoOfStudents,'correspondentMobileNo':get.correspondentMobileNo,'nameOfPrincipal':get.nameOfPrincipal,'principalOrHeadEmailId':get.principalOrHeadEmailId,'principalOrHeadOfficePhoneNo':get.principalOrHeadOfficePhoneNo},
        'School4':
        {'isInstituteRecognizedByGovt':get.isInstituteRecognizedByGovt,'nameOfBoardAffiliated':get.nameOfBoardAffiliated,'affiliationNo':get.affiliationNo,'yearOfAffiliation':get.yearOfAffiliation,'isAffiliationPermanentOrTemp':get.isAffiliationPermanentOrTemp,'conditionsOfAffiliation':get.conditionsOfAffiliation,'minorityStausCertificate':get.minorityStausCertificate,'christian':get.christian,'hindu':get.hindu,'islam':get.islam,'others':get.others,'nonBelievers':get.nonBelievers,'fireSafetyCertificate':get.fireSafetyCertificate,'sanitationCertificate':get.sanitationCertificate,'buildingSafetyCertificate':get.buildingSafetyCertificate},
        'School5':
        {'schoolOwnedBy':get.schoolOwnedBy,'nameOfTheTrustOrCompany':get.nameOfTheTrustOrCompany,'isTrustOrCompanyRegistered':get.isTrustOrCompanyRegistered,'underWhichAct':get.underWhichAct,'yearOfRegistration':get.yearOfRegistration,'registrationNo':get.registrationNo,'validityOfRegistrationPeriod':get.validityOfRegistrationPeriod,'nameOfPresidentOrChairman':get.nameOfPresidentOrChairman,'designationOfPresidentOrChairman':get.designationOfPresidentOrChairman,'addressOfPresidentOrChairman':get.addressOfPresidentOrChairman,'phoneNoOfPresidentOrChairman':get.phoneNoOfPresidentOrChairman,'emailAddressOfPresidentOrChairman':get.emailAddressOfPresidentOrChairman},
        'School6':
        {'governingBodyOfTrustOrCompany':get.governingBodyOfTrustOrCompany,'NoOfMembersInTrustOrCompany':get.NoOfMembersInTrustOrCompany,'tenureOfEachMemberInTrust':get.tenureOfEachMemberInTrust,'educativePastoralCommunityCouncil':get.educativePastoralCommunityCouncil,'membersOfEducativePastoralComCouncil':get.membersOfEducativePastoralComCouncil,'tenureOfEducativePastoralComCouncil':get.tenureOfEducativePastoralComCouncil,'parentTeacherAssosiateExecuteBody':get.parentTeacherAssosiateExecuteBody,'membersOfParentTeacherExecuteBody':get.membersOfParentTeacherExecuteBody,'tenureOfParentTeacherExecuteBody':get.tenureOfParentTeacherExecuteBody},
        'School7':
        {'studentAssociationCouncil':get.studentAssociationCouncil,'membersOfStudentAssociationCouncil':get.membersOfStudentAssociationCouncil,'tenureOfStudentAssociationCouncil':get.tenureOfStudentAssociationCouncil,'generalGrieveOrComplaintCell':get.generalGrieveOrComplaintCell,'schoolManagementCommittee':get.schoolManagementCommittee,'constitutionOfManagementCommittee':get.constitutionOfManagementCommittee,'membersOfManagementCommittee':get.membersOfManagementCommittee,'tenureOfManagementCommittee':get.tenureOfManagementCommittee},
        'School8':
        {'isSchoolLocatedInRentedOrOwnBuilding':get.isSchoolLocatedInRentedOrOwnBuilding,'areaOfSchoolCampus':get.areaOfSchoolCampus,'builtUpArea':get.builtUpArea,'playGroundArea':get.playGroundArea,'noOfBuildingsOrFloors':get.noOfBuildingsOrFloors,'isProvisionsAvailableDifferently':get.isProvisionsAvailableDifferently,'noOfStairCase':get.noOfStairCase,'noOfLifts':get.noOfLifts},
        'School18':
        {'scholarship':get.scholarship},
        'School19':
        {'enrollment':get.enrollment},
    }


# This method is used to update the School Profile's record.
@router.put("/profileput") 
def updated(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    user.id=str(user.id)
    updated_post=db.query(school_model.Information).filter(school_model.Information.id==user.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    if post.get('scholarship'):    
        post['scholarship']=set_data(post['scholarship'])
    if post.get('enrollment'):
        post['enrollment']=set_data(post["enrollment"])
    updated_post.update(post,synchronize_session=False)
    db.commit()
    return {"id":up.id}



# This method is used to get Specific record from 'School Profile' Data table without Token Validation
@router.get("/get/{id}")
def test_post(id:int,db:Session=Depends(get_db)):
    new_post=db.query(school_model.Information).filter(school_model.Information.id==id)
    new=new_post.first()
    return {"data":new}


# get all records from  'School Profile' Table. 
@router.get("/get")
def test_post(db:Session=Depends(get_db)):
    new_post=db.query(school_model.Information).all()
    return new_post

