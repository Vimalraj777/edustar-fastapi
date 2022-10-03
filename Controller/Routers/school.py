from ctypes.wintypes import PINT
import imp
from multiprocessing import synchronize
from pickle import GLOBAL
from pyexpat import model
from typing import Set
# from webbrowser import get
from fastapi import status,HTTPException , APIRouter , Depends
from sqlalchemy import false
from sqlalchemy.orm import Session , relationship
from Utils import utils
from Databases.database import get_db
# from Model import user_profile
from Model import school_model
from Schema import school_schema
from Authorization import oauth2
from sqlalchemy.orm import load_only




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
@router.post("/postSchool") 
def crate_post(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    if post.get('scholarship'):
        post['scholarship']=set_data(post['scholarship'])
    if post.get('enrollment'):
        post['enrollment']=set_data(post['enrollment'])
    new_post=school_model.Information( **post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post.id}



# This method is used to get the logged in user's record from 'School Profile' Data Table.
@router.get("/getSchool")
def test_post(db:Session=Depends(get_db),user_id:str=Depends(oauth2.get_current_user)):
    user_id.id=str(user_id.id)
    new_post=db.query(school_model.Information).filter(school_model.Information.id==user_id.id)
    get=new_post.first()
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
        'School9':
        {'classRooms':get.classRooms,'staffRooms':get.staffRooms,'physicsLab':get.physicsLab,'chemistryLab':get.chemistryLab,'biologyLab':get.biologyLab,'mathsLab':get.mathsLab,'computerScienceLab':get.computerScienceLab,'languageLab':get.languageLab,'homeScienceLab':get.homeScienceLab,'library':get.library,'auditorium':get.auditorium,'counselorsRoom':get.counselorsRoom,'visitorsParlor':get.visitorsParlor,'prayerRoomChapel':get.prayerRoomChapel,'sickRoomOrInfirmary':get.sickRoomOrInfirmary,'canteen':get.canteen,'securityRoom':get.securityRoom,'otherRoomsHalls':get.otherRoomsHalls,'staffUrinalsOrToilets':get.staffUrinalsOrToilets,'studentUrinalsOrToilets':get.studentUrinalsOrToilets,'rooms':get.rooms,'isChildNeedSpecialNeeds':get.isChildNeedSpecialNeeds,'teachersToHandleSpecialChild':get.teachersToHandleSpecialChild},
        'School10':
        {'boundaryWall':get.boundaryWall,'ifYesBoundaryWall':get.ifYesBoundaryWall,'cctv':get.cctv,'isDataSaved':get.isDataSaved,'noOfCameras':get.noOfCameras,'maleSecurityGuard':get.maleSecurityGuard,'noOfMaleSecurity':get.noOfMaleSecurity,'femaleSecurityGuards':get.femaleSecurityGuards,'noOfFemaleSecurity':get.noOfFemaleSecurity,'drinkingWaterFacility':get.drinkingWaterFacility,'properDrainageFacility':get.properDrainageFacility},
        'School11':
        {'middayMealScheme':get.middayMealScheme,'noOfSchoolBuses':get.noOfSchoolBuses,'gpsEnabledCamera':get.gpsEnabledCamera,'noOfLadyAttendor':get.noOfLadyAttendor,'firstAidKit':get.firstAidKit,'drinkingWater':get.drinkingWater,'noOfBusesSubContracted':get.noOfBusesSubContracted,'govtFreeBusPassEligiblity':get.govtFreeBusPassEligiblity,'IsSchoolOffersFreeTransportFacility':get.IsSchoolOffersFreeTransportFacility},
        'School12':
        {'libraryOpenTime':get.libraryOpenTime,'libraryCloseTime':get.libraryCloseTime,'totalNoOfLibraryBooks':get.totalNoOfLibraryBooks,'totalNoOfLibraryMagazines':get.totalNoOfLibraryMagazines,'totalNoOfLibraryDailyNewspapers':get.totalNoOfLibraryDailyNewspapers,'totalNoOfEbooks':get.totalNoOfEbooks,'onlineAccessForLibraryBooks':get.onlineAccessForLibraryBooks,'seperateLibraryForPrimarySection':get.seperateLibraryForPrimarySection,'provisionForRemedialTeaching':get.provisionForRemedialTeaching,'televisionFacilityInSchool':get.televisionFacilityInSchool,'digitalBoardsFacilityInSchool':get.digitalBoardsFacilityInSchool,'multimediaFacilityInSchool':get.multimediaFacilityInSchool,'projectorFacilityInSchool':get.projectorFacilityInSchool,'tapeRecorderFacilityInSchool':get.tapeRecorderFacilityInSchool},
        'School13':
        {'permanentMaleForPrincipalOrHM':get.permanentMaleForPrincipalOrHM,'permanentFeMaleForPrincipalOrHM':get.permanentFeMaleForPrincipalOrHM,'temporaryMaleForPrincipalOrHM':get.temporaryMaleForPrincipalOrHM,'temporaryFeMaleForPrincipalOrHM':get.temporaryFeMaleForPrincipalOrHM,'permanentMaleForVicePrincipalOrHM':get.permanentMaleForVicePrincipalOrHM,'permanentFeMaleForVicePrincipalOrHM':get.permanentFeMaleForVicePrincipalOrHM,'temporaryMaleForVicePrincipalOrHM':get.temporaryMaleForVicePrincipalOrHM,'temporaryFeMaleForVicePrincipalOrHM':get.temporaryFeMaleForVicePrincipalOrHM,'permanentMalePostGraduateTeachers':get.permanentMalePostGraduateTeachers,'permanentFeMalePostGraduateTeachers':get.permanentFeMalePostGraduateTeachers,'temporaryMalePostGraduateTeachers':get.temporaryMalePostGraduateTeachers,
        'temporaryFeMalePostGraduateTeachers':get.temporaryFeMalePostGraduateTeachers,'permanentMaleTrainedGraduateTeachers':get.permanentMaleTrainedGraduateTeachers,'permanentFeMaleTrainedGraduateTeachers':get.permanentFeMaleTrainedGraduateTeachers,'temporaryMaleTrainedGraduateTeachers':get.temporaryMaleTrainedGraduateTeachers,'temporaryFeMaleTrainedGraduateTeachers':get.temporaryFeMaleTrainedGraduateTeachers,'permanentMalePrimaryTeachers':get.permanentMalePrimaryTeachers,'permanentFeMalePrimaryTeachers':get.permanentFeMalePrimaryTeachers,'temporaryMalePrimaryTeachers':get.temporaryMalePrimaryTeachers,'temporaryFeMalePrimaryTeachers':get.temporaryFeMalePrimaryTeachers,'permanentMaleNurseryTrainedTeachers':get.permanentMaleNurseryTrainedTeachers,'permanentFeMaleNurseryTrainedTeachers':get.permanentFeMaleNurseryTrainedTeachers,
        'temporaryMaleNurseryTrainedTeachers':get.temporaryMaleNurseryTrainedTeachers,'temporaryFeMaleNurseryTrainedTeachers':get.temporaryFeMaleNurseryTrainedTeachers,'permanentMaleUntrainedTeachers':get.permanentMaleUntrainedTeachers,'permanentFeMaleUntrainedTeachers':get.permanentFeMaleUntrainedTeachers,'UTtmtemporaryMaleUntrainedTeachersale':get.UTtmtemporaryMaleUntrainedTeachersale,'temporaryFeMaleUntrainedTeachers':get.temporaryFeMaleUntrainedTeachers,'permanentMaleLibrarian':get.permanentMaleLibrarian,'permanentFeMaleLibrarian':get.permanentFeMaleLibrarian,'temporaryMaleLibrarian':get.temporaryMaleLibrarian,'temporaryFeMaleLibrarian':get.temporaryFeMaleLibrarian,'permanentMaleArtsDanceMusicTeachers':get.permanentMaleArtsDanceMusicTeachers,'permanentFeMaleArtsDanceMusicTeachers':get.permanentFeMaleArtsDanceMusicTeachers,
        'temporaryMaleArtsDanceMusicTeachers':get.temporaryMaleArtsDanceMusicTeachers,'temporaryFeMaleArtsDanceMusicTeachers':get.temporaryFeMaleArtsDanceMusicTeachers,'permanentMaleCounsilors':get.permanentMaleCounsilors,'permanentFeMaleCounsilors':get.permanentFeMaleCounsilors,'temporaryMaleCounsilors':get.temporaryMaleCounsilors,'temporaryFeMaleCounsilors':get.temporaryFeMaleCounsilors,'permanentMaleComputerLiteracy':get.permanentMaleComputerLiteracy,'permanentFeMaleComputerLiteracy':get.permanentFeMaleComputerLiteracy,'temporaryMaleComputerLiteracy':get.temporaryMaleComputerLiteracy,'temporaryFeMaleComputerLiteracy':get.temporaryFeMaleComputerLiteracy,'permanentMaleFaithMinisters':get.permanentMaleFaithMinisters,'permanentFeMaleFaithMinisters':get.permanentFeMaleFaithMinisters,
        'temporaryMaleFaithMinisters':get.temporaryMaleFaithMinisters,'temporaryFeMaleFaithMinisters':get.temporaryFeMaleFaithMinisters,'permanentMaleNurse':get.permanentMaleNurse,'permanentFeMaleNurse':get.permanentFeMaleNurse,'temporaryMaleNurse':get.temporaryMaleNurse,'temporaryFeMaleNurse':get.temporaryFeMaleNurse,'permanentMalePTTeachers':get.permanentMalePTTeachers,'permanentFeMalePTTeachers':get.permanentFeMalePTTeachers,'temporaryMalePTTeachers':get.temporaryMalePTTeachers,'temporaryFeMalePTTeachers':get.temporaryFeMalePTTeachers},
        'School14':
        {'permanentOfficeManagers':get.permanentOfficeManagers,'temporaryOfficeManagers':get.temporaryOfficeManagers,'partTimeOfficeManagers':get.partTimeOfficeManagers,'permanentOfficeAssistant':get.permanentOfficeAssistant,'temporaryOfficeAssistant':get.temporaryOfficeAssistant,'partTimeOfficeAssistant':get.partTimeOfficeAssistant,'permanentClerks':get.permanentClerks,'temporaryClerks':get.temporaryClerks,'partTimeClerks':get.partTimeClerks,'permanentLabAttendants':get.permanentLabAttendants,'temporaryLabAttendants':get.temporaryLabAttendants,'partTimeLabAttendants':get.partTimeLabAttendants,'permanentAccountant':get.permanentAccountant,'temporaryAccountant':get.temporaryAccountant,'partTimeAccountant':get.partTimeAccountant,'permanentPeonsOrClerks':get.permanentPeonsOrClerks,'temporaryPeonsOrClerks':get.temporaryPeonsOrClerks,
        'partTimePeonsOrClerks':get.partTimePeonsOrClerks,'permanentOthers':get.permanentOthers,'temporaryOthers':get.temporaryOthers,'partTimeOthers':get.partTimeOthers},
        'School15':
        {'noOfActivitiesCarriedOut':get.noOfActivitiesCarriedOut,'noOfGroupsClubsMovementsPresent':get.noOfGroupsClubsMovementsPresent,'noOfCommunityServicesDoneInLastYear':get.noOfCommunityServicesDoneInLastYear,'noOfSportsSchool':get.noOfSportsSchool,'noOfSportsZonal':get.noOfSportsZonal,'noOfSportsDistrict':get.noOfSportsDistrict,'noOfSportsState':get.noOfSportsState,'noOfSportsNational':get.noOfSportsNational,'noOfSportsInternational':get.noOfSportsInternational,'noOfCompetitionsParticipatedLastYearInSchool':get.noOfCompetitionsParticipatedLastYearInSchool,'noOfCompetitionsParticipatedLastYearInZonal':get.noOfCompetitionsParticipatedLastYearInZonal,'noOfCompetitionsParticipatedLastYearInDistrict':get.noOfCompetitionsParticipatedLastYearInDistrict,'noOfCompetitionsParticipatedLastYearInState':get.noOfCompetitionsParticipatedLastYearInState,
        'noOfCompetitionsParticipatedLastYearInNational':get.noOfCompetitionsParticipatedLastYearInNational,'noOfCompetitionsParticipatedLastYearInInterNational':get.noOfCompetitionsParticipatedLastYearInInterNational,'noOfInterSchoolProgramsOrganizedInSchoolLevel':get.noOfInterSchoolProgramsOrganizedInSchoolLevel,'noOfInterSchoolProgramsOrganizedInZonalLevel':get.noOfInterSchoolProgramsOrganizedInZonalLevel,'noOfInterSchoolProgramsOrganizedInDistrictLevel':get.noOfInterSchoolProgramsOrganizedInDistrictLevel,'noOfInterSchoolProgramsOrganizedInStateLevel':get.noOfInterSchoolProgramsOrganizedInStateLevel,'noOfInterSchoolProgramsOrganizedInNationalLevel':get.noOfInterSchoolProgramsOrganizedInNationalLevel,'noOfInterSchoolProgramsOrganizedInInterNationalLevel':get.noOfInterSchoolProgramsOrganizedInInterNationalLevel},
        'School16':
        {'academicYearBeginMonth':get.academicYearBeginMonth,'academicYearEndMonth':get.academicYearEndMonth,'noOfWorkingDaysIn21To22':get.noOfWorkingDaysIn21To22,'noOfWorkingDaysIn20To21':get.noOfWorkingDaysIn20To21,'noOfWorkingDaysIn19To20':get.noOfWorkingDaysIn19To20,'hoursOfAcademicWorkEachDay21To22':get.hoursOfAcademicWorkEachDay21To22,'hoursOfAcademicWorkEachDay20To21':get.hoursOfAcademicWorkEachDay20To21,'hoursOfAcademicWorkEachDay19To20':get.hoursOfAcademicWorkEachDay19To20,'totalInstructionalHours21To22':get.totalInstructionalHours21To22,'totalInstructionalHours20To21':get.totalInstructionalHours20To21,'totalInstructionalHours19To20':get.totalInstructionalHours19To20,'nonInstructionalWorkingDaysForStaffIn21To22':get.nonInstructionalWorkingDaysForStaffIn21To22,
        'nonInstructionalWorkingDaysForStaffIn20To21':get.nonInstructionalWorkingDaysForStaffIn20To21,'nonInstructionalWorkingDaysForStaffIn19To20':get.nonInstructionalWorkingDaysForStaffIn19To20,'noOfHolidaysExceptNationalHolidays21To22':get.noOfHolidaysExceptNationalHolidays21To22,'noOfHolidaysExceptNationalHolidays20To21':get.noOfHolidaysExceptNationalHolidays20To21,'noOfHolidaysExceptNationalHolidays19To20':get.noOfHolidaysExceptNationalHolidays19To20},
        'School17':
        {'noOfTeachingPeriodPerWeek':get.noOfTeachingPeriodPerWeek,'noOfFaithPeriodsPerWeek':get.noOfFaithPeriodsPerWeek,'teachingPeriodDuration':get.teachingPeriodDuration,'noOfHoursForActivitiesInTheClubs':get.noOfHoursForActivitiesInTheClubs,'schoolTimeInSummerToCome':get.schoolTimeInSummerToCome,'schoolTimeInSummerToOut':get.schoolTimeInSummerToOut,'schoolTimeInWinterToCome':get.schoolTimeInWinterToCome,'schoolTimeInWinterToOut':get.schoolTimeInWinterToOut,'isSchoolWorkingInShifts':get.isSchoolWorkingInShifts},
        'School18':
        {'scholarship':get.scholarship},
        'School19':
        {'enrollment':get.enrollment},
    }


