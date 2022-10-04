from pydantic import BaseModel
from typing import Optional


class tokenData(BaseModel):
    id:Optional[str]=None




class student(BaseModel):
    id:str
    instiName:str
    state:str
    urlname:str
    location:str
    paddress:str
    city:str
    nostaff:int
    noboys:int
    coname:str
    medium:str
    ofemail:str
    needs:str
    district:str
    pincode:int
    ofphno:str
    acadyear:str
    gender:str
    cunofstu:str
    comono:str
    nameofprince:str
    yearofest:int
    natureofaffili:str
    cunofgirls:int
    nonteaching:int
    coemailid:str
    sclevel:str
    headmono:str
    heademailid:str
    headofphno:str
    instirecog:str
    nameboard:str
    affiliationno:str
    affiliyear:str
    affilipertemp:str
    affilicondition:str
    minstatus:str
    christian:str
    hindu:str
    islam:str
    others:str
    nonbelievers:str
    firecer:str
    sanicer:str
    buildcer:str
    schown:str
    nametrust:str
    registertrust:str
    act:str
    yearregis:str
    registernu:str
    validreg:str
    namepcm:str
    desigpcm:str
    addresspcm:str
    phonepcm:str
    emailpcm:str
    tsc:str
    tscmembers:str
    tsctenure:str
    epcc:str
    epccmembers:str
    epcctenure:str
    pt:str
    ptmembers:str
    pttenure:str
    sacouncil:str
    samembers:str
    satenure:str
    ggcc:str
    schoolmc:str
    constitutionmc:str
    mcmembers:str
    mctenure:str
    schlocation:str
    scharea:str
    builduparea:str
    playarea:str
    nobuildings:str
    differentlyavail:str
    noofstairs:str
    nooflifts:str
    croom:str
    sroom:str
    pl:str
    cl:str
    bl:str
    ml:str
    csl:str
    ll:str
    hsl:str
    library:str
    audit:str
    cr:str
    up:str
    prc:str
    sickr:str
    canteen:str
    sr:str
    orh:str
    sut:str
    stut:str
    rooms:str
    speneeds:str
    handlesn:str
    bw:str
    bwyes:str
    cctv:str
    ds:str
    hmcamera:str
    msg:str
    hmmalesg:str
    femalesg:str
    hwfemalesg:str
    drinkingwf:str
    pdf:str
    mms:str
    nobuses:str
    gpsec:str
    nola:str
    firstak:str
    drinkingwa:str
    nobusessc:str
    efgfbp:str
    freetsobts:str
    # mmfainsch:str
    lot:str
    lct:str
    tnolb:str
    tnolm:str
    tnold:str
    tnoeb:str
    oalr:str
    slfps:str
    provisionrt:str
    mmfas1:bool
    mmfas2:bool
    mmfas3:bool
    mmfas4:bool
    mmfas5:bool
    phmpmale:int
    phmpfmale:int
    phmtmale:int
    phmtfmale:int
    # phmTmale:int
    # phmTfmale:int
    vppmale:int
    vppfmale:int
    vptmale:int
    vptfmale:int
    # vpTmale:int
    # vpTfmale:int
    PGTpmale:int
    PGTpfmale:int
    PGTtmale:int
    PGTtfmale:int
    # PGTTmale:int
    # PGTTfmale:int	
    TGTpmale:int
    TGTpfmale:int
    TGTtmale:int
    TGTtfmale:int
    # TGTTmale:int
    # TGTTfmale:int
    PRTpmale:int
    PRTpfmale:int
    PRTtmale:int
    PRTtfmale:int
    # PRTTmale:int
    # PRTTfmale:int
    NTTpmale:int
    NTTpfmale:int
    NTTtmale:int
    NTTtfmale:int
    # NTTTmale:int
    # NTTTfmale:int
    UTpmale:int
    UTpfmale:int
    UTtmale:int
    UTtfmale:int
    # UTTmale:int
    # UTTfmale:int
    Lpmale:int
    Lpfmale:int
    Ltmale:int
    Ltfmale:int
    # LTmale:int
    # LTfmale:int
    Artspmale:int
    Artspfmale:int
    Artstmale:int
    Artstfmale:int
    # ArtsTmale:int
    # ArtsTfmale:int
    Cpmale:int
    Cpfmale:int
    Ctmale:int
    Ctfmale:int
    # CTmale:int
    # CTfmale:int
    CLpmale:int
    CLpfmale:int
    CLtmale:int
    CLtfmale:int
    # CLTmale:int
    # CLTfmale:int
    FMpmale:int
    FMpfmale:int
    FMtmale:int
    FMtfmale:int
    # FMTmale:int
    # FMTfmale:int
    Nursepmale:int
    Nursepfmale:int
    Nursetmale:int
    Nursetfmale:int
    # NurseTmale:int
    # NurseTfmale:int
    PTpmale:int
    PTpfmale:int
    PTtmale:int
    PTtfmale:int
    # PTTmale:int
    # PTTfmale:int
    # Totalpmale:int
    # Totalpfmale:int
    # Totaltmale:int
    # Totaltfmale:int
    # TotalTmale:int
    # TotalTfmale:int
    ofmaper:int
    ofmatemp:int
    ofmapart:int
    # ofmatotal:int
    ofasper:int
    ofastemp:int
    ofaspart:int
    # ofastotal:int
    clerkper:int
    clerktemp:int
    clerkpart:int
    # clerktotal:int
    labper:int
    labtemp:int
    labpart:int
    # labtotal:int
    accountper:int
    accounttemp:int
    accountpart:int
    # accounttotal:int
    peonsper:int
    peonstemp:int
    peonspart:int
    # peonstotal:int
    othersper:int
    otherstemp:int
    otherspart:int
    # otherstotal:int


    no_of_activities:int
    no_of_groups:int
    no_of_community:int
    no_of_sports_school:int
    no_of_sports_zonal:int
    no_of_sports_district:int
    no_of_sports_state:int
    no_of_sports_national:int
    no_of_sports_international:int
    no_of_competition_school:int
    no_of_competition_zonal:int
    no_of_competition_district:int
    no_of_competition_state:int
    no_of_competition_national:int
    no_of_competition_international:int
    no_of_interprograms_school:int
    no_of_interprograms_zonal:int
    no_of_interprograms_district:int
    no_of_interprograms_state:int
    no_of_interprograms_national:int
    no_of_interprograms_international:int

    acad_year_begins:str
    acad_year_ends:str
    workingdays_21_22:int
    workingdays_20_21:int
    workingdays_19_20:int
    eachday_workhours_21_22:int
    eachday_workhours_20_21:int
    eachday_workhours_19_20:int
    totalhours_21_22:int
    totalhours_20_21:int
    totalhours_19_20:int
    non_instruct_workdays_21_22:int
    non_instruct_workdays_20_21:int
    non_instruct_workdays_19_20:int
    holiday_except_holidays_21_22:int
    holiday_except_holidays_20_21:int
    holiday_except_holidays_19_20:int
    teaching_periods_perweek:int
    faith_periods_perweek:int
    period_duration:int
    totalhours_forclubs:int
    summer_timein:str
    summer_timeout:str
    winter_timein:str
    winter_timeout:str
    school_shift:str