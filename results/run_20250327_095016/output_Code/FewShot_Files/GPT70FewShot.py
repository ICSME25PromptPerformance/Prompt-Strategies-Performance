class PersonRequest:
    """
    This class validates input personal information data and sets invalid fields to None based on specific rules.
    """

    def __init__(self, name: str, sex: str, phoneNumber: str):
        """
        Initialize PersonRequest object with the provided information.
        :param name: str, the name of the person
        :param sex: str, the sex of the person
        :param phoneNumber: str, the phone number of the person
        """
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phoneNumber = self._validate_phoneNumber(phoneNumber)

    def _validate_name(self, name: str) -> str:
        """
        Validate the name and return it. If name is empty or exceeds 33 characters in length, set to None.
        :param name: str, the name to validate
        :return: str, the validated name or None if invalid
        """
        # Check if the name is not empty and does not exceed 33 characters
        if name and len(name) <= 33:
            return name
        return None

    def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not 'Man', 'Woman', or 'UGM', set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """
        # Check if the sex is one of the allowed values
        if sex in ['Man', 'Woman', 'UGM']:
            return sex
        return None

    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        """
        Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
        :param phoneNumber: str, the phone number to validate
        :return: str, the validated phone number or None if invalid
        """
        # Check if the phone number is exactly 11 digits long
        if phoneNumber.isdigit() and len(phoneNumber) == 11:
            return phoneNumber
        return None