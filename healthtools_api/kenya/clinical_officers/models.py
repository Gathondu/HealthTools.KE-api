

class ClinicalOfficer(object):
    def __init__(self, **kwargs):
        """represent a clinical officer model"""
        fields = [
            'id', 'name', 'reg_date', 'reg_no',
            'valid_dates', 'address', 'qualifications'
        ]
        for field in fields:
            setattr(self, field, kwargs.get(field, None))