# This method is used to update the School Profile's record.
@router.put("/updateSchool") 
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




# return all the data of School Table
@router.get("/homepageget")
def test_post(db:Session=Depends(get_db)):
    user_id=db.query(school_model.Information).all()
    return {'values':user_id}







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

@router.get('/getSchoolPost/{id}')
def getSchoolPost(id:str,db:Session=Depends(get_db)):
    get=db.query(school_model.Information).filter(school_model.Information.id==id).first()
    # return new_post
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
        'School9':
        {'classRooms':get.classRooms,'staffRooms':get.staffRooms,'physicsLab':get.physicsLab,'chemistryLab':get.chemistryLab,'biologyLab':get.biologyLab,'mathsLab':get.mathsLab,'computerScienceLab':get.computerScienceLab,'languageLab':get.languageLab,'homeScienceLab':get.homeScienceLab,'library':get.library,'auditorium':get.auditorium,'counselorsRoom':get.counselorsRoom,'visitorsParlor':get.visitorsParlor,'prayerRoomChapel':get.prayerRoomChapel,'sickRoomOrInfirmary':get.sickRoomOrInfirmary,'canteen':get.canteen,'securityRoom':get.securityRoom,'otherRoomsHalls':get.otherRoomsHalls,'staffUrinalsOrToilets':get.staffUrinalsOrToilets,'studentUrinalsOrToilets':get.studentUrinalsOrToilets,'rooms':get.rooms,'isChildNeedSpecialNeeds':get.isChildNeedSpecialNeeds,'teachersToHandleSpecialChild':get.teachersToHandleSpecialChild},
        'School10':
        {'boundaryWall':get.boundaryWall,'ifYesBoundaryWall':get.ifYesBoundaryWall,'cctv':get.cctv,'isDataSaved':get.isDataSaved,'noOfCameras':get.noOfCameras,'maleSecurityGuard':get.maleSecurityGuard,'noOfMaleSecurity':get.noOfMaleSecurity,'femaleSecurityGuards':get.femaleSecurityGuards,'noOfFemaleSecurity':get.noOfFemaleSecurity,'drinkingWaterFacility':get.drinkingWaterFacility,'properDrainageFacility':get.properDrainageFacility},
        'School11':
        {'middayMealScheme':get.middayMealScheme,'noOfSchoolBuses':get.noOfSchoolBuses,'gpsEnabledCamera':get.gpsEnabledCamera,'noOfLadyAttendor':get.noOfLadyAttendor,'firstAidKit':get.firstAidKit,'drinkingWater':get.drinkingWater,'noOfBusesSubContracted':get.noOfBusesSubContracted,'govtFreeBusPassEligiblity':get.govtFreeBusPassEligiblity,'IsSchoolOffersFreeTransportFacility':get.IsSchoolOffersFreeTransportFacility},
        'School12':
        {'libraryOpenTime':get.libraryOpenTime,'libraryCloseTime':get.libraryCloseTime,'totalNoOfLibraryBooks':get.totalNoOfLibraryBooks,'totalNoOfLibraryMagazines':get.totalNoOfLibraryMagazines,'totalNoOfLibraryDailyNewspapers':get.totalNoOfLibraryDailyNewspapers,'totalNoOfEbooks':get.totalNoOfEbooks,'onlineAccessForLibraryBooks':get.onlineAccessForLibraryBooks,'seperateLibraryForPrimarySection':get.seperateLibraryForPrimarySection,'provisionForRemedialTeaching':get.provisionForRemedialTeaching,'televisionFacilityInSchool':get.televisionFacilityInSchool,'digitalBoardsFacilityInSchool':get.digitalBoardsFacilityInSchool,'multimediaFacilityInSchool':get.multimediaFacilityInSchool,'projectorFacilityInSchool':get.projectorFacilityInSchool,'tapeRecorderFacilityInSchool':get.tapeRecorderFacilityInSchool},
        'School13':
        {'permanentMaleForPrincipalOrHM':get.permanentMaleForPrincipalOrHM,'permanentFeMaleForPrincipalOrHM':get.permanentFeMaleForPrincipalOrHM,'temporaryMaleForPrincipalOrHM':get.temporaryMaleForPrincipalOrHM,'temporaryFeMaleForPrincipalOrHM':get.temporaryFeMaleForPrincipalOrHM,'permanentMaleForVicePrincipalOrHM':get.permanentMaleForVicePrincipalOrHM,'permanentFeMaleForVicePrincipalOrHM':get.permanentFeMaleForVicePrincipalOrHM,'temporaryMaleForVicePrincipalOrHM':get.temporaryMaleForVicePrincipalOrHM,'temporaryFeMaleForVicePrincipalOrHM':get.temporaryFeMaleForVicePrincipalOrHM,'permanentMalePostGraduateTeachers':get.permanentMalePostGraduateTeachers,'permanentFeMalePostGraduateTeachers':get.permanentFeMalePostGraduateTeachers,'temporaryMalePostGraduateTeachers':get.temporaryMalePostGraduateTeachers,
        'temporaryFeMalePostGraduateTeachers':get.temporaryFeMalePostGraduateTeachers,'permanentMaleTrainedGraduateTeachers':get.permanentMaleTrainedGraduateTeachers,'permanentFeMaleTrainedGraduateTeachers':get.permanentFeMaleTrainedGraduateTeachers,'temporaryMaleTrainedGraduateTeachers':get.temporaryMaleTrainedGraduateTeachers,'temporaryFeMaleTrainedGraduateTeachers':get.temporaryFeMaleTrainedGraduateTeachers,'permanentMalePrimaryTeachers':get.permanentMalePrimaryTeachers,'permanentFeMalePrimaryTeachers':get.permanentFeMalePrimaryTeachers,'temporaryMalePrimaryTeachers':get.temporaryMalePrimaryTeachers,'temporaryFeMalePrimaryTeachers':get.temporaryFeMalePrimaryTeachers,'permanentMaleNurseryTrainedTeachers':get.permanentMaleNurseryTrainedTeachers,'permanentFeMaleNurseryTrainedTeachers':get.permanentFeMaleNurseryTrainedTeachers,
        'temporaryMaleNurseryTrainedTeachers':get.temporaryMaleNurseryTrainedTeachers,'temporaryFeMaleNurseryTrainedTeachers':get.temporaryFeMaleNurseryTrainedTeachers,'permanentMaleUntrainedTeachers':get.permanentMaleUntrainedTeachers,'permanentFeMaleUntrainedTeachers':get.permanentFeMaleUntrainedTeachers,'UTtmtemporaryMaleUntrainedTeachersale':get.UTtmtemporaryMaleUntrainedTeachersale,'temporaryFeMaleUntrainedTeachers':get.temporaryFeMaleUntrainedTeachers,'permanentMaleLibrarian':get.permanentMaleLibrarian,'permanentFeMaleLibrarian':get.permanentFeMaleLibrarian,'temporaryMaleLibrarian':get.temporaryMaleLibrarian,'temporaryFeMaleLibrarian':get.temporaryFeMaleLibrarian,'permanentMaleArtsDanceMusicTeachers':get.permanentMaleArtsDanceMusicTeachers,'permanentFeMaleArtsDanceMusicTeachers':get.permanentFeMaleArtsDanceMusicTeachers,
        'temporaryMaleArtsDanceMusicTeachers':get.temporaryMaleArtsDanceMusicTeachers,'temporaryFeMaleArtsDanceMusicTeachers':get.temporaryFeMaleArtsDanceMusicTeachers,'permanentMaleCounsilors':get.permanentMaleCounsilors,'permanentFeMaleCounsilors':get.permanentFeMaleCounsilors,'temporaryMaleCounsilors':get.temporaryMaleCounsilors,'temporaryFeMaleCounsilors':get.temporaryFeMaleCounsilors,'permanentMaleComputerLiteracy':get.permanentMaleComputerLiteracy,'permanentFeMaleComputerLiteracy':get.permanentFeMaleComputerLiteracy,'temporaryMaleComputerLiteracy':get.temporaryMaleComputerLiteracy,'temporaryFeMaleComputerLiteracy':get.temporaryFeMaleComputerLiteracy,'permanentMaleFaithMinisters':get.permanentMaleFaithMinisters,'permanentFeMaleFaithMinisters':get.permanentFeMaleFaithMinisters,
        'temporaryMaleFaithMinisters':get.temporaryMaleFaithMinisters,'temporaryFeMaleFaithMinisters':get.temporaryFeMaleFaithMinisters,'permanentMaleNurse':get.permanentMaleNurse,'permanentFeMaleNurse':get.permanentFeMaleNurse,'temporaryMaleNurse':get.temporaryMaleNurse,'temporaryFeMaleNurse':get.temporaryFeMaleNurse,'permanentMalePTTeachers':get.permanentMalePTTeachers,'permanentFeMalePTTeachers':get.permanentFeMalePTTeachers,'temporaryMalePTTeachers':get.temporaryMalePTTeachers,'temporaryFeMalePTTeachers':get.temporaryFeMalePTTeachers},
        'School14':
        {'permanentOfficeManagers':get.permanentOfficeManagers,'temporaryOfficeManagers':get.temporaryOfficeManagers,'partTimeOfficeManagers':get.partTimeOfficeManagers,'permanentOfficeAssistant':get.permanentOfficeAssistant,'temporaryOfficeAssistant':get.temporaryOfficeAssistant,'partTimeOfficeAssistant':get.partTimeOfficeAssistant,'permanentClerks':get.permanentClerks,'temporaryClerks':get.temporaryClerks,'partTimeClerks':get.partTimeClerks,'permanentLabAttendants':get.permanentLabAttendants,'temporaryLabAttendants':get.temporaryLabAttendants,'partTimeLabAttendants':get.partTimeLabAttendants,'permanentAccountant':get.permanentAccountant,'temporaryAccountant':get.temporaryAccountant,'partTimeAccountant':get.partTimeAccountant,'permanentPeonsOrClerks':get.permanentPeonsOrClerks,'temporaryPeonsOrClerks':get.temporaryPeonsOrClerks,
        'partTimePeonsOrClerks':get.partTimePeonsOrClerks,'permanentOthers':get.permanentOthers,'temporaryOthers':get.temporaryOthers,'partTimeOthers':get.partTimeOthers},
        'School15':
        {'noOfActivitiesCarriedOut':get.noOfActivitiesCarriedOut,'noOfGroupsClubsMovementsPresent':get.noOfGroupsClubsMovementsPresent,'noOfCommunityServicesDoneInLastYear':get.noOfCommunityServicesDoneInLastYear,'noOfSportsSchool':get.noOfSportsSchool,'noOfSportsZonal':get.noOfSportsZonal,'noOfSportsDistrict':get.noOfSportsDistrict,'noOfSportsState':get.noOfSportsState,'noOfSportsNational':get.noOfSportsNational,'noOfSportsInternational':get.noOfSportsInternational,'noOfCompetitionsParticipatedLastYearInSchool':get.noOfCompetitionsParticipatedLastYearInSchool,'noOfCompetitionsParticipatedLastYearInZonal':get.noOfCompetitionsParticipatedLastYearInZonal,'noOfCompetitionsParticipatedLastYearInDistrict':get.noOfCompetitionsParticipatedLastYearInDistrict,'noOfCompetitionsParticipatedLastYearInState':get.noOfCompetitionsParticipatedLastYearInState,
        'noOfCompetitionsParticipatedLastYearInNational':get.noOfCompetitionsParticipatedLastYearInNational,'noOfCompetitionsParticipatedLastYearInInterNational':get.noOfCompetitionsParticipatedLastYearInInterNational,'noOfInterSchoolProgramsOrganizedInSchoolLevel':get.noOfInterSchoolProgramsOrganizedInSchoolLevel,'noOfInterSchoolProgramsOrganizedInZonalLevel':get.noOfInterSchoolProgramsOrganizedInZonalLevel,'noOfInterSchoolProgramsOrganizedInDistrictLevel':get.noOfInterSchoolProgramsOrganizedInDistrictLevel,'noOfInterSchoolProgramsOrganizedInStateLevel':get.noOfInterSchoolProgramsOrganizedInStateLevel,'noOfInterSchoolProgramsOrganizedInNationalLevel':get.noOfInterSchoolProgramsOrganizedInNationalLevel,'noOfInterSchoolProgramsOrganizedInInterNationalLevel':get.noOfInterSchoolProgramsOrganizedInInterNationalLevel},
        'School16':
        {'academicYearBeginMonth':get.academicYearBeginMonth,'academicYearEndMonth':get.academicYearEndMonth,'noOfWorkingDaysIn21To22':get.noOfWorkingDaysIn21To22,'noOfWorkingDaysIn20To21':get.noOfWorkingDaysIn20To21,'noOfWorkingDaysIn19To20':get.noOfWorkingDaysIn19To20,'hoursOfAcademicWorkEachDay21To22':get.hoursOfAcademicWorkEachDay21To22,'hoursOfAcademicWorkEachDay20To21':get.hoursOfAcademicWorkEachDay20To21,'hoursOfAcademicWorkEachDay19To20':get.hoursOfAcademicWorkEachDay19To20,'totalInstructionalHours21To22':get.totalInstructionalHours21To22,'totalInstructionalHours20To21':get.totalInstructionalHours20To21,'totalInstructionalHours19To20':get.totalInstructionalHours19To20,'nonInstructionalWorkingDaysForStaffIn21To22':get.nonInstructionalWorkingDaysForStaffIn21To22,
        'nonInstructionalWorkingDaysForStaffIn20To21':get.nonInstructionalWorkingDaysForStaffIn20To21,'nonInstructionalWorkingDaysForStaffIn19To20':get.nonInstructionalWorkingDaysForStaffIn19To20,'noOfHolidaysExceptNationalHolidays21To22':get.noOfHolidaysExceptNationalHolidays21To22,'noOfHolidaysExceptNationalHolidays20To21':get.noOfHolidaysExceptNationalHolidays20To21,'noOfHolidaysExceptNationalHolidays19To20':get.noOfHolidaysExceptNationalHolidays19To20},
        'School17':
        {'noOfTeachingPeriodPerWeek':get.noOfTeachingPeriodPerWeek,'noOfFaithPeriodsPerWeek':get.noOfFaithPeriodsPerWeek,'teachingPeriodDuration':get.teachingPeriodDuration,'noOfHoursForActivitiesInTheClubs':get.noOfHoursForActivitiesInTheClubs,'schoolTimeInSummerToCome':get.schoolTimeInSummerToCome,'schoolTimeInSummerToOut':get.schoolTimeInSummerToOut,'schoolTimeInWinterToCome':get.schoolTimeInWinterToCome,'schoolTimeInWinterToOut':get.schoolTimeInWinterToOut,'isSchoolWorkingInShifts':get.isSchoolWorkingInShifts},
        'School18':
        {'scholarship':get.scholarship},
        'School19':
        {'enrollment':get.enrollment},
    }

