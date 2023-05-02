from enum import Enum

HOSTNAME = 'Hostname:'
ROBOT_NO = 'Robot No:'
NA = 'NA'
LINCONL = 'Lincoln'
FRONIUS = 'Fronius'

class BaseEnum(Enum):
    
    @classmethod
    def is_valid_value(cls, value):
        if isinstance(value, list):
            # invalid_values = list(set([member.value.lower() for member in cls]).symmetric_difference(set([val.lower() for val in value])) )
            unfilled_constants = list(set([member.value.lower() for member in cls]) - (set([val.lower() for val in value])) )
            missing_constants = list((set([val.lower() for val in value])) - set([member.value.lower() for member in cls]) )
            valid_constants = all(val.lower() in [member.value.lower() for member in cls] for val in value)
            return valid_constants, unfilled_constants, missing_constants
        else:
            return value.lower() in [member.value.lower() for member in cls], [], []
    
    @classmethod
    def get_all(cls):
        return [member.value for member in cls]
    
class WeldProcedureData(BaseEnum):
    WP = 'WP'
    SCH ='Sch'
    RUNIN = 'Runin'
    BBACK = 'Bback'
    WSTICK = 'Wstick'
    RAMP = 'Ramp'
    MODE = 'Mode'
    DESCRIPTION = 'Description'
    PERRO = 'Perro'
    GATO = 'Gato'

class LincolnWeldScheduleData(BaseEnum):
    NUM = 'Num'
    WFS = 'WFS'
    TRIM = 'Trim'
    ULTIM_ARC = 'UltimArc'
    HOT = 'Hot Start'
    WELD = 'Weld Speed'
    TIME = 'Time'
    COMMENT = 'Comment'

class FroniusWeldScheduleData(BaseEnum):
    NUM = 'Num'
    POWER_CORRRECTION = 'Power correction'
    ARC_LENGTH_CORR = 'Arc length corr'
    JOB_NUMBER = 'Job number'
    WELD = 'Weld Speed'
    TIME = 'Time'
    COMMENT = 'Comment'