@router.put("/updatePostSchool/{id}")
def updatePostSchool(id:str,data:dict,db:Session=Depends(get_db)):
        updated_post=db.query(school_model.Information).filter(school_model.Information.id==id)
        if data.get('scholarship'):    
            data['scholarship']=set_data(data['scholarship'])
        if data.get('enrollment'):
            data['enrollment']=set_data(data["enrollment"])
        updated_post.update(data,synchronize_session=False)
        db.commit()
        return 'success'


@router.post("/postSchoolPost") 
def createPost(post:dict,db:Session=Depends(get_db)):
    checkData=db.query(school_model.Information).filter(school_model.Information.id==post['profileId'])
    if checkData.first():
        updated_post=db.query(school_model.Information).filter(school_model.Information.id==post['profileId'])
        post.pop('profileId')
        if post.get('scholarship'):    
            post['scholarship']=set_data(post['scholarship'])
        if post.get('enrollment'):
            post['enrollment']=set_data(post["enrollment"])
        updated_post.update(post,synchronize_session=False)
        db.commit()
        return {"data":'success put'}
    else:
        post.pop('profileId')
        if post.get('scholarship'):    
            post['scholarship']=set_data(post['scholarship'])
        if post.get('enrollment'):
            post['enrollment']=set_data(post["enrollment"])
        new_post=school_model.Information(**post)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return {"data":'success post'}

    


@router.delete('/deleteSchool/{id}')
def deleteSchool(id:str,db:Session=Depends(get_db)):
    result=db.query(school_model.Information).filter(school_model.Information.id==id).first()
    db.delete(result)
    db.commit()
    return {'result':'deleted successfully'}    

